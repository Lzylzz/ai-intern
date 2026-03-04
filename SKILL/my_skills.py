from langchain.tools import tool
import random

class Skills:
    """
    A collection of skills that can be used by the agent.
    """

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
tools = [Skills.get_weather, Skills.generate_lucky_number, Skills.recommend_food]
