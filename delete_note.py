notes = [
    {"name": "Алексей", "title": "Список покупок", "description": "Купить продукты на неделю"},
    {"name": "Мария", "title": "Учеба", "description": "Подготовиться к экзамену"}
]

while True:
    if not notes:
        print("\nСписок заметок пуст.\n")
    else:
        print("\nТекущие заметки:")
        for i, note in enumerate(notes, 1):
            print(f"\n{i}. Имя: {note['name']}\n   Заголовок: {note['title']}\n   Описание: {note['description']}")

    user_input = input("\nВведите имя пользователя или заголовок для удаления заметки (для завершения 'выход'): ").strip()

    if user_input.lower() == 'выход':
        print("\nВыход из программы.")
        break

    if not user_input:
        print("\nОшибка: Пустой ввод. Попробуйте снова.")
        continue

    user_input_lower = user_input.lower()
    initial_count = len(notes)
    notes = [note for note in notes if note['name'].lower() != user_input_lower and note['title'].lower() != user_input_lower]

    if len(notes) < initial_count:
        print("\nУспешно удалено.")
    else:
        print("\nЗаметок с таким именем пользователя или заголовком не найдено.")