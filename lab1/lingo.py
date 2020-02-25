import random
print('LINGO-BINGO Welkom bij het kip en eieren spel! ')


def lingo():
    guessNum = input('Geef een viercijferig nummer in: ')
    
    # genarate random num and split it 
    numgen = random.randint(1000,10000)
    splitng = [int(y) for y in str(numgen)]
    # print('genarated number',splitng)
    
    # split quessed number
    splitqn=[int(x) for x in str(guessNum)]
    # print('guessed number',splitqn)
    
    #init counters
    gameCount=0
    while splitqn!=splitng:
        chickenCounter=0
        eggCounter=0
        gameCount+=1
            # check if number in the right order match
        for x in range(4):
            if splitqn[x]==splitng[x]: 
                chickenCounter+=1 
            # check if number is in the array
            elif splitqn[x] in splitng: 
                eggCounter+=1

        print(chickenCounter,'kiekes,',eggCounter,'eiers')
        splitqn = list(map(int, input("FOUT, Geef een viercijferig nummer in: ")))
    print('jaat zenne makker gehebt het, in {} tries'.format(gameCount))
lingo()