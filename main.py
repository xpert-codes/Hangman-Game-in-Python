import random
turns = 6

words = ['house', 'hotel', 'sport', 'bat', 'leafy']
word = random.choice(words)
guesses = ''
score = 0
while turns > 0:
    print(f"\nScore: {score}")
    print((f"Incorrect gusses left: {turns}"))
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end='')

        else:
            print("_ ", end='')
            failed += 1

    if failed == 0:
        print("\n\nYou Win")
        break
    guess = input("\n\nEnter Guess: ")
    guesses += guess

    if guess in word:
        score += 2
    if guess not in word:

        turns -= 1
        print("\nWrong\n")

        if turns == 0:
            print("You Loose")

file1 = open("myfile.txt","w")#write mode
file1.write(f"Score: {score}")
file1.close()
