def get_welcome_message():
    return "Hallo!"

def get_opening_question():
    return "Wie kann ich Ihnen behilflich sein?"

def handle_input(user_input):
    if user_input.lower() == "Tschüss":
        return None  # Das Gespräch zu Ende zu bringen
    return f"Sie habe gesagt: {user_input}"