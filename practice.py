print("Welcome back to the Studio, Henry. You were called back by an old friend of yours. He has something to show you. \n")

print("CHAPTER ONE - MOVING PICTURES")
choice1 = input('You enter the studio and come to a fork in the road; One hallway leads to the left while the other leads to the right. Which way do you go? \n'
                'Type "left" or "right". ').lower()
if choice1 == "left":
    print("You enter a room with animation desks galore, some with unfinished sketches. Your gaze lands on a specific desk and fills you with nostalgia. There is nothing for you here.")
if choice1 == "right":
    choice2 = input('You venture further and enter a room labelled the Ink Machine. There is a vast gap in the floor with a lever nearby, powered by a few dry cells. Pull lever? \n'
                    'Type "pull" to pull the lever. '
                    'Type "leave" to leave the room. ').lower()
    if choice2 == "leave":
        print("You decide to walk away and leave the studio behind. Safest option.")
    if choice2 == "pull":
        choice3 = input('The cavernous room rumbles before a large machine is lifted out of the abyss, strung up by a few chains. The machine needs ink to power. \n'
                        'Type "investigate" to leave the room. ').lower()
        if choice3 == "investigate":
            choice4 = input('You leave the Ink Machine room and find a room with a valve. There is a tape recording nearby. \n'
                            'Type "play" to review the tape recording. '
                            'Type "ignore" to ignore the tape recording. ').lower()
            if choice4 == "ignore":
                print("You ignore the recording and have no clue on what to do next.")
            if choice4 == "play":
                choice5 = input('The recording gives you insight on what you should do next by redirecting the ink flow. \n'
                                'Type "continue". ').lower()
                if choice5 == "continue":
                    choice6 = input('You walk a bit further and find the valve responsible for directing the ink flow to the Ink Machine. Turn valve? \n'
                                    'Type "yes" or "no". ').lower()
                    if choice6 == "no":
                        print("What was the point of finding the valve then?")
                    if choice6 == "yes":
                        choice7 = input('You make your way back to the Ink Machine. The doors are boarded up. Investigate? \n'
                                        'Type "yes" or "no": ').lower()
                        if choice7 == "no":
                            print("That was likely the smartest choice.")
                        if choice7 == "yes":
                            choice8 = input('Something lunges at you from behind the boards. The hallways flood with ink. Run? \n'
                                            'Type "yes" or "no". ').lower()
                            if choice8 == "no":
                                print("GAME OVER.")
                            if choice8 == "yes":
                                choice9 = input('You decide to make a break for the exit. The floor beneath you falls way, causing you to fall into a pool of ink below. Explore? \n'
                                                'Type "yes" or "no". ').lower()
                                if choice9 == "no":
                                    print("There's no going back.")
                                if choice9 == "yes":
                                    choice10 = input('You wade further through the ink and find a valve, lowering the ink around you. Keep moving? \n'
                                                    'Type "yes" or "no". ').lower()
                                    if choice10 == "no":
                                        print("What was the point of turning the valve then?")
                                    if choice10 == "yes":
                                        
                                        print("CHAPTER TWO - THE OLD SONG")
                                        choice11 = input('You stumble into a new location. A music department of sorts. There is an axe on the floor next to you. Take it? \n'
                                                        'Type "accept" to take the axe. '
                                                        'Type "decline" to leave it there. ').lower()
                                        if choice11 == "decline":
                                            print("What a foolish decision.")
                                        if choice11 == "accept":
                                            choice12 = input('You take the axe just as something emerges from the puddle of ink before you. It reaches up to pull you down with it. \n'
                                                             'Type "swing" to use your axe. ').lower()
                                            if choice12 == "swing":
                                                choice13 = input('You use your axe and it scares off the cowardly Searcher. There is a stairwell exit next to you. Leave the studio? \n'
                                                                 'Type "yes" or "no". ').lower()
                                            if choice13 == "yes":
                                                choice14 = input('The stairwell is flooded with more ink. You cannot leave yet. Go back? \n'
                                                                 'Type "back" to find a solution. ').lower()
                                                if choice14 == "back":
                                                    choice15 = input('Another Searcher appears before you just as you find a pipe with a missing part. Investigate? \n'
                                                                     'Type "investigate" to get a closer look. ').lower()
                                                    if choice15 == "investigate":
                                                        choice16 = input('The Searcher disappears into another puddle before you make contact with it. It is holding a valve handle that looks to fit the missing part of the pipe you found. \n'
                                                                         'Type "run" to go after it. ').lower()
                                                        if choice16 == "run":
                                                            choice17 = input('You follow the sounds of sloshing ink and find the Searcher. It is standing underneath a crate. What do you do? \n'
                                                                             'Type "drop" to drop a crate on the Searcher. '
                                                                             'Type "swing" to use your axe. ').lower()
                                                            if choice17 == "swing":
                                                                print("Swinging your axe scares the Searcher and it disappears once more. It is probobaly gone for this time ...")
                                                            if choice17 == "drop":
                                                                choice18 = input('You drop the crate on the Searcher, squiashing it. It drops the valve. \n'
                                                                                 'Would you like to turn back? ').lower()
                                                                if choice18 == "yes": 
                                                                    choice19 = input('You return to the pipe you found when something charges at you, swinging an axe of their own. \n'
                                                                                     'RUN. ').lower()
                                                                    if choice19 == "run":
                                                                        choice20 = input('You charge down a particularly dark hallway and see a safehouse up ahead. \n'
                                                                                         'Enter? '
                                                                                         'Type "yes" or "no". ').lower()
                                                                        if choice20 == "yes":
                                                                            
                                                                            print("CHAPTER THREE - RISE AND FALL")
                                                                            choice21 = input('You enter the safehouse and realize you are not alone. A sound is heard further into the room. \n'
                                                                                             'Check the source of the noise? '
                                                                                             'Type "yes" or "no". ').lower()
                                                                            if choice21 == "no":
                                                                                print("Then what?")
                                                                            if choice21 == "yes":
                                                                                choice22 = input('You go to check the noise and find your buddy, Boris, instead! \n '
                                                                                                'You are not alone anymore. Keep going forward? ').lower()
                                                                                if choice22 == "no":
                                                                                    print("You are still stuck in the studio but at least you have a friend now.")
                                                                                if choice22 == "yes":
                                                                                    choice23 = input('You and Boris decide to leave the safehouse and come to yet another fork in the road. The path is split into two, one labelled "The path of The Angel" and the other, "The path of The Demon". \n'
                                                                                                    'Which way do you two go? '
                                                                                                    'Type "left" or "right". ').lower()
                                                                                    if choice23 == "right":
                                                                                        print("The room is filled with ink. It's a dead end.")
                                                                                    if choice23 == "left":
                                                                                        choice24 = input('The Angel Path leads you to an elevator with an ominmous voice telling you to step on. \n'
                                                                                                        'Enter the elevator? ').lower()
                                                                                        if choice24 == "no":
                                                                                            print("Smart choice, but you have no choice.")
                                                                                        if choice24 == "enter": 
                                                                                            choice25 = input('You step onto the elevator and it  moves for you. The ominous voice returns to ask for a favor from you in exchange for your freedom. \n'
                                                                                                            'Boris seems uneasy. Do you accept these terms? '
                                                                                                            'Type "yes" or "no". ').lower()
                                                                                            if choice25 == "no":
                                                                                                print("The voice gets angry and before you know it, the elevator drops suddenly and the both of you fall to your deaths.")
                                                                                            if choice25 == "yes":
                                                                                                choice26 = input('The voice seems pleased with your answer and suggests that you collect two gruesome ingredients for her: The first is a heart. \n'
                                                                                                                'Boris is still uneasy about the voice. You still have a choice to make. '
                                                                                                                'Continue? ').lower()
                                                                                                if choice26 == "no":
                                                                                                    print("The voice gets angry and before you know it, the elevator drops suddenly and the both of you fall to your deaths.")
                                                                                                if choice26 == "continue":
                                                                                                    choice27 = input('The elevator stops on a large projector room and there is a heart beating on a crate in front of you. Something emerges from the shadows, blocking the path in front of you. \n'
                                                                                                                    'Boris is cowering in the elevator cart. '
                                                                                                                    'Type "swing" to use your axe. ').lower()
                                                                                                    if choice27 == "swing":
                                                                                                        choice28 = input('You swing your axe and the projector-headed monstrosity recedes back into the shadows with a shriek. You grab the heart and return to the elevator. \n'
                                                                                                                        'The elevator moves again and the voice returns. Hear the next request? ' 
                                                                                                                        'Type "yes" or "no". ').lower()
                                                                                                        if choice28 == "no":
                                                                                                            print("The voice gets angry and before you know it, the elevator drops suddenly and the both of you fall to your deaths.")
                                                                                                        if choice28 == "yes":
                                                                                                            choice29 = input('The voice is delighted with your cooperation and asks for the second ingredient she needs: Boris. \n'
                                                                                                                            'Boris is cowering in the elevator cart. Hand him over? '
                                                                                                                            'Type "yes" or "no". ').lower()
                                                                                                            if choice29 == "yes":
                                                                                                                print("You monster ...")
                                                                                                            if choice29 == "no":
                                                                                                                choice30 = input('The voice gets angry and before you know it, the elevator drops suddenly. The both of you fall into the depths. \n'
                                                                                                                                'You have a split second decision: There is a small ledge to hold onto. '
                                                                                                                                'Save Boris or save yourself? ').lower()
                                                                                                                if choice30 == "boris":
                                                                                                                    print("Yay :D")
                                                                                                                if choice30 == "yourself":

                                                                                                                    print("CHAPTER FOUR - COLASSAL WONDERS")
                                                                                                                    choice31 = input('You knock out on impact and wake up in a vast storage unit filled to the brim with unused carnival equipment. Boris is nowhere to be seen. \n'
                                                                                                                                    'Look for Boris? '
                                                                                                                                    'Type "yes" or "no". ').lower()
                                                                                                                    if choice31 == "no":
                                                                                                                        print("You monster ...")
                                                                                                                    if choice31 == "yes":
                                                                                                                        choice32 = input('The voice from before returns, claiming that she has Boris in the haunted house at the end of the unit. There is no power, preventing you from going inside. \n'
                                                                                                                                        'There is a certain switch you need to pull nearby. '
                                                                                                                                        'Pull switch? ').lower()
                                                                                                                        if choice32 == "pull":
                                                                                                                            choice33 = input('You pull the switch and enter another sector of the storage unit. The "Projectionist" from before has returned, now twice as disgruntled as before. \n'
                                                                                                                                            'There is another switch you need to pull. '
                                                                                                                                            'Type "run" to run past the Projectionist. '
                                                                                                                                            'Type "swing" to use your axe. ').lower()
                                                                                                                            if choice33 == "run":
                                                                                                                                print("It caught you. Why would you do that?")
                                                                                                                            if choice33 == "swing":
                                                                                                                                choice34 = input('You somehow managed to anger it even more and now it is chasing you. \n'
                                                                                                                                                'There is a place to hide up ahead. Hide? '
                                                                                                                                                'Type "hide" to hide. ').lower()
                                                                                                                                if choice34 == "no": 
                                                                                                                                    print("It caught you. Why did you do that?")
                                                                                                                                if choice34 == "hide":
                                                                                                                                    choice35 = input('You hid behind a cardboard standee and it manages to follow you. It reaches out to grab you ... \n'
                                                                                                                                                    'Type "hide" to stay put. '
                                                                                                                                                    'Type "run" to run away. ').lower()
                                                                                                                                    if choice35 == "run":
                                                                                                                                        print("It caught you. Why did you do that?")
                                                                                                                                    if choice35 == "hide":
                                                                                                                                        choice36 = input('You stayed where you were and something else attack the Projectionist instead. You step out of your hiding spot. \n' 
                                                                                                                                                        'The lever is still untouched. Pull switch? ').lower()
                                                                                                                                        if choice36 == "pull":
                                                                                                                                            choice37 = input('You are now able to enter haunted house from before. \n'
                                                                                                                                                            'Enter? ').lower()
                                                                                                                                            if choice37 == "no":
                                                                                                                                                print("What was the point of doing this?")
                                                                                                                                            if choice37 == "enter":
                                                                                                                                                choice38 = input('You enter the haunted house and enter a darkened ballroom. Boris is at the center of the room but he is larger, bulkier than before. He lunges to attack you. Fight back? \n'
                                                                                                                                                                'Type "run" to run from Boris. '
                                                                                                                                                                'Type "swing" to swing your axe. ').lower()
                                                                                                                                                if choice38 == "run":
                                                                                                                                                    choice39 = input('He lunges to attack you. Fight back? \n')
                                                                                                                                                if choice39 == "swing":
                                                                                                                                                    choice40 = input('You swing your axe at Boris and it kills him. Your axe, unfortunately, breaks. \n'
                                                                                                                                                                    'Afterwards you are approached by two figures, claiming to be your allies. Go with them? ' 
                                                                                                                                                                    'Type "yes" or "no". ').lower()
                                                                                                                                                    if choice40 == "no":
                                                                                                                                                        print("Well, that's awkward.")
                                                                                                                                                    if choice40 == "yes":

                                                                                                                                                        print("CHAPTER FIVE - THE LAST REEL")
                                                                                                                                                        choice41 = input('The figures you follow introduce themselves as Alice and Tom. \n'
                                                                                                                                                                        'They might have a way to help you leave. Trust them? ').lower()
                                                                                                                                                        if choice41 == "no":
                                                                                                                                                            print("Well, that's awkward.")
                                                                                                                                                        if choice41 == "yes":
                                                                                                                                                            choice42 = input('The three of you enter a makeshift harbor and something drops down on you from the shadows. It/s the same figure from the music department. \n'
                                                                                                                                                                            'He swings his axe at you once more.' 
                                                                                                                                                                            'Do you run? ').lower()
                                                                                                                                                            if choice42 == "no":
                                                                                                                                                                print("You can NOT fight an axe with your hands, dude.")
                                                                                                                                                            if choice42 == "yes":
                                                                                                                                                                choice43 = input('You end up tripping over your own feet and Sammy manages to corner you. \n'
                                                                                                                                                                                'Do you stay put? '
                                                                                                                                                                                'Type "yes" or "no". ').lower()
                                                                                                                                                                if choice43 == "no":
                                                                                                                                                                    choice44 = input('You stay in place and Tom sneaks up behind Sammy and takes him out. \n'
                                                                                                                                                                                    'Keep moving forward? '
                                                                                                                                                                                    'Type "yes" or "no". ').lower()
                                                                                                                                                                    if choice44 == "yes":
                                                                                                                                                                        choice45 = input('The three of you keep moving forward and you come to a vault. \n'
                                                                                                                                                                                        'Go inside? '
                                                                                                                                                                                        'Type "yes" or "no". ').lower()
                                                                                                                                                                        if choice45 == "yes":
                                                                                                                                                                            choice46 = input('You etner tha vault and find a reel inside of a box. You will need this later. \n'
                                                                                                                                                                                            'Take the reel? '
                                                                                                                                                                                            'Type "yes" or "no". ').lower()
                                                                                                                                                                            if choice46 == "yes":
                                                                                                                                                                                choice47 = input('You take the reel and venture into the deepest part of the studio. You encounter the ink machine again and there is an island of some sort underneath the flow of ink. \n'
                                                                                                                                                                                                'Would you like to leave? ').lower()
                                                                                                                                                                                if choice47 == "leave":
                                                                                                                                                                                    choice48 = input('You wade your way across and enter a throne room. with a projector on the seat. \n'
                                                                                                                                                                                                    'Type "continue" to investigate. ').lower()
                                                                                                                                                                                    if choice48 == "continue":
                                                                                                                                                                                        choice49 = input('Play the reel? \n'
                                                                                                                                                                                                        'Type "play" to the reel.').lower()
                                                                                                                                                                                        if choice49 == "play":
                                                                                                                                                                                            choice50 = input('You enter the studio and come to a fork in the road; One hallway leads to the left while the other leads to the right. Which way do you go? \n'
                                                                                                                                                                                                            'Type "left" or "right". ').lower()
                                                                                                                                                                                            if choice50 == "right":
                                                                                                                                                                                               print("GAME OVER")