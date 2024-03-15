import stdarray
import stdrandom
import stdio


#Create a 2D list that measures 11 x 16
#Read the minuet measures from standard output
mm = stdarray.create2D(11, 16)
for i in range(11):
    for j in range(16):
       mm[i][j] = stdio.readInt()

#random sequence of 16 numbers
for count in range(16):
    
    #sum of two die roll
    randroll1 = stdrandom.uniformInt(1,7)
    randroll2 = stdrandom.uniformInt(1,7)
    
    #making rolls fit into the range of 0-10; 2-12 on the rows for the table
    sum = randroll1 + randroll2 - 2
    i = sum

    #value of index j: 0-15
    j = stdrandom.uniformInt(0,16)
    
    #Set selection of row and column to minuet measure(Mmeasure)
    Mmeasure = mm[i][j]

    #write standard output
    stdio.writef('%i ', Mmeasure)


#Create a 2D list that measures 6x16
#Read the trio measures from standard output
tm = stdarray.create2D(6, 16)
for i in range(6):
    for j in range(16):
        tm[i][j] = stdio.readInt()


#for the random sequence of trio, value index i; 0-5, value index j; 0-15
for count in range(16):
    
    #roll one random die for row from trio table
    i = stdrandom.uniformInt(0,6)
    
    j = stdrandom.uniformInt(0,16)
    Tmeasure = tm[i][j]

    #write standard output
    stdio.writef('%i ' ,Tmeasure)

stdio.writeln()


