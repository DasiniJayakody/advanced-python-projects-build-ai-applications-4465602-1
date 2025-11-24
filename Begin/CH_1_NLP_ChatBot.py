from textblob import TextBlob
import sys

# Try to import tkinter for GUI fallback when input() is not available
try:
    import tkinter as tk
    from tkinter import simpledialog

    TK_AVAILABLE = True
except Exception:
    TK_AVAILABLE = False

# Define intents and their corresponding responses based on keywords
intents = {
    "hours": {
        "keywords": ["hours", "open", "close", "time"],
        "response": "Our working hours are from 9 AM to 5 PM, Monday to Friday.",
    },
    "return": {
        "keywords": ["return", "refund", "exchange"],
        "response": "You can return any item within 30 days of purchase with a receipt.",
    },
}


def get_response(message):
    # Convert the message to lowercase for consistent keyword matching
    message_lower = message.lower()
    # Check if the message contains any keywords associated with defined intents
    for intent_name, intent_data in intents.items():
        if any(word in message_lower for word in intent_data["keywords"]):
            return intent_data["response"]

    # Analyze the sentiment of the message using TextBlob
    sentiment = TextBlob(message).sentiment.polarity

    # Return a response based on the sentiment score
    if sentiment > 0:
        return "That's so great to hear!"
    elif sentiment < 0:
        return "I'm sorry to hear that. How can I assist you further?"
    else:
        return "I see. Could you please provide more details?"


# New helper: safe_input uses terminal input when available, otherwise falls back to a tkinter dialog
def safe_input(prompt):
    if sys.stdin is not None and sys.stdin.isatty():
        try:
            return input(prompt)
        except EOFError:
            raise
    if TK_AVAILABLE:
        root = tk.Tk()
        root.withdraw()
        try:
            answer = simpledialog.askstring("Chat Input", prompt)
        finally:
            root.destroy()
        if answer is None:
            raise EOFError
        return answer
    print(
        "No interactive input available. Run this script in a terminal or use a GUI-enabled environment."
    )
    raise EOFError


def chat():
    # Greet the user and prompt for input
    print("Hello! I'm your customer service chatbot. How can I assist you today?")
    # Continuously prompt the user for input until they choose to exit
    while True:
        try:
            user_message = safe_input("You: ").strip()
        except EOFError:
            break

        if user_message.lower() in ["exit", "quit", "bye"]:
            break

        print(f"\nChatBot: {get_response(user_message)}")
    # Thank the user for chatting when they exit
    print("ChatBot: Thank you for chatting with us. Have a great day!")


if __name__ == "__main__":
    chat()  # Start the chat when the script is executed
