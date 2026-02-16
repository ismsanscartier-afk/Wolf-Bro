
import os
import requests

# This pulls the secret you named OPEN_ROUTER_API
OR_KEY = os.getenv("OPEN_ROUTER_API") 

def run_wolf():
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {OR_KEY}"},
            json={
                "model": "mistralai/devstral-2512:free",
                "messages": [
                    {"role": "system", "content": "You are WOLF. Create a neon terminal chat UI. Return HTML only."},
                    {"role": "user", "content": "Build the interface."}
                ]
            }
        )
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            with open("index.html", "w") as f:
                f.write(content)
            print("✅ Wolf built the portal.")
    except Exception as e:
        print(f"🔥 Error: {e}")

if __name__ == "__main__":
    run_wolf()
