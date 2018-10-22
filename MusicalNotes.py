import pygame as pg
import time


class Chord:
    def __init__(self,notes):
        self.notes = notes
    def play(self,loop=0):
        for note in self.notes:
            note[0].play(loops=loop)
        time.sleep(0.7)
    def getNotes(self):
        print(self.notes)
        return self.notes
    def getNotesAsString(self):
        return [x[1] for x in self.notes]
        

class Notes:
    def __init__(self):
        self.A = (pg.mixer.Sound('notes\A.wav'),"A")
        self.B = (pg.mixer.Sound('notes\B.wav'),"B")
        self.Bb = (pg.mixer.Sound('notes\Bb.wav'),"Bb")
        self.Csharp = (pg.mixer.Sound('notes\C#.wav'),"C#")
        self.C = (pg.mixer.Sound('notes\C.wav'),"C")
        self.Dsharp = (pg.mixer.Sound('notes\D#.wav'),"D#")
        self.D = (pg.mixer.Sound('notes\D.wav'),"D")
        self.E = (pg.mixer.Sound('notes\E.wav'),"E")
        self.Eb = (pg.mixer.Sound('notes\Eb.wav'),"Eb")
        self.Fsharp = (pg.mixer.Sound('notes\F#.wav'),"F#")
        self.F = (pg.mixer.Sound('notes\F.wav'),"F")
        self.G = (pg.mixer.Sound('notes\G.wav'),"G") 











