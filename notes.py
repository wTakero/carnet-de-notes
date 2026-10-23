import csv


def lire_notes(chemin):
    notes = []
    with open(chemin, encoding="utf-8") as fichier:
        for ligne in csv.DictReader(fichier, delimiter=";"):
            notes.append(float(ligne["note"]))
    return notes


def mention(moyenne):
    if moyenne >= 16:
        return "Très bien"
    if moyenne >= 14:
        return "Bien"
    if moyenne >= 12:
        return "Assez bien"
    return "Passable"


notes = lire_notes("eleves.csv")
moyenne = sum(notes) / 3
print(f"Moyenne : {moyenne}")

with open("rapport.txt", "w", encoding="utf-8") as rapport:
    rapport.write(f"{len(notes)} notes, moyenne {moyenne}\n")
