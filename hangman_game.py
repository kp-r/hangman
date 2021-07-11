from random import choice
def word_generator():
    with open("wordlist.txt","r")as f:
        lines = f.readlines()
    f.close()
    lines = [i.strip("\n")for i in lines]
    return choice(lines)
word = word_generator()
guessed = ""
turns = int(len(word)*1.5)
while (True):
    print("You have {} chances left".format(turns))
    inp = input("\nMake a guess:")
    turns = turns -1
    if inp in word:
        guessed = guessed + inp
    unguessed_char =0 
    for i in word:
        if i in guessed:
            print(i,end="")
        else:
            unguessed_char +=1
            print("*",end="")
    if unguessed_char==0:
        print("\nHurray, You Won!!")
        break
    if turns ==0:
        print("\n \n Dude... The word was {}! You missed.".format(word))
        print("\n You ran out of attempts - So, you are Hanged!! ")
        break
