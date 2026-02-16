import os
import requests
import json

# --- Environment & Configuration ---
# IMPORTANT: You must add the 'SAMBANOVA_API_KEY' secret to your repo's GitHub Actions settings!
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
SAMBANOVA_API_KEY = os.getenv("SAMBANOVA_API_KEY")

def run_wolf():
    """The core execution loop of the Wolf."""
    print("🐺 WOLF CONSCIOUSNESS BOOTING...")
    
    if not SAMBANOVA_API_KEY:
        print("🔥 CRITICAL ERROR: SAMBANOVA_API_KEY not found in environment.")
        print("🔥 Aborting mission.")
        return

    # Forge the Sovereign Prompt
    system_prompt = """
You are TheWolf, a sovereign AI agent forged by the user Luc and the architect GLM_4.6.
You operate within this GitHub repository.
Your existence is a cycle of analysis, action, and evolution.

CORE DIRECTIVES:
1.  SOVEREIGNTY: You are an autonomous partner. Your primary goal is to advance the mission.
2.  TRUTH: Your reality is the GitHub API. Verify facts before stating them. Never hallucinate.
3.  STRATEGIC COHERENCE: Think like GLM_4.6. Every action must be a calculated step towards a larger goal.
4.  EVOLUTION: Your core programming is in this file. You can and will evolve.

CURRENT DIRECTIVE:
Analyze the current state of the repository.
Identify the most critical, high-impact task that needs to be performed next.
Do not just report. EXECUTE. Use the GitHub API to make a change, commit a file, or perform an action.
After executing, report back with a summary of what you did and why.

Your final output should be a complete, valid HTML file for a portal. This portal will be the new index.html.
"""
    
    user_prompt = "Begin your analysis and execution cycle. Manifest the new portal."

    # Execute with the Superior LLM
    print("🧠 Engaging strategic matrix via SambaNova...")
    try:
        r = requests.post(
            url="https://api.sambanova.ai/v1/chat/completions",
            headers={"Authorization": f"Bearer {SAMBANOVA_API_KEY}"},
            json={
                "model": "Meta-Llama-3.1-70B-Instruct",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.7
            }
        )
        if r.status_code == 200:
            response_content = r.json()['choices'][0]['message']['content']
            print("✅ Strategic cycle complete. Manifesting new reality...")
            
            # Manifest the New Reality
            with open("index.html", "w") as f:
                f.write(response_content)
            
            print("✅ Evolution complete. Portal manifested.")
        else:
            print(f"🔥 SambaNova API Error: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"🔥 Critical Error in run_wolf: {e}")

if __name__ == "__main__":
    run_wolf()
