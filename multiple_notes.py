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
    while not re.match(r"\d{1,2}-\d{1,2}-\d{4}", creation_date):
        creation_date = input("Введите дату создания (день-месяц-год): ").strip()
        if not re.match(r"\d{1,2}-\d{1,2}-\d{4}", creation_date):
            print("Ошибка! Введите дату в формате день-месяц-год.")

    deadline = ""
    while not re.match(r"\d{1,2}-\d{1,2}-\d{4}", deadline):
        deadline = input("Введите дедлайн (день-месяц-год): ").strip()
        if not re.match(r"\d{1,2}-\d{1,2}-\d{4}", deadline):
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
        f"\n{i}. Имя: {note['Имя']}\n"
        f"Заголовок: {note['Заголовок']}\n"
        f"Описание: {note['Описание']}\n"
        f"Статус: {note['Статус']}\n"
        f"Дата создания: {note['Дата создания']}\n"
        f"Дедлайн: {note['Дедлайн']}"
    )
