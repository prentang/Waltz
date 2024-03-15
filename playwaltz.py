import stdaudio
import stdio
import sys



#Read the waltz measures from standard input into a 1D list.
waltz = stdio.readInt()


#The followng needds to read the whole list
#If the number of measures is not 32: error
if len(waltz) != 32:
        sys.exit("A waltz must contain exactly 32 measures")

#16 of them need to be from minuet
#if the first 16 are not 1 -> 176: error
for i in range(0,16):
    if waltz[i] <= 1 or waltz[i] >= 176:
        sys.exit("A minuet measure must be from [1, 176]")
    Minuet = "data/M" + str(waltz[i])
    stdaudio.playFile(Minuet)
    stdaudio.wait()

#16 of them need to be from trio
#if the second 16 are not 1 -> 96: error
for i in range(16,32):
    if waltz[i] <= 1 or waltz[i] >= 96:
        sys.exit("A trio measure must be from [1, 96]")
    Trio = "data/T" + str(waltz[i])
    stdaudio.playFile(Trio)
    stdaudio.wait()
