import tkinter as tk
from datetime import datetime, timedelta
import webbrowser

# 🖥️ GUI Setup (moved to the top so root is accessible in all functions)
root = tk.Tk()
root.title("Executive Assistant Chatbot v1.1")
root.geometry("500x500")

# 🎯 Process user input and return appropriate response
def process_input(user_input):
    user_input = user_input.lower()

    if "hi" in user_input:
        return "👋 Hello! How can I assist you today?"

    elif "time after" in user_input:
        try:
            words = user_input.split()
            index = words.index("after")
            num = int(words[index + 1])
            if "hour" in words[index + 2]:
                future_time = datetime.now() + timedelta(hours=num)
            elif "minute" in words[index + 2]:
                future_time = datetime.now() + timedelta(minutes=num)
            else:
                return "🕒 Please specify time in hours or minutes."
            return f"🕒 Time after {num} {words[index + 2]}: {future_time.strftime('%H:%M:%S')}"
        except:
            return "❗ Couldn't parse the time request."

    elif "time now" in user_input or "current time" in user_input:
        now = datetime.now().strftime("%H:%M:%S")
        return f"🕒 Current Time: {now}"

    elif "date" in user_input and "tomorrow" in user_input:
        tomorrow = datetime.now() + timedelta(days=1)
        return f"📅 Tomorrow's Date: {tomorrow.strftime('%A, %B %d, %Y')}"

    elif "date" in user_input:
        today = datetime.now().strftime("%A, %B %d, %Y")
        return f"📅 Today's Date: {today}"

    elif "how are you" in user_input:
        return "😊 I'm just code, but I'm doing great! How about you?"

    elif "open" in user_input:
        if "google" in user_input:
            webbrowser.open("https://www.google.com")
            return "🌐 Opening Google..."
        elif "youtube" in user_input:
            webbrowser.open("https://www.youtube.com")
            return "🌐 Opening YouTube..."
        elif "github" in user_input:
            webbrowser.open("https://www.github.com")
            return "🌐 Opening GitHub..."
        elif "chatgpt" in user_input:
            webbrowser.open("https://chat.openai.com")
            return "🌐 Opening ChatGPT..."
        else:
            return "🌐 I can open Google, YouTube, GitHub, or ChatGPT for now."

    elif user_input in ["exit", "quit", "bye"]:
        root.after(500, root.quit)  # Delay slightly to allow message to show
        return "👋 Goodbye! Have a great day!"

    else:
        return "🤖 I’m still learning. Try another command."

# 🚀 Function called when user clicks Send
def send():
    user_input = entry_field.get()
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    bot_response = process_input(user_input)
    if bot_response:  # Prevent inserting None
        chat_log.insert(tk.END, bot_response + "\n\n")
    entry_field.delete(0, tk.END)

# 📜 Chat log
chat_log = tk.Text(root, bd=1, bg="white", font=("Arial", 12))
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 🙋 Welcome message
welcome_msg = (
    "👋 Hello! I’m your Executive Assistant.\n"
    "💬 You can ask me:\n"
    "   - What’s the time now?\n"
    "   - What’s today’s date?\n"
    "   - Open YouTube / Google / GitHub\n"
    "   - Exit\n"
    "Type your request below 👇\n\n"
)
chat_log.insert(tk.END, welcome_msg)

# 🖊️ Entry + Send button layout
input_frame = tk.Frame(root)
input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

entry_field = tk.Entry(input_frame, font=("Arial", 12))
entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

send_button = tk.Button(input_frame, text="Send", command=send, width=10)
send_button.pack(side=tk.RIGHT)

# 🌀 Start GUI loop
root.mainloop()
