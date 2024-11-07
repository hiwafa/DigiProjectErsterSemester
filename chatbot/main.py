from utils import format_message
from responses import get_welcome_message, get_opening_question, handle_input


def main():
    print(format_message("Chatbot", get_welcome_message()))
    print(format_message("Chatbot", get_opening_question()))

    while True:
        user_input = input(format_message("Benutzer", "")).strip()
        response = handle_input(user_input)

        if response is None:
            print(format_message("Chatbot", "Tschüss!"))
            break
        print(format_message("Chatbot", response))


if __name__ == "__main__":
    main()
