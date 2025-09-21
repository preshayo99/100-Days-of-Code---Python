
print('''
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___| 
 _     _                 _
(_)   | |               | |
 _ ___| | __ _ _ __   __| |
| / __| |/ _` | '_ \ / _` |
| \__ \ | (_| | | | | (_| |
|_|___/_|\__,_|_| |_|\__,_|
                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \ 
                                                   .       .             
                       
                      'Xx xX*,
                ,*xXXx_xXx    \ 
                   _xXXXXXxx*,
                ,*XXx@x@Xx
                     X @|@@ `x       
                   /'  ||    '\ 
                       ||
                       ||
                       ||
                       ||
                 /ssssssss.
             /sssssssSSSSssssssssss.
            /sssssSSSSSSSSSSSSSSSssssssssssss.              
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~''')

print('''\nWELCOME TO TREASURE ISLAND ADVENTURER!!\n
Your mission is simple...(Press enter)''') 
run = input()

print('Find the treasure if you dare!! (Press enter)')
run = input()

first_choice = input('The path splits into two. Do you go left or right?: ').lower()
if first_choice == 'left':
    print('Wise choice. The path grows darker, and you hear the sound of rushing water ahead.')
    
    second_choice = input('\nA wide river blocks your way. Do you swim across or wait?: ' ).lower()
    if second_choice == 'wait':
        print('Patience pays off. A wooden raft drifts toward you. You climb aboard and float safely to the other side.')
        
        third_choice = input('\nAhead stands a grand castle with three massive doors—one red, one blue, one yellow. Which do you choose?: ').lower()
       
        if third_choice == 'red':
            print('Flames erupt the moment you enter! 🔥 You’re consumed by fire...GAME OVER\n')
        elif third_choice == 'blue':
            print('You hear growls echoing in the dark. Suddenly fangs appear! 🐺 Werewolves surround you...You never stood a chance...GAME OVER\n')
        elif third_choice != 'yellow':
            print('That’s… not a door. You wander aimlessly and are never seen again. GAME OVER\n')
        else:
            print('''\nThe door creaks open...sunlight floods in. Before you lies a glittering chest overflowing with gold and jewels! 💎✨
                                        Congratulations, adventurer—you’ve found the treasure! 
                                                            🎉You Win! 🎉\n''')
    
    else:print('\nA swarm of giant trout drags you under...you drown. GAME OVER\n')
else:
    print('The ground crumbles beneath you—ahhh! You’ve fallen into a bottomless pit.GAME OVER\n')