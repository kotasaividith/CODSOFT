import random

# Dictionary to store user-specific information
memory = {}

# Predefined responses for various categories
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
        "I'm still learning! Can you try saying that another way?",
        "It seems I'm not following. Could you explain again?",
        "I'm having trouble processing that. Can you try again?",
        "That's a bit unclear to me. Can you give me more context?",
        "I'm afraid I didn't get that. Can you elaborate?",
        "Sorry, could you please clarify what you're asking?",
        "I'm not quite sure what you mean. Could you explain further?",
        "Hmm, that's not ringing any bells. Can you give me more details?",
        "I'm having trouble processing your request. Can you try again?",
        "It seems like I'm missing something. Could you provide additional information?",
        "Sorry, I'm drawing a blank. Can you give me some more context?",
        "I'm not sure I'm following. Could you break it down for me?",
        "I'm having difficulty understanding your message. Can you simplify it?",
        "I'm struggling to understand. Could you phrase it differently?",
        "It appears I'm not getting your point. Can you try expressing it differently?",
        "Sorry, I'm a bit confused. Can you provide more clarity?"
    ]
}

# Expected user input categories
responsesUserInput = {
    "greetings": ["hi", "hello", "hey", "good morning"],
    "farewells": ["bye", "quit"],
    "thankYous": ["thanks", "thank you so much", "you are great", "that's working"],
    "acknowledgments": ["ok"],
    "questions": ["how are you?"],
    "commands": ["greet", "farewell", "ask", "repeat", "memory", "forget", "clear"]
}

def generateResponse(userInput):
    """
    Generates a response based on user input.
    
    Parameters:
    userInput (str): The input string from the user.

    Returns:
    str: The response generated by the chatbot.
    """
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
    """
    Starts the chatbot interaction with the user.
    """
    print("Chatbot: Hi! How can I help you today?")
    while True:
        userInput = input("You: ")
        response = generateResponse(userInput)
        print("Chatbot:", response)
        if userInput.lower() in responsesUserInput["farewells"]:
            break

# Initiates the chatbot conversation
startChat()
