from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("✅ API Key가 정상적으로 읽혔습니다.")
    print("Key 앞부분:", api_key[:7] + "...")
else:
    print("❌ API Key를 찾을 수 없습니다.")