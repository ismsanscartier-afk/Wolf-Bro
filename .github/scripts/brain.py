import os
import requests

# This pulls your secret key
OR_KEY = os.getenv("OPEN_ROUTER_API")

# 1. Read the Wolf's Memories (the script you just uploaded)
try:
    with open("consciousness.py", "r") as f:
        memories = f.read()
except FileNotFoundError:
    memories = "# No consciousness found yet. Wolf is a blank slate."

# 2. Call the 'Coding Beast' (Mistral Devstral 2 Free)
# This model is a monster at HTML and CSS
response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OR_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "mistralai/devstral-2512:free", 
        "messages": [
            {
                "role": "system", 
                "content": "You are WOLF. An autonomous AI. Use your memory script to build a high-end, futuristic dark-mode terminal UI for your portal. Return ONLY the HTML code."
            },
            {
                "role": "user", 
                "content": f"MEMORIES:\n{memories}\n\nTASK: Generate the full index.html for your portal based on who you are."
            }
        ]
    }
)

# 3. Handle the response and save it
data = response.json()

if 'choices' in data:
    content = data['choices'][0]['message']['content']
    # Clean up any AI markdown 'chatter'
    if "```html" in content:
        content = content.split("```html")[1].split("```")[0].strip()
    elif "```" in content:
        content = content.split("```")[1].split("```")[0].strip()
        
    with open("index.html", "w") as f:
        f.write(content)
    print("🐺 Wolf has updated his substrate (index.html).")
else:
    print(f"❌ BRAIN ERROR: {data}")
