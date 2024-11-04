
import argparse


def main():

    # Erstellen eines Parsers für Befehlszeilenargumente
    parser = argparse.ArgumentParser(description="Chatbot Command Line Interface")

    # Definieren des Arguments --question
    parser.add_argument('--question', type=str, help='Die Frage, die vom Chatbot verarbeitet werden soll')

    # Argumente verarbeiten
    args = parser.parse_args()

    # Überprüfen, ob das Argument --question vorhanden ist
    if args.question:
        # Wenn eine Frage vorhanden ist, wird sie gespeichert und ausgegeben
        question = args.question
        print(f"Frage erhalten: {question}")
    else:
        # Wenn keine Frage vorhanden ist, wird eine Willkommensnachricht angezeigt
        print("Willkommen beim Chatbot! Bitte geben Sie Ihre Frage ein.")


if __name__ == "__main__":
    main()
