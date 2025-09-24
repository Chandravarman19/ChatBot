#CHATBOT
def chatbot():
    print("Chatbot: Hi, I am your chatbot ! Type 'bye' to exit. \n")
    while True:
        user_input = input("You:").lower().strip()
        #Exit Condition\
        if user_input == "bye":
            print("Chatbot:Goodbye! Have a great day")
            break
        elif "hi" in user_input or "hello" in user_input:
            print("Chatbot:Hello there! How can i help You")

        elif "How are you" in user_input:
            print("Chatbot: I am just code ! But i'm doing great")
        elif "name" in user_input:
            print("Chatbot: I'm Robo, your Python basic chatbot assistant")
        elif "weather" in user_input:
            print("Chatbot: I can't fetch live weather ! But  I think its sunny")
        elif "joke" in user_input:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything !")
        else:
            print("Chatbot: Sorry, I didn't understand that. can you try again?")

chatbot()