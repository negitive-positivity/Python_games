print("Welcome to H@ngman! You have 18 attempts to guess the word. Good luck!")
def converttostring(current):
    returnedstring = ''

    for i in range(len(current)):
        returnedstring += current[i] + ' '

    return returnedstring

def hangman(current):
    attempts = 0
    while attempts < 18:
        letter = input("What letter would you like to guess? ").lower()
        validletters = 'abcdefghijklmnopqrstuvwxyz'

        if letter not in validletters:
            print("Not a letter!! Try again >:(")

        if letter in lettersguessed:
            print("You already guessed that!")       

        elif letter in validletters:
            if letter in targetword and attempts < 18:
                attempts += 1
                print("Your letter is in the word! " + str(18 - attempts) + " attempts remaining")
                lettersguessed.append(letter)
                for i in range(len(targetword)):
                    if letter == targetword[i]:
                        current[i] = letter
                print(converttostring(current))
                print("Letters guessed: " + str(lettersguessed), end="\n\n")
        
            elif letter not in targetword and attempts < 18:
                attempts += 1
                print("Your letter is not in the word! " + str(18 - attempts) + " attempts remaining")
                lettersguessed.append(letter)
                print(converttostring(current))
                print("Letters guessed: " + str(lettersguessed), end="\n\n")
                
        if attempts > 0 and '_' not in current:
            print("You guessed the word!")
            break
    
        elif attempts == 0:
            print("You ran out of tries! try again next time :(")
            break
                
    return attempts

wordsplayed = []

def wordpicker():
    if len(wordsplayed) > 0:
        print("You have played numbers: " + str(wordsplayed))
    playerword = int(input("Pick a number between 1 and 20: "))
    if playerword in wordsplayed or playerword == '':
        print("You already guessed that word!")
        playerword = int(input("Pick a number between 1 and 20: "))
    targetword = ''
    endmessage = ''
    if playerword >= 1 and playerword <= 20:
        if playerword == 1:
            targetword = 'antidisestablishmentarianism'
            endmessage = "the opposition to the disestablishment of the Church of England"
        elif playerword == 2:
            targetword = 'deltarune'
            endmessage = "an episodic role-playing video game developed by Toby Fox as a follow-up to his 2015 video game Undertale. In the game, the player controls a human teenager, Kris, who is destined to save the world together with Susie, a monster, and Ralsei, a prince from the Dark World."
        elif playerword == 3:
            targetword = 'undertale'
            endmessage = "a 2015 2D role-playing video game created by American indie developer Toby Fox. The player controls a child who has fallen into the Underground: a large, secluded region under the surface of the Earth, separated by a magical barrier."
        elif playerword == 4:
            targetword = 'pneumonoultramicroscopicsilicovolcanoconiosis'
            endmessage = "an invented long word said to mean a lung disease caused by inhaling very fine ash and sand dust from a volcano/volcanic area."
        elif playerword == 5:
            targetword = 'zebra'
            endmessage = "an African wild horse with black-and-white stripes and an stand up mane."
        elif playerword == 6:
            targetword = 'hippopotomonstrosesquippedaliophobia'
            endmessage = "the fear of long words. It's also known as sesquipedalophobia, which is a Latin term that means long word"
        elif playerword == 7:
            targetword = 'ghostwriter'
            endmessage = "a person whose job it is to write material for someone else who is the named author."
        elif playerword == 8:
            targetword = 'atmosphere'
            endmessage = "the envelope of gases surrounding the earth or another planet."
        elif playerword == 9:
            targetword = 'integrated'
            endmessage = "with various parts or aspects linked or coordinated."
        elif playerword == 10:
            targetword = 'disturbance'
            endmessage = "the interruption of a settled and peaceful condition."
        elif playerword == 11:
            targetword = 'supplementary'
            endmessage = "completing or enhancing something."
        elif playerword == 12:
            targetword = 'allowance'
            endmessage = "the amount of something that is permitted, especially within a set of regulations or for a specified purpose"
        elif playerword == 13:
            targetword = 'echocardiagram'
            endmessage = "a test of the action of the heart using ultrasound waves to produce a visual display, used for the diagnosis or monitoring of heart disease."
        elif playerword == 14:
            targetword = 'excavation'
            endmessage = "the action of excavating something, especially an archaeological site."
        elif playerword == 15:
            targetword = 'progressive'
            endmessage = "happening or developing gradually or in stages; proceeding step by step. or, a person advocating or implementing social reform or new, liberal ideas."
        elif playerword == 16:
            targetword = 'negligence'
            endmessage = "failure to take proper care in doing something."
        elif playerword == 17:
            targetword = 'mechanical'
            endmessage = "working or produced by machines or machinery. or, (of a person or action) not having or showing thought or spontaneity; automatic."
        elif playerword == 18:
            targetword = 'simplicity'
            endmessage = "the quality or condition of being easy to understand or do. or, the quality or condition of being plain or natural."
        elif playerword == 19:
            targetword = 'identification'
            endmessage = "the action or process of identifying someone or something or the fact of being identified. or, a means of proving a person's identity, especially in the form of official papers."
        elif playerword == 20:
            targetword = 'randomization'
            endmessage = "the arrangement of a set of items, people, etc. in an unpredictable, unsystematic, or random order."
    else:
        print("Not a valid answer")
        playerword = int(input("Pick a number between 1 and 20: "))
        
    return targetword, endmessage, playerword


current = []
targetword, endmessage, playerword = wordpicker()
for i in range(len(targetword)):
    current.append("_")
    
lettersguessed = []
averageguesses = []
print(current)

attempts = hangman(current)
games = 1


for i in range(100000000000000):
    print(targetword + ": " + endmessage)
    play = input("Would you like to play again? ")
    averageguesses.append(attempts)
    average = 0
    items = len(averageguesses)
    
    for i in range(items):
        average += averageguesses[i]
    average /= items
    
    if play == 'yes' or play == 'Yes':
        games += 1
        wordsplayed.append(playerword)
        lettersguessed = []
        current = []
        targetword, endmessage, playerword = wordpicker()
        for i in range(len(targetword)):
            current.append("_")
        hangman(current)
        print("You have played " + str(games) + " games so far!")
        print("Your average guesses: " + str(average))

    elif play == 'no' or play == 'No' or play == 'nah':
        print("aww okay :(")
        print("You played " + str(games) + " games in total!")
        print("Your average guesses were: " + str(average))
        print(endmessage)
        break

    else:
        print("Answer the question >:(")
