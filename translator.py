from googletrans import Translator
import csv
import os

translator = Translator()

def translate_text(text, dest_language="uk"):
    """Перекладає текст на вказану мову"""
    try:
        return translator.translate(text, dest=dest_language).text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def translate_file(input_file, output_file, dest_language="uk"):
    """Перекладає вміст .txt або .csv файлу"""
    if input_file.endswith(".txt"):
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
        translated_text = translate_text(text, dest_language)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(translated_text)
    elif input_file.endswith(".csv"):
        with open(input_file, "r", encoding="utf-8") as f, open(output_file, "w", encoding="utf-8", newline="") as out_f:
            reader = csv.reader(f)
            writer = csv.writer(out_f)
            for row in reader:
                translated_row = [translate_text(cell, dest_language) for cell in row]
                writer.writerow(translated_row)
    print(f"✅ Файл збережено як {output_file}")

if __name__ == "__main__":
    choice = input("🔠 Введіть текст або шлях до файлу для перекладу: ").strip()
    lang = input("🌍 Введіть мову перекладу (наприклад, 'uk' для української): ").strip()

    if os.path.isfile(choice):
        output_file = f"translated_{os.path.basename(choice)}"
        translate_file(choice, output_file, lang)
    else:
        print(f"🎯 Переклад: {translate_text(choice, lang)}")
