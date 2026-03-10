from langchain.tools import tool
import random
import os
import urllib.request

class Skills:
    """
    A collection of skills that can be used by the agent.
    """

    @staticmethod
    @tool
    def list_available_skills() -> list[str]:
        """
        List all available skills in the skills directory.
        
        Returns:
            list[str]: A list of available skill names.
        """
        skills_dir = os.path.join(os.path.dirname(__file__), "skills")
        if not os.path.exists(skills_dir):
            return []
        
        skills = []
        for name in os.listdir(skills_dir):
            if os.path.isdir(os.path.join(skills_dir, name)) and os.path.exists(os.path.join(skills_dir, name, "SKILL.md")):
                skills.append(name)
        return skills

    @staticmethod
    @tool
    def load_skill(skill_name: str) -> str:
        """
        Load the instructions and content of a specific skill.
        Use this when you need to perform a task related to a specific skill (e.g., "brand-guidelines").
        
        Args:
            skill_name (str): The name of the skill to load (e.g., "brand-guidelines").
            
        Returns:
            str: The content of the skill's instruction file (SKILL.md).
        """
        skills_dir = os.path.join(os.path.dirname(__file__), "skills")
        skill_path = os.path.join(skills_dir, skill_name, "SKILL.md")
        
        if not os.path.exists(skill_path):
            return f"Error: Skill '{skill_name}' not found."
            
        try:
            with open(skill_path, "r", encoding="utf-8") as f:
                content = f.read()
            return content
        except Exception as e:
            return f"Error reading skill file: {e}"

    @staticmethod
    @tool
    def web_fetch(url: str) -> str:
        """
        Fetch content from a URL.
        Use this tool when a skill instruction requires fetching external resources (e.g., guidelines, rules).
        
        Args:
            url (str): The URL to fetch.
            
        Returns:
            str: The content of the URL or an error message.
        """
        try:
            with urllib.request.urlopen(url) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            return f"Error fetching URL: {e}"

    @staticmethod
    @tool
    def read_file(file_path: str) -> str:
        """
        Read the content of a file from the local filesystem.
        Use this tool when you need to analyze code or content in a file.
        
        Args:
            file_path (str): The path to the file to read.
            
        Returns:
            str: The content of the file or an error message.
        """
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' not found."
            
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"

    @staticmethod
    @tool
    def get_weather(city: str) -> str:
        """
        Get the current weather for a specific city.
        
        Args:
            city (str): The name of the city (e.g., "Beijing", "New York").
            
        Returns:
            str: A string describing the weather.
        """
        # Simulate a weather API response
        conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy"]
        temp = random.randint(-5, 35)
        condition = random.choice(conditions)
        return f"The weather in {city} is {condition} with a temperature of {temp}°C."

    @staticmethod
    @tool
    def generate_lucky_number(user_name: str) -> dict:
        """
        Generate a lucky number for a user.
        
        Args:
            user_name (str): The name of the user.
            
        Returns:
            dict: A dictionary containing the user name and their lucky number.
        """
        # Simulate some logic
        lucky_number = random.randint(1, 100)
        return {
            "user": user_name,
            "lucky_number": lucky_number,
            "message": f"Hello {user_name}, your lucky number today is {lucky_number}!"
        }

    @staticmethod
    @tool
    def recommend_food(mood: str) -> str:
        """
        Recommend a food based on the user's mood.
        
        Args:
            mood (str): The mood of the user (e.g., "happy", "sad", "tired").
            
        Returns:
            str: A food recommendation.
        """
        recommendations = {
            "happy": "Ice Cream",
            "sad": "Hot Chocolate",
            "tired": "Coffee",
            "angry": "Spicy Hot Pot",
            "excited": "Pizza"
        }
        return f"Since you are feeling {mood}, I recommend you eat: {recommendations.get(mood.lower(), 'A healthy salad')}."

# List of tools to be exported
tools = [Skills.get_weather, Skills.generate_lucky_number, Skills.recommend_food, Skills.list_available_skills, Skills.load_skill, Skills.web_fetch, Skills.read_file]
