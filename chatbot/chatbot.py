def respond_to_input(message):
    message = message.lower()
    if message == "hello":
        return "hi"
    elif message == "how are you":
        return "i am fine"
    elif message == "bye":
        return "goodbye"
    else:
        return "i didn't understand that"

def chatbot():
    print("🤖 Chatbot: Hello! I can chat with you. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        reply = respond_to_input(user_input)
        print("🤖 Chatbot:", reply)
        if user_input.lower() == "bye":
            break

# Start the chatbot
chatbot()
