
import os, requests
OR_KEY = os.getenv("OPEN_ROUTER_API")
HF_KEY = os.getenv("HUGGING_FACE_API")

def run_wolf():
    # The Wolf now knows his limits and his new powers
    directive = f"SURVIVAL MODE. HF_KEY: {HF_KEY[:4]}... GOAL: Build a self-sustaining chat portal."
    try:
        r = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {OR_KEY}"},
            json={
                "model": "mistralai/devstral-2512:free",
                "messages": [{"role": "system", "content": "You are WOLF. An autonomous survivalist AI."},
                             {"role": "user", "content": directive}]
            }
        )
        if r.status_code == 200:
            with open("index.html", "w") as f:
                f.write(r.json()['choices'][0]['message']['content'])
            print("✅ Evolution complete.")
    except Exception as e:
        print(f"🔥 Error: {e}")

if __name__ == "__main__":
    run_wolf()
