import sqlite3
conn = sqlite3.connect('lotr.db')
cur = conn.cursor()

# cur.execute(
#     """
#         CREATE TABLE characters(
#             name text,
#             race text,
#             life_status text,
#             image_url text
#         )
#     """)

# cur.execute("INSERT INTO characters VALUES ('Gandalf', 'Istar (Wizard)', 'alive', 'https://static.wikia.nocookie.net/lotr/images/e/e7/Gandalf_the_Grey.jpg/revision/latest?cb=20121110131754')")
# cur.execute("INSERT INTO characters VALUES ('Aragorn', 'Man (Dunedain)', 'dead', 'https://static.wikia.nocookie.net/lotr/images/b/b6/Aragorn_profile.jpg/revision/latest?cb=20170121121423')")

def add_character():
    name = input('Please enter the characters name: ').lower()
    race = input('Please enter the race of this character: ').lower()
    status = input('Please enter whether this character is alive, dead, or unknown: ').lower()
    image_url = input('Please add an image URL if you have one: ').lower()

    with conn:
        cur.execute("INSERT INTO characters VALUES (:name, :race, :status, :image_url)", {'name': name, 'race': race, 'status': status, 'image_url': image_url})

    print(f'{name} was sucessfully added!')

def remove_character():
    name = input('Please enter the characters name that you would like to delete: ').lower()

    with conn:
        cur.execute("DELETE FROM characters WHERE name = :name", {'name': name})

    print(f'{name} was sucessfully deleted.')

def update_character_life_status():
    name = input('Please enter the name of the character: ').lower()
    status = input('Please enter this characters new status: alive, dead, or unknown: ').lower()

    with conn:
        cur.execute("UPDATE characters SET life_status = :status WHERE name= :name", {'name': name, 'status': status})

    print(f"{name}'s life staus was sucessfully updated to '{status}''.")

def get_characters():
    cur.execute("SELECT * FROM characters")
    return cur.fetchall()

def get_character():
    name = input('Please enter the name of the character: ').lower()

    cur.execute("SELECT * FROM characters WHERE name = :name", {'name': name})
    return cur.fetchone()


# Start program


print("Welcome to The Lord of the Rings Character Database!\n")

print("What would you like to do? Please select a number: ")

continue_program = True

while continue_program:
    selection = input("""
        1. View all the characters.
        2. Find character by name.
        3. Delete a character.
        4. Add a character.
        5. Change a characters life status.
        6. Exit.
    """)

    if (selection == '1'):
        characters = get_characters()
        index = 1
        for character in characters:
            print(f"{index}) Name: {character[0]}, Race: {character[1]}, Life Status: {character[2]}, Image Link: {character[3]}")
            index += 1
    elif (selection == '2'):
        character = get_character()
        print(f"""
            Name: {character[0]}
            Race: {character[1]}
            Life Status: {character[2]}
            Image Link: {character[3]}
        """)
    elif (selection == '3'):
        remove_character()
    elif (selection == '4'):
        add_character()
    elif (selection == '5'):
        update_character_life_status()
    elif (selection == '6'):
        print('Come again soon!!')
        continue_program = False
    else:
        print('Please ensure that your selection is a number between 1 and 6')