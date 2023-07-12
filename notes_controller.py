import notes_db
import mysql.connector
from datetime import datetime as dt

cnx = mysql.connector.connect(user="root", database="notes")
cursor = cnx.cursor()


def create_note():
    add_note = "INSERT INTO `note`(`name`, `description`, `date`) VALUES( %s, %s, %s)"
    test_note = ("ligma", "test note for the database", dt.now().date())
    cursor.execute(add_note, test_note)
    cnx.commit()


def display_notes():
    display_notes = "SELECT * FROM `note`"
    cursor.execute(display_notes)
    for id, name, description, date in cursor:
        print(
            f"Note id: {id}\nNote: {name}\nDescription: {description}\nDate: {date}\n"
        )


def update_note():
    note_id = input("Note id")
    new_note_name = input("New Name of the note")
    new_description_note = input("New Description of the note")
    new_date_note = input("New Date of the note")
    update_notes = "update notes SET name = %s, description = %s, date = %s WHERE id = %s"
    new_data = (new_note_name, new_description_note, new_date_note, note_id)
    cursor.execute(update_notes, new_data)


    

def delete_note():
    delete_note = "DELETE FROM `note` WHERE `id` = %s"
    delete = input("Insert the note nuber you want to delete")
    cursor.execute(delete_note, (delete,))
    cnx.commit()


def delete_all_notes():
    delete_notes = "DELETE * FROM `note`"
    cursor.execute(delete_notes)
    cnx.commit()


display_notes()
delete_note()
