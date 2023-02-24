#Change numbers letters or di mo ... https://www.kalimbatabs.net/kalimba-letter-number-notation-converter/
import json
import os

file_name = "Cant_Help_Falling_In_Love_on_a_Kalimba.kal"

# Lesen von JSON-Daten aus der ausgewählten Datei
with open(file_name) as f:
    kal_data = json.load(f)
# Filtern von leeren Noten und leeren Maßnahmen
kal_data["song"] = [[note for note in measure if note["note"]] for measure in kal_data["song"] if measure]
# Schreiben von JSON-Daten in die Datei "out.kal"
with open("out.kal", "w") as f:
    json.dump(kal_data, f)
# Lesen von JSON-Daten aus der Datei "out.kal" und Umkehrung der "song"-Liste
with open("out.kal") as f:
    data = json.load(f)
    data["song"] = data["song"][::-1]
# Schreiben von JSON-Daten in die Datei "out2.kal"
with open("out2.kal", "w") as f:
    json.dump(data, f)

# Umwandlungsliste definieren
CDur = {
    'C4': '1',
    'D4': '2',
    'E4': '3',
    'F4': '4',
    'G4': '5',
    'A4': '6',
    'B4': '7',
    'C5': '1*',
    'D5': '2*',
    'E5': '3*',
    'F5': '4*',
    'G5': '5*',
    'A5': '6*',
    'B5': '7*',
    'C6': '1**',
    'D6': '2**',
    'E6': '3**'
}

DDur = {
    'D4': '1',
    'E4': '2',
    'F#4': '3',
    'G4': '4',
    'A4': '5',
    'B4': '6',
    'C#4': '7',
    'D5': '1*',
    'E5': '2*',
    'F#5': '3*',
    'G5': '4*',
    'A5': '5*',
    'B5': '6*',
    'C#5': '7*',
    'D6': '1**',
    'E6': '2**',
    'F#6': '3**'
}

EDur = {
'E4': '1',
'F#4': '2',
'G#4': '3',
'A4': '4',
'B4': '5',
'C#5': '6',
'D#5': '7',
'E5': '1*',
'F#5': '2*',
'G#5': '3*',
'A5': '4*',
'B5': '5*',
'C#6': '6*',
'D#6': '7*',
'E6': '1**',
'F#6': '2**',
'G#6': '3**'
}

FDur = {
'F4': '1',
'G4': '2',
'A4': '3',
'A#4': '4',
'C5': '5',
'D5': '6',
'E5': '7',
'F5': '1*',
'G5': '2*',
'A5': '3*',
'A#5': '4*',
'C6': '5*',
'D6': '6*',
'E6': '7*',
'F6': '1**',
'G6': '2**',
'A6': '3**'
}

GDur = {
'G4': '1',
'A4': '2',
'B4': '3',
'C5': '4',
'D5': '5',
'E5': '6',
'F#5': '7',
'G5': '1*',
'A5': '2*',
'B5': '3*',
'C6': '4*',
'D6': '5*',
'E6': '6*',
'F#6': '7*',
'G6': '1**',
'A6': '2**',
'B6': '3**'
}

ADur = {
'A4': '1',
'B4': '2',
'C#5': '3',
'D5': '4',
'E5': '5',
'F#5': '6',
'G#5': '7',
'A5': '1*',
'B5': '2*',
'C#6': '3*',
'D6': '4*',
'E6': '5*',
'F#6': '6*',
'G#6': '7*',
'A6': '1**',
'B6': '2**',
'C#7': '3**'
}

HDur = {
'B4': '1',
'C#5': '2',
'D#5': '3',
'E5': '4',
'F#5': '5',
'G#5': '6',
'A#5': '7',
'B5': '1*',
'C#6': '2*',
'D#6': '3*',
'E6': '4*',
'F#6': '5*',
'G#6': '6*',
'A#6': '7*',
'B6': '1**',
'C#7': '2**',
'D#7': '3**'
}

CMoll = {
'C4': '1',
'D4': '2',
'Eb4': '3',
'F4': '4',
'G4': '5',
'Ab4': '6',
'Bb4': '7',
'C5': '1*',
'D5': '2*',
'Eb5': '3*',
'F5': '4*',
'G5': '*',
'Ab5': '6*',
'Bb5': '7*',
'C6': '1**',
'D6': '2**',
'Eb6': '3**'
}

DMoll = {
'D4': '1',
'E4': '2',
'F4': '3b',
'G4': '4',
'A4': '5',
'Bb4': '6',
'C5': '7',
'D5': '1*',
'E5': '2*',
'F5': '3b*',
'G5': '4*',
'A5': '5*',
'Bb5': '6*',
'C6': '7*',
'D6': '1**',
'E6': '2**',
'F6': '3b**'
}

EMoll = {
'E4': '1',
'F#4': '2',
'G4': '3',
'A4': '4',
'B4': '5',
'C5': '6',
'D5': '7',
'E5': '1*',
'F#5': '2*',
'G5': '3*',
'A5': '4*',
'B5': '5*',
'C6': '6*',
'D6': '7*',
'E6': '1**',
'F#6': '2**',
'G6': '3**'
}

Fmoll = {
'F4': '1',
'G4': '2b',
'Ab4': '3',
'Bb4': '4',
'C5': '5b',
'Db5': '6',
'Eb5': '7',
'F5': '1*',
'G5': '2b*',
'Ab5': '3*',
'Bb5': '4*',
'C6': '5b*',
'Db6': '6*',
'Eb6': '7*',
'F6': '1**',
'G6': '2b**',
'Ab6': '3**'
}

GMoll = {
'G3': '1',
'A3': '2',
'Bb3': '3',
'C4': '4',
'D4': '5',
'Eb4': '6',
'F4': '7',
'G4': '1*',
'A4': '2*',
'Bb4': '3*',
'C5': '4*',
'D5': '5*',
'Eb5': '6*',
'F5': '7*',
'G5': '1**',
'A5': '2**',
'Bb5': '3**'
}

AMoll = {
'A4': '1',
'B4': '2',
'C5': '3',
'D5': '4',
'E5': '5',
'F5': '6',
'G5': '7',
'A5': '1*',
'B5': '2*',
'C6': '3*',
'D6': '4*',
'E6': '5*',
'F6': '6*',
'G6': '7*',
'A6': '1**',
'B6': '2**',
'C7': '3**'
}

Hmoll = {
'B3': '1',
'C#4': '2',
'D4': '3',
'E4': '4',
'F#4': '5',
'G4': '6',
'A4': '7',
'B4': '1*',
'C#5': '2*',
'D5': '3*',
'E5': '4*',
'F#5': '5*',
'G5': '6*',
'A5': '7*',
'B5': '1**',
'C#6': '2**',
'D6': '3**'
}

# Lese die JSON-Datei ein
with open('out2.kal', 'r') as f:
    data = json.load(f)

# Extrahiere die Noten aus dem JSON-Objekt
notes_list = []
for sections in data['song']:
    note = []
    for selection in sections:
        note.append(selection['note'])
    notes_list.append(note)

# Konvertiere Noten von Buchstaben zu Zahlen
notes_numbers = []
for note_list in notes_list:
    notes_number = []
    for note in note_list:
        if note == "rest":
            notes_number.append(note)
        else:
            notes_number.append(CDur[note]) ################################################################# Ändern für andere tonleiter
    notes_numbers.append(notes_number)

# Konvertiere Liste von Notenlisten in einen String mit Zahlen
endformat = ""
for note_list in notes_numbers:
    if len(note_list) > 1:
        endformat += "(" + " ".join(note_list) + ") "
    else:
        if note_list[0] == "rest":
            endformat += "\n"
        else:
            endformat += note_list[0] + " "

# Schreibe die Noten in eine Textdatei
with open(file_name[:-4]+"_numbers.txt", 'w') as f:
    f.write(endformat)

files_to_remove = ['out.kal', 'out2.kal']
for file in files_to_remove:
    os.remove(file)