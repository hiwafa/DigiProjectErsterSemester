def get_welcome_message():
    return "Hallo!"

def get_opening_question():
    return "Wie kann ich Ihnen behilflich sein?"


predefined_answers = {
    "Wie heißen Sie?": "Ich bin Chatbot.",
    "Wie funktioniert diese App?": "Geben Sie Ihre Frage ein und ich werde versuchen, sie zu beantworten."
}


def handle_input(user_input):
    if user_input.lower() == "Tschüss":
        return None  # Das Gespräch zu Ende zu bringen
    elif user_input in predefined_answers:
        return predefined_answers[user_input]
    # return f"Sie habe gesagt: {user_input}"
    else:
        return "Es tut mir leid, ich kenne diese Frage nicht. Bitte Stelle Sie eine andere Frage."