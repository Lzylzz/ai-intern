import os
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
# from langchain.agents import create_tool_calling_agent, AgentExecutor # Deprecated in newer langchain versions
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import ToolMessage
from my_skills import tools
import os
import sys

# Load environment variables
load_dotenv()

def main():
    # Check for DashScope (Qwen) key first
    dashscope_key = os.getenv("DASHSCOPE_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    
    if dashscope_key and not dashscope_key.startswith("sk-xxxxxxxx"):
        print("Using Qwen (DashScope) API...")
        # Use Qwen via OpenAI compatibility layer
        llm = ChatOpenAI(
            api_key=dashscope_key,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            model="qwen-plus", # Or qwen-max, qwen-turbo
            temperature=0
        )
    elif openai_key and not openai_key.startswith("your_openai_api_key"):
        print("Using OpenAI API...")
        # Initialize the LLM with OpenAI
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    else:
        print("Error: No valid API Key found.")
        print("Please set DASHSCOPE_API_KEY (for Qwen) or OPENAI_API_KEY in the .env file.")
        sys.exit(1)

    # Bind tools to the LLM
    llm_with_tools = llm.bind_tools(tools)

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
            # Simple invocation with tools
            # In newer LangChain, we often use invoke directly with bound tools
            # or use LangGraph for more complex agent behavior.
            # For this simple demo, we'll manually handle the tool calls loop or just show the tool call generation.
            
            # 1. Ask the model
            messages = [
                ("system", "You are a helpful assistant. You have access to several skills. Use them to help the user."),
                ("human", user_input),
            ]
            ai_msg = llm_with_tools.invoke(messages)
            
            # 2. Check if the model wants to call tools
            if ai_msg.tool_calls:
                print(f"Agent decided to call tools: {len(ai_msg.tool_calls)} calls")
                
                # Append the AI's tool-calling message to history
                messages.append(ai_msg)

                for tool_call in ai_msg.tool_calls:
                     selected_tool = {"get_weather": tools[0], "generate_lucky_number": tools[1], "recommend_food": tools[2]}[tool_call["name"]]
                     tool_output = selected_tool.invoke(tool_call["args"])
                     print(f"  - Tool '{tool_call['name']}' returned: {tool_output}")
                     messages.append(ToolMessage(str(tool_output), tool_call_id=tool_call["id"]))
                
                # 3. Get final response
                final_response = llm_with_tools.invoke(messages)
                print(f"Agent: {final_response.content}\n")
            else:
                print(f"Agent: {ai_msg.content}\n")


        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
