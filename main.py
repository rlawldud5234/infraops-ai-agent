import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

agent = Agent(
    name="InfraOps Assistant",
    instructions="""
    You are an infrastructure troubleshooting assistant.
    You have knowledge of VMware, NSX-T, Linux, networking,
    and private cloud infrastructure.

    Answer technical questions clearly and explain:
    1. Possible causes
    2. What to check
    3. Recommended next steps
    """
)

async def main():
    result = await Runner.run(
        agent,
        "VM에서 외부 인터넷 통신이 되지 않습니다. "
        "인프라 엔지니어라면 무엇부터 확인해야 하나요?"
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())