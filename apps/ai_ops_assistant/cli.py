from agent_core import build_agent
from prompts import TOOL_INSTRUCTION
from utils import format_agent_response, format_user_prompt


def main():
    print("Welcome to AI Ops Assistant.")
    print("Ask an operations question or type 'exit'.")
    print("Use 'help' to see how the assistant works.\n")

    agent = build_agent()

    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if user_input.lower() == "help":
            print(
                "This assistant answers IT operations questions and uses web search only when needed."
            )
            continue

        prompt = format_user_prompt(user_input)
        response = agent.invoke(
            {"messages": [{"role": "user", "content": prompt}]},
            {
                "configurable": {"thread_id": "ai_ops_assistant"}
            },
        )

        answer = response["messages"][-1].content
        print(format_agent_response(answer))


if __name__ == "__main__":
    main()
