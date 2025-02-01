# text_translator
# Автоматичний перекладач тексту

## 📌 Опис
Цей скрипт дозволяє перекладати текст за допомогою Google Translate API. Підтримує як введений текст, так і файли `.txt` або `.csv`.

## 🚀 Функції
- Переклад тексту одним запитом.
- Пакетний переклад `.txt` або `.csv` файлів.
- Можливість вибору мов (наприклад, англійська → українська).

## 📥 Встановлення
Перед використанням необхідно встановити бібліотеку `googletrans`:
```sh
pip install googletrans==4.0.0-rc1
```

## 🚀 Використання
```sh
python translator.py
```
Далі:
1. Введіть текст або шлях до файлу (`.txt` або `.csv`).
2. Виберіть мову перекладу (наприклад, `uk` для української).
3. Отримайте переклад або збережений файл.

## 🔧 Додаткові можливості
- Переклад файлів великим обсягом.
- Підтримка різних мов (`en`, `fr`, `de`, `uk` тощо).
- Можливість розширення через API Google Cloud.

Ліцензія: MIT License
