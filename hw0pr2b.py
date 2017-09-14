# coding: utf-8
#
# hw0pr2b.py
#
# How to win: *name*, yes, time, yes, north, attack
# Small bug with exit loop will sometimes return to the "are you ready"
# question if other answers fail out. Going to office hours on Monday to try
# and resolve this. Thanks! Sorry it's long, I honestly think I misunderstood
# the level of commitment on this assignment.

""" 
Title for your adventure:   The Quest.

Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.

"""

import time

def adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    delay = 0.2          # change to 0.0 for testing/speed runs; larger for dramatic effect!

# Initialization Sequence
    print()
    print()
    print()
    print()
    print("               / \ ")
    print("              {   }")
    print("              p   !")
    print("              ; : ;")
    print("              | : |")
    print("              | : |")
    print("              l ; l")
    print("              l ; l")
    print("              I ; I")
    print("              I ; I")
    print("              I ; I")
    print("              I ; I")
    print("              d | b")	
    print("              H | H")
    print("              H | H")
    print("              H I H ")
    print("      ,;,     H I H    ,;,")
    print("     ;H@H;    ;_H_;,  ;H@H;")
    print("     \Y/d_,;|4H@HK|;,_b\Y/ ")
    print("      \;MMMMM$@@@$MMMMM;/ ")
    print("        ~~~*;!8@8!;*~~~ ")
    print("             ;888; ")
    print("             ;888; ")
    print("             ;888; ")
    print("             ;888; ")
    print("             d8@8b ")
    print("             O8@8O ")
    print("             T808T ")
    print("              `~` ")
    print()
    print()
    print('   W   E   L   C   O   M   E')
    print()
    print()
    print()
    print('               To ')
    print('        The ~first~ CS5          ')
    print('      T H U N D E R D O M E            ')
    print()
    print()
    print()
    print()
    print()
    username = input("What's your name, humble Grutor? ")

# Initial dialogue and control structure
    print()
    print()
    print('Welcome,', username, 'to the CS5 Thunderdome.')
    print('In this game, you will fight for your life.')
    print('Your stamina and ability will be pushed to the limit.')
    print()
    print("This is the most extreme text-based RPG in existence.")
    print()
# Opt-out scenario
    while True:
            status = input('Are you ready? ')
            if status == "yes":
                print('Onwords, to certain death')
                print()
                print()
                print()
                print("You awaken to a harsh buzzing sound. Everything seems hazy, yet you can sense light")
                print('is streaming through your blinds. You rub your eyes, and get out of bed.')
                print()
                print()
                print("Glancing at the clock, you realize the time is 8:05. 'CRAP', you scream into the abyss,")
                print("It takes 5 minutes to walk to Mudd, so there's no way you'll make it to CS5 in time.")
                print()
                print()
                #Defines the first choice
                choice1 = input("Do you take your time and accept being late, or do you sprint to class? [time/sprint] ")
                print()
                #The first path through the game
                if choice1 == "time":
                    print('')
                    print('')
                    print('You have made the wise decision. Groggily, you brush your teeth, comb your hair,')
                    print ('put on clothing, and make your way up to Mudd. ')
                    print('')
                    print('As you enter CS5, rather late, Prof. Dodds decides to put you on the spot.')
                    print(username, ', he calls out. Come up front, you\'ll be our PicoBot for today.')
                    print('Instantly, you freeze up. You\'ve always hated participating in class, and')
                    print('CS5 is big enough that you could easily dissapear into the crowd, never to be')
                    print('noticed again. On the other hand, this could be a great way to earn Dodds\'')
                    print('favor, and maybe even get an A over all.')
                    print('')
                    choice2 = input('Will you move up to the front and become PicoBot? [yes/no] ')
                    if choice2 == "yes":
                        print('')
                        print('')
                        print('')
                        print('You sheepishly walk to the front of the classroom. As you approach the preset maze,')
                        print('it becomes apparent that Dodds has set up a fairly intricate Picobot map. Another')
                        print('student is also up front, standing on one end of the map.')
                        print('')
                        print('Dodds has you stand on the opposite end of the map. Four paths diverge from where')
                        print('you are. One is labled N, the next E, then W, then S. You vaguely remember learning')
                        print('the cardinal directions for Picobot just a few classes prior. Dodds hands you a ')
                        print('plastic boffing sword.')
                        print('')
                        print('"This is just a test run!" he proclaims. The goal is to try and outmanuver your opponent')
                        print('and hopefully land the first (and last!) hit with your boffing sword. On your marks,')
                        print('')
                        print('')
                        print('get set. . .')
                        print('')
                        print('')
                        print('GO!')
                        print('')
                        print('')
                        print('You suddenly feel the clock racing against you, and tunnel vision enveloping your ')
                        print('conciousness. Your opponent takes a move, yet do to the setup of the chair maze, it\'s')
                        print('very hard to tell in what direction. It\'s your turn, and the stakes have never been')
                        print('higher. What will you do? You could follow a NEWS cardinal direction, or simply run')
                        print('from Dodds, straight to the registrar, and drop the class forever.')
                        print('')
                        print('')
                        choice3 = input('What do you choose? [north/east/west/south/run] ')
                        if choice3 == "north":
                            print('you step forward, deeper into the maze. Your opponent pushes towards your left.')
                            print('It\'s hard to see based on the small size of the Picobot tiles, yet, you think that')
                            print('there is a possible opening on the other side of him. ')
                            print('')
                            print('')
                            choice4 = input('What will you do? [attack/retreat/escape] ')
                            if choice4 == "attack":
                                print('')
                                print('')
                                print('You step forward to attack, swinging your triumphant boffing sword of CS5.')
                                print('Mightly, you land a hit. Your enemy falls to the ground, defeated forever.')
                                print('The seated students break into applause. Prof Dodds is stunned.')
                                print('')
                                print('')
                                print('Congratulations! You won an A in CS5.')
                                break

                            elif choice4 == "retreat":
                                print('')
                                print('')
                                print('You stumble backwards, only to hit a chair. You fly backwards, humiliating ')
                                print('yourself in front of all your classmates. Dodds laughed. You will never pass CS5.')
                                print('')
                                print('')
                                print('You lose,', username)
                                break
                            else:
                                print('')
                                print('')
                                print('Your attempts to leave this domain have been futile. Your opponent reaches his')
                                print('sword far above your head. All you can hope for is a pardon from Dodds.')
                                print('Maybe this would have been a good day to use those CS5 Euros.')
                                print('')
                                break
                        elif choice3 == "east":
                            print('')
                            print('')
                            print('You step east, towards the watching students. Sadly, you stumble over your own two')
                            print('feet, and fail to catch your balance. You plunge to immediate defeat.')
                            print('')
                            print('')
                            print('Better luck next time', username)
                            break
                        elif choice3 == "west":
                            print('')
                            print('')
                            print('You move towards the walls of Galileo hall, unsure what to do. Luckily, you seem')
                            print('to spot an opening. With the vengance of a million poorly compiled Picbots,')
                            print('you rush towards your opponent, knocking them off their feet.')
                            print('')
                            print('Congratulations', username, ', you have survived CS5.')
                            print('')
                            break
                        elif choice3 == "south":
                            print('')
                            print('')
                            print('You stumble backwards, only to hit a chair. You fly backwards, humiliating ')
                            print('yourself in front of all your classmates. Dodds laughed. You will never pass CS5.')
                            print('')
                            print('')
                            print('You lose,', username)
                            break
                        else:
                            print('')
                            print('')
                            print('Fight or flight kicks in, and your survival instincts cause you to flee CS5. You')
                            print('dash straight out of HMC, all the way to Avery Hall, and into the office of the')
                            print('registrar. CS5 may have defeated you, but luckily it\'s still add/drop.')
                            print('')
                            print('')
                            print('Better luck next time,', username)
                            print('')
                            print('')
                            break
                #First "death"    
                elif choice1 == "sprint":
                    print('')
                    print('')
                    print('You think fast, throw on some shoes, and sprint out the door. ')
                    print('Luckily, you arrive at HMC in time for class, but everybody seems to be looking')
                    print('at you funny. Confused, you head to the bathroom. As you stand in the mirror, you\'re')
                    print('horriffied to realize that you forgot to change out of your pajamas.')
                    print('')
                    print('')
                    print('You didn\'t survive the brutalities of CS5. Better luck next time.')
                    break
            else:
                break