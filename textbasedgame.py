import random

name = input("What is your name? ")

#choosing class + invalid protection
print("Classes: Druid, Fighter, Warlock, Mage, Rouge")
characterclass = input("What class do you choose? ")

valid = False
if characterclass == "druid" or characterclass == "Druid" or characterclass == "fighter" or characterclass == "Fighter" or characterclass == "warlock" or characterclass == "Warlock" or characterclass == "mage" or characterclass == "Mage" or characterclass == "rouge" or characterclass == "Rouge":
    valid = True

while valid == False:
    print("Invalid class detected! Try again.")
    characterclass = input("What class do you choose? ")
    if characterclass == "druid" or characterclass == "Druid" or characterclass == "fighter" or characterclass == "Fighter" or characterclass == "warlock" or characterclass == "Warlock" or characterclass == "mage" or characterclass == "Mage" or characterclass == "rouge" or characterclass == "Rouge":
        valid = True


#stats
health = 0
attack = 0
defense = 0

if characterclass == "druid" or  characterclass == "Druid":
    health = 85
    attack = 40
    defense = 3
    print(name + ", You have chosen Druid! ")

elif characterclass == "fighter" or characterclass == "Fighter":
    health = 80
    attack = 35
    defense = 3
    print(name + ", You have chosen Fighter! ")

elif characterclass == "Mage" or characterclass == "mage":
    health = 95
    attack = 37
    defense = 0
    print(name + ", You have chosen Mage! ")

elif characterclass == "warlock" or characterclass == "Warlock":
    health = 90
    attack = 35
    defense = 5
    print(name + ", You have chosen Warlock! ")

elif characterclass == "Rouge" or characterclass == "rouge":
    health = 85
    attack = 32
    defense = 2
    print(name + ", You have chosen Rouge! ")

else:
    print("Invalid class.")

    
#function/actual game
average = 0
timeshealed = 0
exp = 0
level = 0

for counter in range(2):

    print("Good luck traveller! These lands are unsafe.. make sure to stock up on heals!")
    print("                                            ")
    print (name + " encounters an enemy...")
    ehealth = random.randint(50, 100)
    eattack = random.randint(10, 15)
    edefense = random.randint(2, 20 - eattack)


    #first battle
    print("Enemy #1 arrives!")
    while health > 0 and ehealth > 0:
        inputt = input("Do you wish to heal, attack or defend? ")
        
        if inputt == "attack" or inputt == "Attack":
            print(name + " attacks!")
            ehealth = ehealth - attack
            attackstat = attack + attack
            print("Enemy has " + str(ehealth) + " health left!")
            
            #enemy decidion
            edecidion = random.randint(1,2)
            if edecidion == 1:
                print("Enemy attacks!")
                health = health - eattack + defense
                print(name + " has " + str(health) + " health left!", end="\n\n")
            else:
                print("Enemy heals!")
                ehealth += edefense
                print("Enemy has " + str(ehealth) + " health left!", end="\n\n")

            
        elif inputt == "defend" or inputt == "Defend":
            print(name + " defends!")
            eattack -= 5
            
            #enemy decidion
            edecidion = random.randint(1,2)
            if edecidion == 1:
                print("Enemy attacks!")
                health = health - eattack + defense
                print(name + " has " + str(health) + " health left!", end="\n\n")
            else:
                print("Enemy heals!")
                ehealth += edefense
                print("Enemy has " + str(ehealth) + " health left!", end="\n\n")
            eattack += 5

            
        elif inputt == "heal" or inputt == "Heal":
            if timeshealed < 4:
                timeshealed += 1
                print(name + " heals!")
                heals = int(health/3)
                health += heals
                
                #enemy decidion
                edecidion = random.randint(1,2)
                if edecidion == 1:
                    print("Enemy attacks!")
                    health = health - eattack + defense
                    print(name + " has " + str(health) + " health left!", end="\n\n")
                else:
                    print("Enemy heals!")
                    ehealth += edefense
                    print("Enemy has " + str(ehealth) + " health left!", end="\n\n")
            else:
                print(name + " has run out of heals!")
            
        else:
            print(name + " was confused and didn't put in anything legible! Try again >:( ")
            

        if health > 0:
            average = average + 1
            if exp == 100:
                exp -= 100
                level += 1
                attack += 5
                health += 5
                defense += 5
                print("You have leveled up! You are now level " + str(level) + ".")
                if level > 1:
                    print("Your stats have incresed by 5.")
            elif exp < 100:
                exp += 50
        if health == 0:
            print ("The first battle has ended!")
            break

    #second battle
    print()
    print (name + " encounters an enemy...")
    ehealth = random.randint(50, 100)
    eattack = random.randint(10, 15)
    edefense = random.randint(2, 20 - eattack)
    print("Enemy #2 arrives!")
    
    while health > 0 and ehealth > 0:
        inputt = input("Do you wish to heal, attack or defend? ")
        
        if inputt == "attack" or inputt == "Attack":
            print(name + " attacks!")
            ehealth = ehealth - attack
            attackstat = attack + attack
            print("Enemy has " + str(ehealth) + " health left!")
            
            #enemy decidion
            edecidion = random.randint(1,2)
            if edecidion == 1:
                print("Enemy attacks!")
                health = health - eattack + defense
                print(name + " has " + str(health) + " health left!", end="\n\n")
            else:
                print("Enemy heals!")
                ehealth += edefense
                print("Enemy has " + str(ehealth) + " health left!", end="\n\n")
                
                
            
        elif inputt == "defend" or inputt == "Defend":
            print(name + " defends!")
            eattack -= 5
            print("Enemy has " + str(ehealth) + " health left!", end="\n\n")
            
            #enemy decidion
            edecidion = random.randint(1,2)
            if edecidion == 1:
                print("Enemy attacks!")
                health = health - eattack + defense
                print(name + " has " + str(health) + " health left!", end="\n\n")
            else:
                print("Enemy heals!")
                ehealth += edefense
                print("Enemy has " + str(ehealth) + " health left!", end="\n\n")
            
        elif inputt == "heal" or inputt == "Heal":
            if timeshealed < 4:
                timeshealed += 1
                print(name + " heals!")
                heals = int(health/3)
                health += heals
                
                #enemy decidion
                edecidion = random.randint(1,2)
                if edecidion == 1:
                    print("Enemy attacks!")
                    health = health - eattack + defense
                    print(name + " has " + str(health) + " health left!", end="\n\n")
                else:
                    print("Enemy heals!")
                    ehealth += edefense
                    print("Enemy has " + str(ehealth) + " health left!", end="\n\n")
            else:
                print(name + " has run out of heals!")
            
        else:
            print(name + " was confused and didn't put in anything legible! Try again >:( ")
            
            
        if health > 0:
            average = average + 1
            if exp >= 100:
                exp = 0
                level += 1
                attack += 5
                health += 5
                defense += 5
                print("You have leveled up! You are now level " + str(level) + ".")
                if level > 1:
                    print("Your stats have incresed by 5.")
            elif exp < 100:
                exp += 50
        if health == 0:
            print ("The second battle has ended!")
            break

    #third battle
    print()
    print (name + " encounters an enemy...")
    ehealth = random.randint(50, 100)
    eattack = random.randint(10, 15)
    edefense = random.randint(2, 20 - eattack)
    print("Enemy #3 arrives!")
    
    while health > 0 and ehealth > 0:
        inputt = input("Do you wish to attack, defend, or heal? ")
        
        if inputt == "attack" or inputt == "Attack":
            print(name + " attacks!")
            ehealth = ehealth - attack
            attackstat = attack + attack
            #enemy decidion
            edecidion = random.randint(1,2)
            if edecidion == 1:
                print("Enemy attacks!")
                health = health - eattack + defense
                print(name + " has " + str(health) + " health left!", end="\n\n")
            else:
                print("Enemy heals!")
                ehealth += edefense
                print("Enemy has " + str(ehealth) + " health left!", end="\n\n")

            
        elif inputt == "defend" or inputt == "Defend":
            print(name + " defends!")
            eattack -= 5
            
            #enemy decidion
            edecidion = random.randint(1,2)
            if edecidion == 1:
                print("Enemy attacks!")
                health = health - eattack + defense
                print(name + " has " + str(health) + " health left!", end="\n\n")
            else:
                print("Enemy heals!")
                ehealth += edefense
                print("Enemy has " + str(ehealth) + " health left!", end="\n\n")
            eattack += 5


        elif inputt == "heal" or inputt == "Heal":
            if timeshealed < 4:
                timeshealed += 1
                print(name + " heals!")
                heals = int(health/3)
                health += heals
                
                #enemy decidion
                edecidion = random.randint(1,2)
                if edecidion == 1:
                    print("Enemy attacks!")
                    health = health - eattack + defense
                    print(name + " has " + str(health) + " health left!", end="\n\n")
                else:
                    print("Enemy heals!")
                    ehealth += edefense
                    print("Enemy has " + str(ehealth) + " health left!", end="\n\n")
            else:
                print(name + " has run out of heals!")

        else:
            print(name + " was confused and didn't put in anything legible! Try again >:( ") 
            
        if health > 0:
            average = average + 1
            if exp >= 100:
                exp = 0
                level += 1
            elif exp < 100:
                exp += 50
                attack += 5
                health += 5
                defense += 5
                print("You have leveled up! You are now level " + str(level) + ".")
                if level > 1:
                    print("Your stats have incresed by 5.")
        if health == 0:
            print ("The third battle has ended!")
            break

    #final boss
    print()
    print (name + " encounters an enemy...They seem extra strong! And what is that music...?")
    healbefore = input("Would you like to heal before starting the battle? ")
    if healbefore == "yes" or healbefore == "Yes" or healbefore == "heal" or healbefore == "Heal":
        timeshealed += 1
        print(name + " heals!")
        heals = int(health/3)
        health += heals
        print("Good luck...hope your choice benifits you, traveller!")
    elif healbefore == "no" or healbefore == "No":
        print("Good luck...hope your choice benifits you, traveller!")
    else:
        print("You are going to have a bad time...")
        
    print()    
    print("SANS (final boss) arrives! (I thought this was DND? Where did he-) *cue MEGALOVANIA in the background*")

    while level < 2:
        ehealth = 300
        eattack = 40
        break
    while level >= 2:
        ehealth = 500
        eattack = 50
        break
    
    while health > 0 and ehealth > 0:
        inputt = input("Do you wish to attack, defend, or heal? ")
        
        if inputt == "attack" or inputt == "Attack":
            print(name + " attacks!")
            ehealth = ehealth - attack
            attackstat = attack + attack
            print("Sans has " + str(ehealth) + " health left!")
            print("Sans attacks with a gaster blaster!")
            health = health - eattack + defense
            print(name + " has " + str(health) + " health left!", end="\n\n")

        elif inputt == "defend" or inputt == "Defend":
            print(name + " defends!")
            eattack -= 5
            print("Sans has " + str(ehealth) + " health left!", end="\n\n")
            print("Sans attacks! His eye turns a fiery blue...")
            health = health - eattack + defense
            print(name + " has " + str(health) + " health left!", end="\n\n")
            eattack += 5

        elif inputt == "heal" or inputt == "Heal":
            if timeshealed < 4:
                timeshealed += 1
                print(name + " heals!")
                heals = int(health/3)
                health += heals
                print("Sans has " + str(ehealth) + " health left!")
                print("MEGALOVANIA plays louder! Sans chuckles and throws a bone at you")
                health = health - eattack + defense
                print(name + " has " + str(health) + " health left!", end="\n\n")
            else:
                print(name + " has run out of heals!")

        else:
            print(name + " was confused and didn't put in anything legible! Try again >:( ") 
            
        if health > 0:
            average = average + 1
            if exp >= 100:
                exp = 0
                level += 1
            elif exp < 100:
                exp += 50
                attack += 5
                health += 5
                defense += 5
                print("You have leveled up! You are now level " + str(level) + ".")
                if level > 1:
                    print("Your stats have incresed by 5.")
        if health == 0:
            print ("The third battle has ended!")
            break
        
    break


#end statements
if health > 0:
    print("You won!")
    print("You dealt " + str(attackstat) + " damage overall!" )
    if average / 4 == 1:
        print("You dealt an average of " + str(attackstat/3) + " each battle!", end="\n\n")

if health < 0:
    print("The enemy defeated you...")
    print(attackstat/3)
    if average / 4 == 1:
        print("You dealt an average of " + str(attackstat/4) + " each battle!")
    if average / 3 == 1:
        print("You dealt an average of " + str(attackstat/3) + " each battle!")
    if average / 2 == 1:
        print("You dealt an average of " + str(attackstat/2) + " each battle!")
    if average / 1 == 1:
        print("You dealt an average of " + str(attackstat/1) + " each battle!")