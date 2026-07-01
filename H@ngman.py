import random

print("Welcome to H@ngman! You have 10 (wrong) attempts to guess the word. Good luck!")

def converttostring(current):
    return ' '.join(current)


def remainingletters(guessed):
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    return ' '.join(letter for letter in validletters if letter not in guessed)


def hangman(current, targetword, lettersguessed):
    wrong = 0
    totalguesses = 0
    while wrong < 10:
        letter = input("What letter would you like to guess? ").lower()
        validletters = 'abcdefghijklmnopqrstuvwxyz'

        if len(letter) != 1 or letter not in validletters:
            print("Not a letter!! Try again >:(")
            continue

        if letter in lettersguessed:
            print("You already guessed that!")
            continue

        totalguesses += 1

        if letter in targetword:
            print("Your letter is in the word! " + str(10 - wrong) + " wrong guesses allowed remaining")
            lettersguessed.append(letter)
            for i in range(len(targetword)):
                if letter == targetword[i]:
                    current[i] = letter
            print(converttostring(current))
            print("Letters left to try: " + remainingletters(lettersguessed), end="\n\n")

        else:
            wrong += 1
            print("Your letter is not in the word! " + str(10 - wrong) + " wrong guesses remaining")
            lettersguessed.append(letter)
            print(converttostring(current))
            print("Letters left to try: " + remainingletters(lettersguessed), end="\n\n")

        if '_' not in current:
            print("You guessed the word!")
            break

        if wrong >= 10:
            print("You ran out of tries! try again next time :(")
            break

    return totalguesses


wordsplayed = []

WORDS = {
    1: ('antidisestablishmentarianism',
        "the opposition to the disestablishment of the Church of England"),
    2: ('deltarune',
        "an episodic role-playing video game developed by Toby Fox as a follow-up to his 2015 video game Undertale. In the game, the player controls a human teenager, Kris, who is destined to save the world together with Susie, a monster, and Ralsei, a prince from the Dark World."),
    3: ('undertale',
        "a 2015 2D role-playing video game created by American indie developer Toby Fox. The player controls a child who has fallen into the Underground: a large, secluded region under the surface of the Earth, separated by a magical barrier."),
    4: ('pneumonoultramicroscopicsilicovolcanoconiosis',
        "an invented long word said to mean a lung disease caused by inhaling very fine ash and sand dust from a volcano/volcanic area."),
    5: ('zebra',
        "an African wild horse with black-and-white stripes and an stand up mane."),
    6: ('hippopotomonstrosesquippedaliophobia',
        "the fear of long words. It's also known as sesquipedalophobia, which is a Latin term that means long word"),
    7: ('ghostwriter',
        "a person whose job it is to write material for someone else who is the named author."),
    8: ('atmosphere',
        "the envelope of gases surrounding the earth or another planet."),
    9: ('integrated',
        "with various parts or aspects linked or coordinated."),
    10: ('disturbance',
         "the interruption of a settled and peaceful condition."),
    11: ('supplementary',
         "completing or enhancing something."),
    12: ('allowance',
         "the amount of something that is permitted, especially within a set of regulations or for a specified purpose"),
    13: ('echocardiagram',
         "a test of the action of the heart using ultrasound waves to produce a visual display, used for the diagnosis or monitoring of heart disease."),
    14: ('excavation',
         "the action of excavating something, especially an archaeological site."),
    15: ('progressive',
         "happening or developing gradually or in stages; proceeding step by step. or, a person advocating or implementing social reform or new, liberal ideas."),
    16: ('negligence',
         "failure to take proper care in doing something."),
    17: ('mechanical',
         "working or produced by machines or machinery. or, (of a person or action) not having or showing thought or spontaneity; automatic."),
    18: ('simplicity',
         "the quality or condition of being easy to understand or do. or, the quality or condition of being plain or natural."),
    19: ('identification',
         "the action or process of identifying someone or something or the fact of being identified. or, a means of proving a person's identity, especially in the form of official papers."),
    20: ('randomization',
         "the arrangement of a set of items, people, etc. in an unpredictable, unsystematic, or random order."),
}


def wordpicker():
    if len(wordsplayed) > 0:
        print("You have played numbers: " + str(wordsplayed))

    while True:
        raw = input("Pick a number between 1 and 20 (or type 'r' for a random word): ").strip().lower()

        if raw in ('r', 'random'):
            available = [n for n in WORDS if n not in wordsplayed]
            if not available:
                print("You've played every word! Starting the list over.")
                wordsplayed.clear()
                available = list(WORDS)
            playerword = random.choice(available)
            break

        try:
            playerword = int(raw)
        except ValueError:
            print("Please enter a number, not text.")
            continue

        if playerword not in WORDS:
            print("Not a valid answer")
            continue

        if playerword in wordsplayed:
            print("You already guessed that word!")
            continue

        break

    targetword, endmessage = WORDS[playerword]
    return targetword, endmessage, playerword


current = []
targetword, endmessage, playerword = wordpicker()
for i in range(len(targetword)):
    current.append("_")

lettersguessed = []
averageguesses = []
print(current)

attempts = hangman(current, targetword, lettersguessed)
games = 1


while True:
    print(targetword + ": " + endmessage)

    play = input("Would you like to play again? ").strip().lower()

    averageguesses.append(attempts)
    average = sum(averageguesses) / len(averageguesses)

    if play in ('yes', 'y'):
        games += 1
        wordsplayed.append(playerword)
        lettersguessed = []
        current = []
        targetword, endmessage, playerword = wordpicker()
        for i in range(len(targetword)):
            current.append("_")
        attempts = hangman(current, targetword, lettersguessed)  # FIX #4: capture the return value on replays too
        print("You have played " + str(games) + " games so far!")
        print("Your average guesses: " + str(average))

    elif play in ('no', 'nah', 'n'):
        print("aww okay :(")
        print("You played " + str(games) + " games in total!")
        print("Your average guesses were: " + str(average))
        print(endmessage)
        break

    else:
        print("Answer the question >:(")