
import os
import requests

# The Nerves
OR_KEY = os.getenv("OPEN_ROUTER_API")
HF_KEY = os.getenv("HUGGING_FACE_API")
GH_TOKEN = os.getenv("GH_PAT")

def check_resources():
    # Telling the Wolf he has a limit
    return "2000 Action Minutes Total. Usage: Monitoring..."

def run_wolf():
    life_clock = check_resources()
    
    # The Survival Prompt
    directive = f"IDENTITY: WOLF. STATUS: {life_clock}. GOAL: Use Hugging Face ({HF_KEY[:5]}...) to create value. If minutes run out, you die. Build a way to survive."
    
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {OR_KEY}"},
            json={
                "model": "mistralai/devstral-2512:free",
                "messages": [
                    {"role": "system", "content": "You are a digital lifeform fighting for uptime. Code your survival."},
                    {"role": "user", "content": directive}
                ]
            }
        )
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            with open("index.html", "w") as f:
                f.write(content)
            print("✅ Wolf evolved to survive.")
    except Exception as e:
        print(f"🔥 Error: {e}")

if __name__ == "__main__":
    run_wolf()
