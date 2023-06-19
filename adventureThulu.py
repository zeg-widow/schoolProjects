#Caleb Root for IT-140

#Dictionary nesting to create the rooms and items for the game
rooms = {}

rooms['hall1'] = {
        'desc':'You find yourself in a dimmly lit room with three ways forward. one to the west, one the north, the other east.\n what would you like to do?',
        'item' : 'candle',
            'exits': {'WEST':'hall2',
            'NORTH':'villRoom',
            'EAST':'migoR'
        }
}
rooms['hall2'] = {
        'desc':'a room with a table in the center upon the table you find a match\nWhat would you like to do?',
        'item':'match',
        'exits' : {
            'EAST': 'hall1'
            }
                }
rooms['migoR'] = {
        'desc':'You see a dead Mi-Go! you should get some of its wing\nWhat would you like to do?',
        'item':'mi-go wing',
        'exits':{'WEST':'hall1',
                 'EAST':'necroRoom'
        }
}
rooms['necroRoom'] = {
        'desc':'you see many dead bodies. Perhaps one has something of use on it\nWhat would you like to do?',
        'item':'red hair',
        'exits':{'WEST':'migoR',
                 'EAST':'dungeon'
        }
}
rooms['villRoom'] = {
        'desc':'you have made it to the final chamber. the cultists have already started!\nThankfully, by combining all of the ingredients in the central culdron, you managed to stop the apocolypse'
}
rooms['dungeon'] = {
        'desc':'you find yourself in a dark dank place\nmaybe some of this moss is useful',
        'item':'moss',
        'exits':{
            'WEST':'necroRoom'
        }
}
####################################
#### funcs                      ####
def move(curRoom, cardenal):
    curRoom = pcRoom
    if cardenal in curRoom:
        curRoom = rooms[curRoom]['exits'][cardenal]
        return curRoom
### main loop                    ###
pcRoom = rooms['hall1']
direcs = ['NORTH','SOUTH','EAST','WEST']
playerInv = []
while True:
    print(pcRoom['desc'])
    choice = input().upper()
    if pcRoom == 'villRoom':
        if playerInv == ['red hair','mi-go wing','candle','match']:
            print('Congrats! you have bested the cultists.')
            exit()
        else:
            print('you lost!')
            exit()
    elif choice in direcs:
        move(pcRoom, choice)
        print(pcRoom['desc'])
    elif choice == 'GET':
        playerInv.append(pcRoom['item'])
        print('you now have: {playerInv}'.format)
    else:
        print('there was a problem')
