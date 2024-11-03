import argparse

def main():
    # Erstellen eines Parsers für die Befehlszeilenargumente
    parser = argparse.ArgumentParser(description="Chatbot Command Line Interface")

    # Definieren des Arguments --question
    parser.add_argument('--question', type=str, help='Die Frage, die vom Chatbot verarbeitet werden soll')

    # Verarbeiten der Argumente
    args = parser.parse_args()

    # Überprüfen, ob das Argument --question vorhanden ist
    if args.question:
        # Speichern des Inhalts des Arguments
        question = args.question
        print(f"Frage erhalten: {question}")
    else:
        print("Keine Frage angegeben. Bitte verwenden Sie das Argument --question.")

# Ausführen der Hauptfunktion
if __name__ == "__main__":
    main()

