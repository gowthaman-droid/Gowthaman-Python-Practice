import random

responses = {
    "greeting": ["Hello ", "Hi there!", "Hey!"],
    "name": ["I am your chatbot ", "Call me PyBot"],
    "how": ["I'm doing great!", "All good "],
    "study": ["Go study ", "Focus! Exams coming "],
    "python": ["Practice daily ", "Build projects "]
}

try:
    f = open("user.txt", "r")
    username = f.read()
    f.close()
except:
    username = input("Enter your name: ")
    f = open("user.txt", "w")
    f.write(username)
    f.close()

print("Bot: Welcome", username)

chat = open("chat.txt", "a")

while True:
    user = input(username + ": ").lower()
    chat.write(username + ": " + user + "\n")

    if user == "exit":
        print("Bot: Bye ")
        chat.write("Bot: Bye\n")
        break

    if "hi" in user or "hello" in user:
        reply = random.choice(responses["greeting"])

    elif "name" in user:
        reply = random.choice(responses["name"])

    elif "how are you" in user:
        reply = random.choice(responses["how"])

    elif "study" in user or "exam" in user:
        reply = random.choice(responses["study"])

    elif "python" in user:
        reply = random.choice(responses["python"])

    else:
        reply = "I don’t understand "

    print("Bot:", reply)
    chat.write("Bot: " + reply + "\n")

chat.close()