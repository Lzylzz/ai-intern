from my_skills import tools
from langchain_core.tools import BaseTool

print(f"Type of first tool: {type(tools[0])}")
try:
    print(f"Is instance of BaseTool? {isinstance(tools[0], BaseTool)}")
    print(f"Tool name: {tools[0].name}")
    print("Verification successful.")
except Exception as e:
    print(f"Verification failed: {e}")
