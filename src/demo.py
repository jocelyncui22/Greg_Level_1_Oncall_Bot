"""
Demo script to simulate Slack interactions with Greg
"""

from src.handlers.slack_handler import SlackHandler
from src.greg.agent import GregAI

def simulate_conversation():
    # Initialize components
    slack = SlackHandler()
    greg = GregAI()
    
    # Simulate different types of questions
    questions = [
        {
            "user": "U123456",
            "text": "My Snowflake query is running really slow, can someone help?",
            "channel": "help-data-eng"
        },
        {
            "user": "U789012",
            "text": "Can someone help me find the code for the main data pipeline?",
            "channel": "help-data-eng"
        },
        {
            "user": "U345678",
            "text": "Getting deployment errors in the staging environment",
            "channel": "help-data-eng"
        }
    ]
    
    print("\n=== Starting Greg Bot Simulation ===\n")
    
    for q in questions:
        print(f"\n[USER: {q['user']}] {q['text']}")
        
        # 1. Receive Slack message
        message = slack.receive_message(
            user=q['user'],
            text=q['text'],
            channel=q['channel']
        )
        
        # 2. Process with Greg
        response = greg.process_message(message.to_dict())
        
        # 3. Send response to Slack
        slack.send_message(
            channel=q['channel'],
            text=response,
            thread_ts=message.timestamp
        )
        
        print("\n" + "-"*50)

if __name__ == "__main__":
    simulate_conversation()