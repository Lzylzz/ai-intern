# Skills Demo with LangChain (Qwen / OpenAI)

This project demonstrates how to use "skills" (implemented as tools) with an LLM agent that autonomously chooses which skill to use to complete a workflow.

It supports **Alibaba Cloud Qwen (DashScope)** and **OpenAI**.

## Prerequisites

- Python 3.9+
- Qwen (DashScope) API Key OR OpenAI API Key

## Setup

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Configure your API Key:
    - Rename `.env.example` to `.env`.
    - Edit `.env` and fill in your API key:
        - **For Qwen**: Fill in `DASHSCOPE_API_KEY`. Get it from [Aliyun DashScope Console](https://dashscope.console.aliyun.com/apiKey).
        - **For OpenAI**: Fill in `OPENAI_API_KEY`.
    
    The code prioritizes `DASHSCOPE_API_KEY` if both are present.

## Running the Demo

Run the main script:

```bash
python main.py
```

## How it works

-   **`my_skills.py`**: Contains the `Skills` class with 3 static methods decorated as tools (`@tool`). These represent the "skills" or interfaces the model can use.
    -   `get_weather(city)`: Returns weather info.
    -   `generate_lucky_number(user_name)`: Returns a lucky number.
    -   `recommend_food(mood)`: Recommends food based on mood.

-   **`main.py`**: Initializes a LangChain agent with `ChatOpenAI` (compatible with Qwen) and the tools from `my_skills.py`.
    -   The agent receives user input.
    -   It autonomously decides which tool(s) to call based on the input.
    -   It executes the tool(s) and returns the final response.

## Example Interactions

-   **Single Skill**: "What's the weather in Beijing?" (Uses `get_weather`)
-   **Workflow**: "I'm feeling sad, what should I eat? Also, what's my lucky number? I'm Bob." (Uses `recommend_food` and `generate_lucky_number`)
