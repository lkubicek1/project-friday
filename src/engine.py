import os
import argparse
import yaml
import requests
from google import genai
from google.genai import types
from datetime import datetime
import time
import sys
from dotenv import load_dotenv

# --- HELPER FUNCTIONS ---

def load_config(report_id):
    # Get the directory where THIS script lives (src/), then go up one level to project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", "reports.yaml")
    
    try:
        with open(config_path, "r") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ Critical Error: Config file not found at {config_path}")
        sys.exit(1)
    
    if report_id not in data["reports"]:
        raise ValueError(f"Report ID '{report_id}' not found in {config_path}")
    
    return data["reports"][report_id]

def send_discord(content, token, channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {"Authorization": f"Bot {token}", "Content-Type": "application/json"}
    
    # Discord 2000 char limit handling (safe buffer 1900)
    CHUNK_SIZE = 1900
    
    if not content:
        print("⚠️ Warning: Content was empty. Skipping Discord send.")
        return

    lines = content.split('\n')
    current_chunk = ""
    
    for line in lines:
        # If adding the next line exceeds chunk size, send current chunk
        if len(current_chunk) + len(line) + 1 > CHUNK_SIZE:
            response = requests.post(url, json={"content": current_chunk}, headers=headers)
            if response.status_code != 200:
                print(f"❌ Discord Error ({response.status_code}): {response.text}")
            
            current_chunk = ""
            time.sleep(1) # Rate limit protection

        current_chunk += line + "\n"
    
    # Send the final chunk
    if current_chunk.strip():
        response = requests.post(url, json={"content": current_chunk}, headers=headers)
        if response.status_code != 200:
            print(f"❌ Discord Error ({response.status_code}): {response.text}")

# --- MAIN EXECUTION ---

def main():
    # Load environment variables from .env file (if it exists)
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--report_id", required=True)
    args = parser.parse_args()

    # 1. Load Config
    try:
        config = load_config(args.report_id)
    except Exception as e:
        print(f"❌ Configuration Error: {e}")
        sys.exit(1)
    
    # 2. Load Secrets
    api_key = os.environ.get("GEMINI_API_KEY")
    discord_token = os.environ.get("DISCORD_TOKEN")
    
    # Dynamic Channel Selection
    channel_env_var = config.get("channel_env_var", "DISCORD_CHANNEL_GENERAL")
    channel_id = os.environ.get(channel_env_var)

    if not all([api_key, discord_token, channel_id]):
        print(f"❌ Missing Secrets! Checked for API_KEY, TOKEN, and {channel_env_var}")
        sys.exit(1)

    # 3. Initialize F.R.I.D.A.Y.
    client = genai.Client(api_key=api_key)
    
    # Google Search grounding configuration
    grounding_tool = types.Tool(
        google_search=types.GoogleSearch()
    )
    
    generation_config = types.GenerateContentConfig(
        tools=[grounding_tool],
        system_instruction=config.get('system_instruction', "You are a helpful AI assistant.")
    )

    # 4. Execute Generation
    print(f"--- F.R.I.D.A.Y. initializing: {config['display_name']} ---")
    today = datetime.now().strftime("%B %d, %Y")
    prompt = config['prompt_template'].format(date=today)
    
    report_text = ""
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=generation_config,
        )
        # Check if response was blocked by safety filters
        if not response.candidates:
             report_text = "⚠️ **Safety Alert:** The protocol was blocked by safety filters. No data retrieved."
             print("Safety Filter Triggered.")
        else:
             report_text = response.text

    except ValueError:
        # This catches the specific "Response was blocked" error from the SDK
        report_text = "⚠️ **Safety Alert:** The model refused to generate this report due to safety guidelines."
    except Exception as e:
        report_text = f"⚠️ **System Malfunction:** {str(e)}"
        print(f"GenAI Error: {e}")

    # 5. Delivery
    header = f"**{config['display_name']} • {today}**"
    
    # Send Header
    send_discord(header, discord_token, channel_id)
    # Send Report
    send_discord(report_text, discord_token, channel_id)
    
    print("✅ Report transmitted successfully.")

if __name__ == "__main__":
    main()
