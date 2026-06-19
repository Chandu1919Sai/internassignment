"""
TASK 4: Basic Chatbot — CodeAlpha Python Internship
Goal: A simple rule-based chatbot that responds to user input.
Key Concepts: if-elif, functions, loops, input/output
"""

import random
import time

# ─── Response Rules ───────────────────────────────────────────────────────────
# Each key is a tuple of trigger words/phrases; value is a list of responses
# (one is picked randomly to feel more natural).

RESPONSES = {
    ("hello", "hi", "hey", "hiya", "howdy"): [
        "Hey there! 👋 How can I help you today?",
        "Hello! Great to see you. What's on your mind?",
        "Hi! I'm CodeBot. Ask me anything!",
    ],
    ("how are you", "how are u", "how r you", "you okay", "you good"): [
        "I'm doing great, thanks for asking! 😊 How about you?",
        "All systems running smoothly! How can I assist?",
        "I'm fantastic! Ready to chat. What do you need?",
    ],
    ("what is your name", "who are you", "your name", "what are you"): [
        "I'm CodeBot 🤖 — your friendly Python-powered chatbot!",
        "Call me CodeBot! Built with Python for CodeAlpha internship.",
    ],
    ("bye", "goodbye", "see you", "see ya", "quit", "exit", "cya"): [
        "Goodbye! Have an amazing day! 👋",
        "See you later! Take care! 😊",
        "Bye bye! It was nice chatting with you! 🌟",
    ],
    ("thanks", "thank you", "thx", "ty"): [
        "You're welcome! 😊 Anything else I can help with?",
        "Happy to help! Let me know if you need more!",
        "Anytime! That's what I'm here for! 🤖",
    ],
    ("help", "what can you do", "commands", "features"): [
        "I can chat with you! Try saying:\n"
        "  • hello / hi / hey\n"
        "  • how are you\n"
        "  • what is your name\n"
        "  • tell me a joke\n"
        "  • what time is it\n"
        "  • bye / goodbye",
    ],
    ("joke", "tell me a joke", "funny", "make me laugh"): [
        "Why do programmers prefer dark mode?\n  Because light attracts bugs! 🐛😄",
        "Why did Python break up with Java?\n  Because it had too many classes! 😂",
        "How many programmers does it take to change a light bulb?\n  None — it's a hardware problem! 💡",
        "Why is Python the best language?\n  Because it's written in English, not in tears! 😆",
    ],
    ("time", "what time", "current time"): [
        f"The current time is: {time.strftime('%H:%M:%S')} 🕐",
    ],
    ("date", "what date", "today", "current date"): [
        f"Today's date is: {time.strftime('%A, %d %B %Y')} 📅",
    ],
    ("weather", "how is the weather"): [
        "I can't check live weather, but I hope it's sunny wherever you are! ☀️",
        "I wish I could check outside, but I'm just code! Try a weather app. 🌤️",
    ],
    ("who made you", "who created you", "who built you", "who wrote you"): [
        "I was built by a CodeAlpha Python intern! 🐍💻",
        "A passionate Python developer made me as part of the CodeAlpha internship!",
    ],
    ("python", "do you like python"): [
        "Python is the BEST! 🐍 Clean syntax, powerful libraries — what's not to love?",
        "Oh I love Python! It's literally the language I'm written in! 😄",
    ],
}

# Default replies when nothing matches
DEFAULT_RESPONSES = [
    "Hmm, I'm not sure I understand. Could you rephrase that? 🤔",
    "Interesting! I'm still learning. Try asking something else.",
    "I didn't quite catch that. Type 'help' to see what I can do!",
    "That's a tough one! I'm just a simple bot. 😅 Try 'help'.",
]


# ─── Core Functions ────────────────────────────────────────────────────────────

def normalize(text):
    """Lowercase and strip punctuation for easier matching."""
    return text.lower().strip().rstrip("!?.,'\"")


def get_response(user_input):
    """Find the best matching response for the user's input."""
    normalized = normalize(user_input)

    for triggers, replies in RESPONSES.items():
        for trigger in triggers:
            if trigger in normalized:
                return random.choice(replies)

    return random.choice(DEFAULT_RESPONSES)


def is_farewell(user_input):
    """Check if the user wants to exit."""
    farewells = ("bye", "goodbye", "see you", "see ya", "quit", "exit", "cya")
    normalized = normalize(user_input)
    return any(word in normalized for word in farewells)


def typing_effect(text, delay=0.02):
    """Print text character by character for a typing effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# ─── Main Chatbot Loop ────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 50)
    print("   🤖  CODEBOT — Simple Python Chatbot")
    print("   Built for CodeAlpha Python Internship")
    print("=" * 50)
    typing_effect("  CodeBot: Hello! I'm CodeBot 🤖 Type 'help' for commands.")
    print()

    while True:
        try:
            user_input = input("  You     : ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  CodeBot: Goodbye! 👋\n")
            break

        if not user_input:
            print("  CodeBot: Please say something! I'm listening... 👂")
            continue

        response = get_response(user_input)
        typing_effect(f"  CodeBot: {response}")
        print()

        if is_farewell(user_input):
            break

    print("=" * 50)
    print("  Chat session ended. Come back soon! 🌟")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
