from pathlib import Path
import math

from dotenv import load_dotenv
from openai import OpenAI
from agents import function_tool


BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"

load_dotenv()

client = OpenAI()

EMBEDDING_MODEL = "text-embedding-3-small"


def load_documents():
    """knowledge 폴더의 Markdown 문서를 읽는다."""
    documents = []

    for path in KNOWLEDGE_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")

        documents.append({
            "filename": path.name,
            "content": text,
        })

    return documents


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100):
    """
    문서를 작은 chunk로 나눈다.

    chunk_size:
        한 chunk의 최대 문자 수

    overlap:
        앞 chunk와 겹치는 문자 수
    """

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def create_embedding(text: str):
    """텍스트를 embedding vector로 변환한다."""

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )

    return response.data[0].embedding


def cosine_similarity(a, b):
    """두 embedding vector의 cosine similarity를 계산한다."""

    dot_product = sum(
        x * y
        for x, y in zip(a, b)
    )

    norm_a = math.sqrt(
        sum(x * x for x in a)
    )

    norm_b = math.sqrt(
        sum(x * x for x in b)
    )

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)


def build_knowledge_index():
    """
    knowledge 폴더의 문서를 읽고
    chunk + embedding 형태의 검색 인덱스를 만든다.
    """

    documents = load_documents()

    index = []

    for document in documents:

        chunks = chunk_text(
            document["content"]
        )

        for chunk_id, chunk in enumerate(chunks):

            embedding = create_embedding(chunk)

            index.append({
                "filename": document["filename"],
                "chunk_id": chunk_id,
                "content": chunk,
                "embedding": embedding,
            })

    return index


@function_tool
def search_knowledge(query: str) -> str:
    """
    Search infrastructure troubleshooting knowledge.

    Use this tool when technical knowledge about VMware,
    NSX-T, Linux networking, firewall, NAT, routing,
    or troubleshooting methodology is needed.

    Args:
        query: Technical question to search for.
    """

    index = build_knowledge_index()

    if not index:
        return "No knowledge documents were found."

    query_embedding = create_embedding(query)

    results = []

    for item in index:

        score = cosine_similarity(
            query_embedding,
            item["embedding"],
        )

        results.append({
            "filename": item["filename"],
            "chunk_id": item["chunk_id"],
            "content": item["content"],
            "score": score,
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True,
    )

    top_results = results[:3]

    output = []

    for result in top_results:

        output.append(
            f"""
[Source]
{result["filename"]}

[Chunk]
{result["chunk_id"]}

[Similarity]
{result["score"]:.3f}

[Content]
{result["content"]}
"""
        )

    return "\n".join(output)