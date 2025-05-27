from datetime import datetime
import webbrowser

def chatbot():
    print("👋 Hello, I’m your Executive Assistant Chatbot.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "quit", "bye"]:
            print("👋 Goodbye! Have a productive day.")
            break

        elif "time" in user_input:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"🕒 Current Time: {now}")

        elif "date" in user_input:
            today = datetime.now().strftime("%A, %B %d, %Y")
            print(f"📅 Today's Date: {today}")

        elif user_input in ["hi", "hello", "hey"]:
            print("👋 Hello! How can I assist you today?")

        else:
            print("🤖 I’m still learning. Try another command.")

if __name__ == "__main__":
    chatbot()
