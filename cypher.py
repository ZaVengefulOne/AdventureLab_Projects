import random


def encrypt(file_name, output_file_name):
    with open(file_name, "r", encoding="utf-8") as inp:
        text = inp.read().replace(' ', '').replace(',', '').replace('.', '')
    new_text = ''

    characters = list(text + " " * 10)

    for char in characters:
        if char != " ":
            if random.randint(0, 100) > 70:
                new_text += " "
        new_text += char
    with open(output_file_name, "w", encoding="utf-8") as out:
        out.write(new_text)
