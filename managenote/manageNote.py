import datetime
import os

class Note:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        date = datetime.datetime.now()
        note = Note(title, content, date)
        self.notes.append(note)

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                break

    def show_notes(self):
        for note in self.notes:
            print(f"Title: {note.title}")
            print(f"Content: {note.content}")
            print(f"Date: {note.date}")
            print("------------------")

    def search_notes(self, keyword):
        found_notes = []
        for note in self.notes:
            if keyword.lower() in note.title.lower() or keyword.lower() in note.content.lower():
                found_notes.append(note)
        return found_notes

    def save_notes_to_file(self, file_name):
        with open(file_name, "w") as file:
            for note in self.notes:
                file.write(f"{note.title}\n")
                file.write(f"{note.content}\n")
                file.write(f"{note.date}\n")
                file.write("------------------\n")

    def load_notes_from_file(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 4):
                    title = lines[i].strip()
                    content = lines[i+1].strip()
                    date = datetime.datetime.strptime(lines[i+2].strip(), "%Y-%m-%d %H:%M:%S.%f")
                    note = Note(title, content, date)
                    self.notes.append(note)

note_manager = NoteManager()

note_manager.create_note("Note 1", "This is the content of note 1")
note_manager.create_note("Note 2", "This is the content of note 2")
note_manager.create_note("Important Note", "This is an important note")

note_manager.show_notes()

note_manager.delete_note("Note 2")

note_manager.show_notes()

found_notes = note_manager.search_notes("important")
for note in found_notes:
    print(f"Title: {note.title}")
    print(f"Content: {note.content}")
    print(f"Date: {note.date}")
    print("------------------")

note_manager.save_notes_to_file("notes.txt")

note_manager.load_notes_from_file("notes.txt")

note_manager.show_notes()
#--------------------------------------
# num_notes = int(input('Please enter the number of texts: '))

# note_list = []

# for id in range(1, num_notes+1):
#     subject = str(input('Please enter the subject: '))
#     text = str(input('Please enter the text: '))

#     note = {'id': id, subject: text}
#     note_list.append(note)

#     with open(f"C:/Users/N.A/Desktop/project/{subject}.txt", mode="at") as file_test:
#         file_test.write(text)
#         file_test.close()

# def find_note_text():
#     get_subject = input('Please enter the subject of the note: ')

#     found_notes = list(filter(lambda item : item.get(get_subject), note_list))

#     if found_notes:
#         for note_text in found_notes:
#             print(note_text)
#     else:
#         print('Note not found.')

# find_note_text()