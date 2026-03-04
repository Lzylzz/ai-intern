import os
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from my_skills import tools

# Load environment variables
load_dotenv()

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("Error: OPENAI_API_KEY is not set. Please set it in the .env file.")
        sys.exit(1)

    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. You have access to several skills. "
                   "Use them to help the user. If you need to use multiple skills, you can do so."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    # Create the agent
    agent = create_tool_calling_agent(llm, tools, prompt)

    # Create the agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    print("Agent is ready! You can ask questions like:")
    print("- 'What's the weather in Shanghai?'")
    print("- 'I'm feeling happy, what should I eat?'")
    print("- 'Give me a lucky number for Alice.'")
    print("- 'What's the weather in Tokyo and what should I eat if I'm sad?' (Complex workflow)")
    print("\nType 'exit' to quit.\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        try:
            response = agent_executor.invoke({"input": user_input})
            print(f"Agent: {response['output']}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
