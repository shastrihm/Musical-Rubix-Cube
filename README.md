A while ago, I watched a video (https://www.youtube.com/watch?v=FW2Hvs5WaRY) that illuminated a neat connection between Rubix Cubes and musical notes thanks to Group Theory. 

The idea is that permutations of a Rubix Cube form a group in a similar way to notes in a chord. By assigning each solved face a harmonious chord (each square in the face is a note in 
the chord), a solution to the Rubix Cube can be expressed as a chord progression that slowly ascends from disharmony to harmony.  

(Requires pygame)
Rubix.py        --   API for simulating a 3x3 Rubix Cube. A cube contains 6 Face objects, which each contain 9 Color objects. The Color objects contain the color and musical note data.
MusicalNotes.py --   API for initializing musical notes and chords.
pygButton.py    --   A simple pygame button class. 
generateWav.py  --   Generates musical notes as individual .wav files which are then saved to a /notes folder. You must run this before running main.py for the program to access them.

main.py         --   Runs an interactive simulation. Through pygame, we display a flattened 3x3 Rubix Cube with the corresponding musical notes overlayed on each square. Playing around with the cube changes the position of colors and notes. If you press the "Play Current Cube State!" button, you'll hear the chords of the current configuration. The most harmonious chord will be the solved state. Play around with it and see if you can compose some music! 