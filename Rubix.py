import MusicalNotes as mn

class RubixCube:
  def __init__(self):
    notes = mn.Notes()
    chord0 = mn.Chord([notes.A,notes.Csharp,notes.E])
    chord1 = mn.Chord([notes.E,notes.G,notes.C])
    chord2 = mn.Chord([notes.A,notes.D,notes.F])
    chord3 = mn.Chord([notes.B,notes.Dsharp,notes.Fsharp])
    chord4 = mn.Chord([notes.D,notes.Fsharp,notes.A])
    chord5 = mn.Chord([notes.G,notes.Eb,notes.Bb])

    self.faces = [CubeFace(0,"green",chord0),CubeFace(1,"red",chord1),CubeFace(2,"yellow",chord2),CubeFace(3,"orange",chord3),CubeFace(4,"white",chord4),CubeFace(5,"blue",chord5)]
  

  def getFace(self,n):
    return self.faces[n]
  
  def getSquareAtFace(self,face,sqr):
    return self.getFace(face).getSquare(sqr)

  def getColorOfSqrAtFace(self,face,sqr):
    return self.getSquareAtFace(face,sqr).color
  
  def copyOfFace(self,face):
    return self.faces[n][:]
  
  def horizontalSwap(self,face1,face2,face3,face4,orientation):
    if orientation=="top":
      i,j,k = 0,1,2 
    elif orientation=="bottom":
      i,j,k = 6,7,8

    face1[i],face1[j],face1[k],face2[i],face2[j],face2[k],face3[i],face3[j],face3[k],face4[i],face4[j],face4[k] = face4[i],face4[j],face4[k],face1[i],face1[j],face1[k],face2[i],face2[j],face2[k],face3[i],face3[j],face3[k]
    
  def verticalSwap(self,face1,face2,face3,face4,orientation):
    if orientation=="front":
      i,j,k,l,m,n,o,p,q = 0,1,2,3,4,5,6,7,8 
      face1[k],face1[n],face1[q],face2[o],face2[p],face2[q],face3[i],face3[l],face3[o],face4[o],face4[p],face4[q] = face4[o],face4[p],face4[q],face1[k],face1[n],face1[q],face2[o],face2[p],face2[q],face3[i],face3[l],face3[o]
    elif orientation=="back":
      face1[0],face1[3],face1[6],face2[0],face2[1],face2[2],face3[2],face3[5],face3[8],face4[0],face4[1],face4[2] = face4[0],face4[1],face4[2],face1[0],face1[3],face1[6],face2[0],face2[1],face2[2],face3[2],face3[5],face3[8]
    elif orientation=="left":
      face1[0],face1[3],face1[6],face2[0],face2[3],face2[6],face3[2],face3[5],face3[8],face4[0],face4[3],face4[6] = face4[0],face4[3],face4[6],face1[0],face1[3],face1[6],face2[0],face2[3],face2[6],face3[2],face3[5],face3[8]
    elif orientation=="right":
      face1[2],face1[5],face1[8],face2[2],face2[5],face2[8],face3[0],face3[3],face3[6],face4[2],face4[5],face4[8] = face4[2],face4[5],face4[8],face1[2],face1[5],face1[8],face2[2],face2[5],face2[8],face3[0],face3[3],face3[6]
    


  def rotateTop(self,clockwise=True):
    #face 0
    if clockwise:
      self.getFace(0).rotate(True)
      self.horizontalSwap(self.getFace(1).squares,self.getFace(2).squares,self.getFace(3).squares,self.getFace(4).squares,"top")
    else:
      self.getFace(0).rotate(False)
      self.horizontalSwap(self.getFace(1).squares,self.getFace(4).squares,self.getFace(3).squares,self.getFace(2).squares,"top")

      

  def rotateBottom(self,clockwise=True):
    #face 5
    if clockwise:
      self.getFace(5).rotate(True)
      self.horizontalSwap(self.getFace(1).squares,self.getFace(2).squares,self.getFace(3).squares,self.getFace(4).squares,"bottom")
    else:
      self.getFace(5).rotate(False)
      self.horizontalSwap(self.getFace(1).squares,self.getFace(4).squares,self.getFace(3).squares,self.getFace(2).squares,"bottom")

  def rotateBack(self,clockwise=True):
    #face 4
    if clockwise:
      self.getFace(4).rotate(True)
      self.verticalSwap(self.getFace(3).squares,self.getFace(0).squares,self.getFace(1).squares,self.getFace(5).squares,"back")
    else:
      self.getFace(4).rotate(False)
      self.verticalSwap(self.getFace(3).squares,self.getFace(5).squares,self.getFace(1).squares,self.getFace(0).squares,"back")

  def rotateFront(self,clockwise=True):
    #face 2
    if clockwise:
      self.getFace(2).rotate(True)
      self.verticalSwap(self.getFace(3).squares,self.getFace(0).squares,self.getFace(1).squares,self.getFace(5).squares,"front")
    else:
      self.getFace(2).rotate(False)
      self.verticalSwap(self.getFace(3).squares,self.getFace(5).squares,self.getFace(1).squares,self.getFace(0).squares,"front")

  def rotateLeft(self,away=True):
    #face 3
    if away:
      self.getFace(3).rotate(False)
      self.verticalSwap(self.getFace(2).squares,self.getFace(0).squares,self.getFace(4).squares,self.getFace(5).squares,"left")
    else:
      self.getFace(3).rotate(True)
      self.verticalSwap(self.getFace(2).squares,self.getFace(5).squares,self.getFace(4).squares,self.getFace(0).squares,"left")

  def rotateRight(self,away=True):
    #face 1
    if away:
      self.getFace(1).rotate(False)
      self.verticalSwap(self.getFace(2).squares,self.getFace(0).squares,self.getFace(4).squares,self.getFace(5).squares,"right")
    else:
      self.getFace(1).rotate(True)
      self.verticalSwap(self.getFace(2).squares,self.getFace(5).squares,self.getFace(4).squares,self.getFace(0).squares,"right")
    

  def reset(self,none=None):
    self.__init__()

  def display(self):
    raw_output = []
    raw_faces = [face.squares for face in self.faces]
    for f in range(0,len(raw_faces)):
      face_output = []
      for sqr in raw_faces[f]:
        face_output.append(sqr.color)
      raw_output.append(face_output)
    #print(raw_output)
    return raw_output

  def noteDisplay(self):
    raw_output = []
    raw_faces = [face.squares for face in self.faces]
    for f in range(0,len(raw_faces)):
      face_output = []
      for sqr in raw_faces[f]:
        face_output.append(sqr.note[1])
      raw_output.append(face_output)
    print(raw_output)
    return raw_output

  
    
  

class CubeFace:
  def __init__(self,number,nativeColor,nativeChord):
    self.number = number
    notes = nativeChord.notes
    self.squares = [Color(nativeColor,notes[0]),Color(nativeColor,notes[1]),Color(nativeColor,notes[2]),Color(nativeColor,notes[1]),Color(nativeColor,notes[2]),Color(nativeColor,notes[0]),Color(nativeColor,notes[2]),Color(nativeColor,notes[0]),Color(nativeColor,notes[1])]
  
  def getSquare(self,n):
    return self.squares[n]

  def setSquareEqualTo(self,n,sqr):
    self.squares[n] = sqr

  def rotate(self,clockwise=True):
    if clockwise:
      newFace = [6,3,0,7,4,1,8,5,2] # permutation of indices when rotated cw
      self.squares = [self.getSquare(i) for i in newFace]
    else:
      newFace = [2,5,8,1,4,7,0,3,6] # permutation of indices when rotated ccw
      self.squares = [self.getSquare(i) for i in newFace]

  def getUniqueNotes(self):
    uniqueNotes = []
    for square in self.squares:
        if square.note not in uniqueNotes:
            uniqueNotes.append(square.note)

    return uniqueNotes
  
  def playFace(self):
    uniqueNotes = self.getUniqueNotes()
    faceChord = mn.Chord(uniqueNotes)
    faceChord.play(loop=0)





class Color:
  def __init__(self,color,note):
    self.color = color
    self.note = note



#[['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green'], ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'], ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow'], ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'], ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'], ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']]