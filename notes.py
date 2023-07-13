import json

class Notes:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        note = {
            'title': title,
            'content': content
        }
        self.notes.append(note)
        self.save_notes()

    def get_notes(self):
        return self.notes

    def edit_note(self, note_index):
        if note_index < 1 or note_index > len(self.notes):
            return False

        new_content = input("Введите новое содержимое заметки: ")
        self.notes[note_index - 1]['content'] = new_content
        self.save_notes()
        return True

    def delete_note(self, note_index):
        if note_index < 1 or note_index > len(self.notes):
            return False

        del self.notes[note_index - 1]
        self.save_notes()
        return True

    def save_notes(self):
        with open('data.json', 'w') as file:
            json.dump(self.notes, file)

    def load_notes(self):
        try:
            with open('data.json', 'r') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []