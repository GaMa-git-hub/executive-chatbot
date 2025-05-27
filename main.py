def chatbot():
    print("👋 Hello, I’m your Executive Assistant Chatbot.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "quit", "bye"]:
            print("👋 Goodbye! Have a productive day.")
            break

        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"🕒 Current Time: {now}")

        else:
            print("🤖 I’m still learning. Try another command.")

if __name__ == "__main__":
    chatbot()
