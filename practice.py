print("Welcome back to the Studio, Henry. You were called back by an old friend of yours. He has something to show you. \n")

print("CHAPTER ONE")
choice1 = input('You enter the studio and are met with an open room and a desolate hallway. Would you like to explore your surrondings? \n'
                'Type "yes" or "no". ').lower()
if choice1 == "no":
    print("The exit door is no longer behind you. You have no choice. GAME OVER.")
if choice1 == "yes":
    choice2 = input('You venture further and find a large, vast room labelled the Ink Machine. The entryway is boarded up with planks. \n'
                    'Type "approach" to take a closer look. '
                    'Type "leave" to leave. ').lower()
    if choice2 == "leave":
        print("You're stranded, genius. GAME OVER.")
    if choice2 == "approach":
        choice3 = input('Something lunges at you but is blocked by the planks. The hallways start flooding with ink. Run away? \n'
                        'Type "yes" or "no". ').lower()
        if choice3 == "no":
            print("The entity breaks through the planks and attacks, killing you instantly. GAME OVER.")
        if choice3 == "yes":
            choice4 = input('You escape its clutches and make a break for the exit. Unfortunately, the floor beneath you breaks and you fall beneath and into a pool of ink, slowing your movements. Explore? \n'
                            'Type "yes" or "no". ').lower()
            if choice4 == "no":
                print("The ink is getting higher and before long, it drowns you. GAME OVER.")
            if choice4 == "yes":
                choice5 = input('As you wade deeper into the inky depths, you come across a valve sticking out of a pipe in the wall. \n'
                                'Type "activate" to turn the valve. ' 
                                'Type "leave" to leave. ').lower()
                if choice5 == "leave":
                    print("The ink is getting higher and before long, it drowns you. GAME OVER.")
                if choice5 == "activate": 
                    
                    print("CHAPTER TWO")
                    choice6 = input('The valve drains the ink and you are able to move freely. You continue on your way and come acros the Music Department. The stairwell exit is flooded with ink. Continue? \n'
                                    'Type "yes" or "no". ').lower()
                    if choice6 == "no":
                        print("You're stranded, genius. GAME OVER.")
                    if choice6 == "yes":
                        choice7 = input('You look for a way to drain the stairwell and come across a Searcher. There is an axe lying on the ground next to you. \n'
                                        'Type "accept" to take the axe. '
                                        'Type "decline" to leave it alone. ').lower()
                        if choice7 == "decline":
                            print("... Why?")
                        if choice7 == "accept":
                            choice8 = input('You take the axe and successfully take down the Searcher. You spot a shadowy figure near the stairwell. Investigate? \n'
                                            'Type "yes" or "no". ').lower()
                            if choice8 == "no":
                                print("Smart decision.")
                            if choice8 == "yes":
                                choice9 = input('The shadowy figure turns out to be Sammy Lawrence. He takes your axe and attempts to sacrifice you to the Ink Demon. What do you do? \n'
                                                'Type "fight" to fight back. '
                                                'Type "flight" to run away. ').lower()
                                if choice9 == "fight":
                                    print("Sammy uses your axe against you and end up getting sacrificed. GAME OVER.")
                                if choice9 == "flight":
                                    choice10 = print('You run from Sammy and flee down a darkened hallway, losing him in the darkness. You make it to a saferoom but quickly realize you are not alone. ')








    







