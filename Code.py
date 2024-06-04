from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def main():
    text_to_translate = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g. 'hindi' for HINDI): ")
    translated_text = translate_text(text_to_translate, target_language)
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()
