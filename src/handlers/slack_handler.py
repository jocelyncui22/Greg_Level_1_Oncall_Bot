from typing import Dict, Any, Optional
from datetime import datetime
import json
from datetime import datetime
from typing import Dict, Any, Optional


class SlackMessage:
    def __init__(self, user: str, text: str, channel: str):
        self.user = user
        self.text = text
        self.channel = channel
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user": self.user,
            "text": self.text,
            "channel": self.channel,
            "timestamp": self.timestamp
        }


class SlackHandler:
    """Simulated Slack handler for receiving and sending messages"""

    def __init__(self):
        self.messages = []

    def receive_message(self, user: str, text: str, channel: str) -> SlackMessage:
        """Simulate receiving a message from Slack"""
        message = SlackMessage(user, text, channel)
        self.messages.append(message)
        return message

    def send_message(self, channel: str, text: str, thread_ts: Optional[str] = None) -> Dict[str, Any]:
        """Simulate sending a message to Slack"""
        response = {
            "channel": channel,
            "text": text,
            "timestamp": datetime.now().isoformat(),
            "thread_ts": thread_ts
        }
        return response

# Example usage
if __name__ == "__main__":
    slack = SlackHandler()
    
    # Simulate receiving a message
    message = slack.receive_message(
        user="U123456",
        text="Can someone help me understand why my Snowflake query is slow?",
        channel="help-data-eng"
    )
    
    # Simulate sending a response
    response = slack.send_message(
        channel="help-data-eng",
        text="I'll look into that query for you!",
        thread_ts=message.timestamp
    )