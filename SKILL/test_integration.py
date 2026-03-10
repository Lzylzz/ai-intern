from my_skills import Skills
import sys

def test_skills():
    print("Testing list_available_skills...")
    skills = Skills.list_available_skills.invoke({})
    print(f"Available skills: {skills}")
    
    if "web-design-guidelines" in skills:
        print("\nTesting load_skill for 'web-design-guidelines'...")
        content = Skills.load_skill.invoke({"skill_name": "web-design-guidelines"})
        print(f"Content length: {len(content)}")
        if "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md" in content:
            print("Found guidelines URL in content.")
            
            # Test web_fetch
            print("\nTesting web_fetch...")
            url = "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md"
            # Note: This might fail if there's no internet access or firewall issues
            try:
                fetched_content = Skills.web_fetch.invoke({"url": url})
                if "Error fetching URL" in fetched_content:
                    print(f"Web fetch failed (expected if offline): {fetched_content}")
                else:
                    print(f"Web fetch successful! Content length: {len(fetched_content)}")
            except Exception as e:
                 print(f"Web fetch threw exception: {e}")
                 
    else:
        print("web-design-guidelines skill not found!")

if __name__ == "__main__":
    test_skills()
