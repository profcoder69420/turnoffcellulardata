import os
import sys
import time
import json
from datetime import datetime, timezone
import requests

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
if not WEBHOOK_URL:
    print("ERROR: DISCORD_WEBHOOK_URL environment variable is not set.", file=sys.stderr)
    sys.exit(1)

# Customize message via env var or fallback
CUSTOM_MESSAGE = os.environ.get("Always turn off cellular data when you're not using it!")
timestamp = datetime.now(timezone.utc).astimezone().isoformat()
payload = {
    "content":  "This is an hourly reminder. If you don't want future messages, consider muting the channel"
}

# Basic retry with exponential backoff
max_attempts = 3
backoff_base = 2  # seconds

for attempt in range(1, max_attempts + 1):
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        if 200 <= response.status_code < 300:
            print(f"Successfully sent message at {timestamp}")
            sys.exit(0)
        else:
            print(f"Attempt {attempt}: Received HTTP {response.status_code} response. Body: {response.text}", file=sys.stderr)
    except requests.RequestException as e:
        print(f"Attempt {attempt}: Request failed: {e}", file=sys.stderr)

    if attempt < max_attempts:
        sleep_time = backoff_base ** attempt
        print(f"Sleeping {sleep_time} seconds before retry...", file=sys.stderr)
        time.sleep(sleep_time)

print("Failed to send webhook after retries.", file=sys.stderr)
sys.exit(1)
