import math
import wave
import struct

# List of frequencies and their amplitudes
def synthComplex(freq=[440],coef=[1], datasize=10000, fname="test.wav"):
    frate = 44100.00  
    amp=8000.0 
    sine_list=[]
    for x in range(datasize):
        samp = 0
        for k in range(len(freq)):
            samp = samp + coef[k] * math.sin(2*math.pi*freq[k]*(x/frate))
        sine_list.append(samp)
    wav_file=wave.open(fname,"w")
    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes=datasize
    comptype= "NONE"
    compname= "not compressed"
    wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    for s in sine_list:
        wav_file.writeframes(struct.pack('h', int(s*amp/2)))
    wav_file.close()

synthComplex([262], [1], 30000, "C.wav")
synthComplex([330], [1], 30000, "E.wav")
synthComplex([392], [1], 30000, "G.wav")
synthComplex([440], [1], 30000, "A.wav")
synthComplex([277], [1], 30000, "C#.wav")
synthComplex([494], [1], 30000, "B.wav")
synthComplex([311], [1], 30000, "D#.wav")
synthComplex([370], [1], 30000, "F#.wav")
synthComplex([294], [1], 30000, "D.wav")
synthComplex([349], [1], 30000, "F.wav")
synthComplex([311], [1], 30000, "Eb.wav")
synthComplex([466], [1], 30000, "Bb.wav")