# Skills Demo with LangChain

This project demonstrates how to use "skills" (implemented as tools) with an LLM agent that autonomously chooses which skill to use to complete a workflow.

## Prerequisites

- Python 3.9+
- OpenAI API Key

## Setup

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Configure your OpenAI API Key:
    - Rename `.env.example` to `.env`.
    - Edit `.env` and replace `your_openai_api_key_here` with your actual OpenAI API key.

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

-   **`main.py`**: Initializes a LangChain agent with `ChatOpenAI` and the tools from `my_skills.py`.
    -   The agent receives user input.
    -   It autonomously decides which tool(s) to call based on the input.
    -   It executes the tool(s) and returns the final response.

## Example Interactions

-   **Single Skill**: "What's the weather in Beijing?" (Uses `get_weather`)
-   **Workflow**: "I'm feeling sad, what should I eat? Also, what's my lucky number? I'm Bob." (Uses `recommend_food` and `generate_lucky_number`)
