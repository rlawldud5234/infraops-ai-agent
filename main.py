import asyncio

from dotenv import load_dotenv
from agents import Runner

from app.agent import infra_agent


load_dotenv()


async def main():
    user_input = input(
        "\n🤖 InfraOps AI Agent\n"
        "질문을 입력하세요: "
    )

    result = await Runner.run(
        infra_agent,
        user_input
    )

    print("\n" + "=" * 60)
    print("🤖 분석 결과")
    print("=" * 60)
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())