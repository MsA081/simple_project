num_notes = int(input('Please enter the number of texts: '))

note_list = []

for id in range(1, num_notes+1):
    subject = str(input('Please enter the subject: '))
    text = str(input('Please enter the text: '))

    note = {'id': id, subject: text}
    note_list.append(note)

    with open(f"C:/Users/N.A/Desktop/project/{subject}.txt", mode="at") as file_test:
        file_test.write(text)
        file_test.close()

def find_note_text():
    get_subject = input('Please enter the subject of the note: ')

    found_notes = list(filter(lambda item : item.get(get_subject), note_list))

    if found_notes:
        for note_text in found_notes:
            print(note_text)
    else:
        print('Note not found.')

find_note_text()