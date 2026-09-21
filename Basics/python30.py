while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Bye 👋")
        break

    elif "hi" in user or "hello" in user:
        print("Bot: Hello! How can I help you?")

    elif "who are you" in user:
        print("Bot: I am your Python chatbot ")

    elif "how are you" in user:
        print("Bot: I'm good! What about you?")

    elif "im going to study" in user or "exam is coming" in user:
        print("Bot: Study well and don't stress too much!")

    elif "is python hard" in user:
        print("Bot: Python is easy, just practice daily ")

    elif "bye" in user:
        print("Bot: Goodbye! ")
        break
    else:
        print("Bot: I don't understand that yet ")