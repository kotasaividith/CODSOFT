import random

memory = {}
responsesAI = {
    "greetings": ["Hello!", "Hi there!", "Hey!", "Hey, how's it going?"],
    "farewells": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "acknowledgments": ["Great! Let me know if there's anything else I can help with."],
    "thankYous": ["You're welcome! If you have any further questions or need assistance, feel free to ask."],
    "questions": ["I'm doing well, thank you!", "I'm good, thanks for asking.", "All good!"],
    "defaultResponses": [
        "Sorry, I didn't catch that. Could you please repeat?",
        "I'm not sure I understand. Could you provide more details?",
        "Hmm, I'm having trouble understanding. Can you rephrase that?",
        "Apologies, could you clarify what you mean?",
        "It seems I'm not following. Could you explain again?",
    ]
}

responsesUserInput = {
    "greetings": ["hi", "hello", "hey", "good morning"],
    "farewells": ["bye", "quit"],
    "thankYous": ["thanks", "thank you so much", "you are great", "that's working"],
    "acknowledgments": ["ok"],
    "questions": ["how are you?"],
    "commands": ["greet", "farewell", "ask", "repeat", "memory", "forget", "clear"]
}

def generateResponse(userInput):
    userInputLower = userInput.lower()
    if userInputLower in memory:
        return memory[userInputLower]
    if userInputLower in responsesUserInput["greetings"]:
        response = random.choice(responsesAI["greetings"])
    elif userInputLower in responsesUserInput["farewells"]:
        response = random.choice(responsesAI["farewells"])
    elif userInputLower in responsesUserInput["questions"]:
        response = random.choice(responsesAI["questions"])
    elif userInputLower in responsesUserInput["thankYous"]:
        response = random.choice(responsesAI["thankYous"])
    elif userInputLower in responsesUserInput["acknowledgments"]:
        response = random.choice(responsesAI["acknowledgments"])
    elif "my name is" in userInputLower:
        name = userInputLower.split("my name is")[-1].strip()
        response = f"Nice to meet you, {name}!"
        memory["userName"] = name
    elif "what is my name" in userInputLower:
        if "userName" in memory:
            response = f"Your name is {memory['userName']}."
        else:
            response = "I don't know your name yet."
    else:
        response = random.choice(responsesAI["defaultResponses"])
    memory[userInputLower] = response
    return response

def startChat():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        userInput = input("You: ")
        response = generateResponse(userInput)
        print("Chatbot:", response)
        if userInput.lower() in responsesUserInput["farewells"]:
            break

startChat()
