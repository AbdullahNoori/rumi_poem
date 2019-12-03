









def forward_function(poem):
    print('______________Poem_Forwarad______________')
    print()
    for i in range(0, len(poem)):
        index = str(i+1) #index is changed into string 
        line = poem[i]  #line is set to the index of the poem
        print(index+":"+line)

def reversed_function(poem):
    print('_____________Poem_Reversed________________')
    for i in range(len(poem), 0, -1):  # for loop to take i in range from max len of poem to 0 and -1
        index = str(i) #index is changed into string 
        line = poem[i-1] 
        print(index+":"+line)

def unique_function(poem):
    print('_____________Poem_Unique________________')
    for lineIndex in range(0, len(poem)): 
        line = poem[lineIndex]
        print(lineIndex+1, end="")
        for wordIndex in range(len(poem[lineIndex]), 0, -1):
        #     index = str(wordIndex-1)
            # word = line[wordIndex]
            print(line[wordIndex-2], end="")
        print("")

if __name__ =='__main__':
    f = open("rumi_poem.txt",'r')
    poem = f.readlines()
    forward_function(poem)
    reversed_function(poem)
    unique_function(poem)
