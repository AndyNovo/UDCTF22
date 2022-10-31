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
        print("Not the right guess length")
        return False
    if not alphacheck(guess_in):
        print("Invalid characters A-Z only")
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
        return
    if len(result["correct"]) == len(problem["answer"]):
        print("You win the flag is %s" % (flag))
        exit(0)
    problem["guesses"] += 1
    if (problem["guesses"] >= 6):
        print("You lose")
        exit(1)
    print(result, "Guesses used:", problem["guesses"])

def main():
    problem = challenge()
    print("WELCOME TO DAD JOKE WORDLE: Your joke is %s letters long. It starts with %s" % (len(problem["answer"]), problem["answer"][:2]))

    while problem["guesses"] < 6:
        guess = input("Guess? >\n")
        makeguess(guess,problem)

main()
