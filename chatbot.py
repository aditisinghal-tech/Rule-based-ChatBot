import datetime as dt

BOT_NAME = "ChatBot"
CREATOR = "Aditi Singhal"
EXIT_COMMANDS = ["bye", "exit", "quit"]

def greet():
    return "🤖ChatBot: Hello there! How can i assist you today?"

def ask_wellbeing():
    return "🤖ChatBot: I'm just a program, but I'm running perfectly fine!"

def get_name():
    return f"🤖ChatBot: I'm your friendly {BOT_NAME}, created by {CREATOR}."

def about_python():
    return "🤖ChatBot: Python is a versatile programming language loved for its simplicity and power."

def get_time():
    return f"🤖ChatBot: The current time is {dt.datetime.now().strftime('%H:%M:%S')}."

def get_date():
    return f"🤖ChatBot: Today's date is {dt.datetime.now().strftime('%Y-%m-%d')}."

def tell_joke():
    return "🤖ChatBot: Why do programmers prefer dark mode? Because light attracts bugs🐛!😂"

def weather_info():
    return "🤖ChatBot: I can't fetch live weather yet, but I hope it's nice where you are!"

def fun_fact():
    return "🤖ChatBot: Did you know? The first computer bug was an actual moth stuck in a computer."

def help_menu():
    return """🤖ChatBot: Here are some things you can ask me:
    - hello / hi
    - how are you
    - your name
    - about python
    - time / date
    - tell me a joke
    - weather
    - fun fact
    - help
    - bye / exit / quit
    """

def unknown():
    return "🤖ChatBot: Sorry, I don't understand that yet. Type 'help' to see what I can do."

# Dictionary mapping keywords to functions
COMMANDS = {
    "hello": greet,
    "hi": greet,
    "how are you": ask_wellbeing,
    "your name": get_name,
    "python": about_python,
    "time": get_time,
    "date": get_date,
    "joke": tell_joke,
    "weather": weather_info,
    "fact": fun_fact,
    "help": help_menu
}

def chatbot():
    print(f"🤖ChatBot: Hello! Type 'help' to see what can i do or 'bye' to exit.")
    print("-"*68)

    while True:
        user_input = input("You: ").strip().lower()

        # Exit condition
        if user_input in EXIT_COMMANDS:
            print("🤖ChatBot: Goodbye! Have a great day.😊")
            break

        # Find matching command
        response_found = False
        for keyword, action in COMMANDS.items():
            if keyword in user_input:
                print(action())
                response_found = True
                break

        if not response_found:
            print(unknown())

chatbot()