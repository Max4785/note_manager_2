import re

# Создаём список 
notes = []

print("Добро пожаловать в \"Менеджер заметок\"! Вы можете добавить новую заметку.")

while True:
    user_input = ""

    # Если в user_input нет данных, заходим в цикл, появляются, выходим из него
    while not user_input:
        user_input = input("Введите имя пользователя: ").strip()
    name = user_input

    user_input = ""
    while not user_input:
        user_input = input("Введите заголовок заметки: ").strip()
    title = user_input

    user_input = ""
    while not user_input:
        user_input = input("Введите описание заметки: ").strip()
    description = user_input

    status = ""
    while status not in ["новая", "в процессе", "выполнено"]:
        status = input("Введите статус заметки (новая, в процессе, выполнено): ").strip().lower()
        if status not in ["новая", "в процессе", "выполнено"]:
            print("Ошибка! Введите корректный статус.")

    creation_date = ""
    while not re.match(r"\d{1,2}-\d{1,2}-\d{4}", дата_создания):
        дата_создания = input("Введите дату создания (день-месяц-год): ").strip()
        if not re.match(r"\d{1,2}-\d{1,2}-\d{4}", дата_создания):
            print("Ошибка! Введите дату в формате день-месяц-год.")

    deadline = ""
    while not re.match(r"\d{1,2}-\d{1,2}-\d{4}", дедлайн):
        deadline = input("Введите дедлайн (день-месяц-год): ").strip()
        if not re.match(r"\d{1,2}-\d{1,2}-\d{4}", дедлайн):
            print("Ошибка! Введите дату в формате день-месяц-год.")

    note = {
        "Имя": name,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": creation_date,
        "Дедлайн": deadline
    }

    notes.append(note)

    add_note = ""
    while add_note not in ["да", "нет"]:
        add_note = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
        if add_note not in ["да", "нет"]:
            print("Ошибка! Введите 'да' или 'нет'.")
    if add_note == "нет":
        break

print("\nСписок заметок:")
for i, note in enumerate(notes, 1):
    print(
        f"\n{i}. Имя: {note['name']}\n"
        f"Заголовок: {note['title']}\n"
        f"Описание: {note['description']}\n"
        f"Статус: {note['status']}\n"
        f"Дата создания: {note['creation_date']}\n"
        f"Дедлайн: {note['deadline']}"
    )
