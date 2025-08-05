# Hourly Discord Webhook Bot

## Purpose
Sends a message to a specific Discord channel once every hour using GitHub Actions and a Discord webhook.

## Setup

1. Create a Discord webhook for the target channel.
2. Add the webhook URL as a secret in GitHub repository settings:
   - Name: `DISCORD_WEBHOOK_URL`
3. (Optional) Customize the message by setting the `MESSAGE` environment variable in the workflow.
4. Commit `send_webhook.py` and the workflow file; GitHub Actions will trigger hourly.

## Security
- Webhook URL is stored in GitHub Secrets and not committed to source control.
- Logs do not expose the webhook URL.
