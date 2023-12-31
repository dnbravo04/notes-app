import notes_db
import mysql.connector
from datetime import datetime as dt

cnx = mysql.connector.connect(user="root", database="notes")
cursor = cnx.cursor()


def create_note():
    try:
        note_name = input()
        add_note = "INSERT INTO `note`(`name`, `description`, `date`) VALUES( %s, %s, %s)"
        cursor.execute(add_note)
        return 'Note created succesfully'
        cnx.commit()
    except Exception as err:
        print('An error has ocurred while creating the note' + err)


def display_notes():
    try:
        display_notes = "SELECT * FROM `note`"
        cursor.execute(display_notes)
        for id, name, description, date in cursor:
            print(
                f"Note id: {id}\nNote: {name}\nDescription: {description}\nDate: {date}\n"
            )
    except Exception as err:
        print('An error has ocurred while creating the note' + err)
        

def update_note():
    try:
        note_id = input("Note id")
        new_note_name = input("New Name of the note:")
        new_description_note = input("New Description of the note:")
        new_date_note = input("New Date of the note in format YYYY-MM-DD:")
        update_notes = "UPDATE notes SET name = %s, description = %s, date = %s WHERE id = %s"
        new_data = (new_note_name, new_description_note, new_date_note, note_id)
        cursor.execute(update_notes, new_data)
    except Exception as err:
        print('An error has ocurred while creating the note' + err)

    

def delete_note():
    try:
        delete_note = "DELETE FROM `note` WHERE `id` = %s"
        delete = input("Insert the note nuber you want to delete")
        cursor.execute(delete_note, (delete,))
        cnx.commit()
    except Exception as err:
        print('An error has ocurred while deleting the note' + err)


def delete_all_notes():
    try:
        delete_notes = "DELETE * FROM `note`"
        cursor.execute(delete_notes)
        cnx.commit()
    except Exception as err:
        print('An error has ocurred while deleting the notes' + err)