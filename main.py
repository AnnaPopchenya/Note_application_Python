from notes import Notes


def main():
    notes = Notes()

    while True:
        print("\n=== Меню ===")
        print("1. Создать заметку")
        print("2. Посмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("0. Выход")

        choice = input("Введите номер операции: ")

        if choice == '1':
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержимое заметки: ")
            notes.create_note(title, content)
            print("Заметка успешно создана и сохранена.")
        elif choice == '2':
            notes_list = notes.get_notes()
            if len(notes_list) == 0:
                print("Список заметок пуст.")
            else:
                print("Список заметок:")
                for note in notes_list:
                    print(f"Заголовок: {note['title']}")
                    print(f"Содержимое: {note['content']}")
                    print()
        elif choice == '3':
            note_index = int(
                input("Введите номер заметки для редактирования: "))
            if notes.edit_note(note_index):
                print("Заметка успешно отредактирована.")
            else:
                print("Неверный номер заметки.")
        elif choice == '4':
            note_index = int(input("Введите номер заметки для удаления: "))
            if notes.delete_note(note_index):
                print("Заметка успешно удалена.")
            else:
                print("Неверный номер заметки.")
        elif choice == '0':
            break
        else:
            print("Неверный номер операции. Пожалуйста, повторите ввод.")


if __name__ == "__main__":
    main()
