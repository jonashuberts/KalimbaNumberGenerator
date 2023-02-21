#Todo: Success display after generation. Write notes played at the same time in brackets
from tkinter import Tk, Label, Radiobutton, IntVar, Button, filedialog
import mido

def midi_to_kalimba(midi_file, mode):
    mid = mido.MidiFile(midi_file)
    kalimba_notation = []

    notes = {
        60: '1',
        62: '2',
        64: '3',
        65: '4',
        67: '5',
        69: '6',
        71: '7',
        72: '1*',
        74: '2*',
        76: '3*',
        77: '4*',
        79: '5*',
        81: '6*',
        83: '7*',
        84: '1**',
        86: '2**',
        88: '3**'
    }

    if mode == "letters":
        notes = {
            60: 'C',
            62: 'D',
            64: 'E',
            65: 'F',
            67: 'G',
            69: 'A',
            71: 'B',
            72: 'C*',
            74: 'D*',
            76: 'E*',
            77: 'F*',
            79: 'G*',
            81: 'A*',
            83: 'B*',
            84: 'C**',
            86: 'D**',
            88: 'E**'
        }

    for i, track in enumerate(mid.tracks):
        for msg in track:
            if msg.type == 'note_on':
                note = msg.note
                if note in notes:
                    kalimba_notation.append(notes[note])
                else:
                    kalimba_notation.append("X")

    with open(f"{midi_file.split('.')[0]}_tabs.txt", "w") as f:
        f.write(" ".join(kalimba_notation))

def select_file():
    global midi_file
    midi_file = filedialog.askopenfilename(initialdir = "", title = "Select file", filetypes = (("MIDI files", "*.mid"), ("all files", "*.*")))

def generate_tabs():
    mode = var.get()
    if var.get() == 1:
        mode = "numbers"
    else:
        mode = "letters"
    midi_to_kalimba(midi_file, mode)

root = Tk()
root.title("Kalimba Number / Text Generator")

var = IntVar()

Label(root, text

= "Select the mode for the kalimba notation:").pack()
Radiobutton(root, text="Numbers", variable=var, value=1).pack()
Radiobutton(root, text="Letters", variable=var, value=2).pack()

Button(root, text="Select file", command=select_file).pack()
Button(root, text="Generate tabs", command=generate_tabs).pack()

root.mainloop()