import signal
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphacheck(somestr):
    for c in somestr:
        if not c in alphabet:
            return False
    return True

f=open("jokes.txt","r")
lngstr=f.read()
f.close()
jokes = lngstr.split("\n")[:-1]
for joke in jokes:
    assert(alphacheck(joke))
print("Jokes are Upperclass.  Thanks to icanhazdadjoke.com!")
#The jokes were scraped and non alpha characters were stripped, the ñ was swapped for N (in the Jalepeño joke)
f=open("flag.txt","r")
flag=f.read()
f.close()

def histomaker(answer):
    result = {}
    for ltr in alphabet:
        result[ltr] = []
    for i in range(len(answer)):
        ltr = answer[i]
        result[ltr].append(i)
    return result

def checkguess(answer, guess_in):
    if len(guess_in) != len(answer):
        print("Guess length wrong")
        return False
    if not alphacheck(guess_in):
        print("Invalid characters")
        return False
    truth = histomaker(answer)
    guess = histomaker(guess_in)
    correct = []
    position = []
    for ltr in alphabet:
        tmp = guess[ltr]
        truetmp = truth[ltr]
        counter = 0
        for i in tmp:
            if i in truetmp:
                counter += 1
                correct.append(i)
        for i in tmp:
            if not i in correct:
                if len(truetmp) > counter:
                    counter += 1
                    position.append(i)
    correct.sort()
    position.sort()
    return {"correct": correct, "position": position}

def challenge():
    answer = random.choice(jokes)
    return {"answer": answer, "guesses": 0}

def makeguess(guess, problem):
    result = checkguess(problem["answer"], guess)
    if result == False:
        print("Invalid guess")
        return "bad"
    if len(result["correct"]) == len(problem["answer"]):
        print("One down")
        return "win"
    problem["guesses"] += 1
    if (problem["guesses"] >= 2):
        print("You lose")
        exit(1)
    print(result, "Guesses used:", problem["guesses"])
    return "continue"

def problem():
    problem = challenge()
    print("WELCOME TO DAD JOKE WORDLE: Your joke is %s letters long." % (len(problem["answer"])))

    while problem["guesses"] < 2:
        guess = input("Guess? >\n")
        tmp = makeguess(guess,problem)
        if tmp == "win":
            return True
    return False

signal.alarm(60)
for _ in range(10):
    tmp = problem()
    if not tmp:
        exit(1)
print("Well done! %s" % flag)
