#Caleb Root for IT-140

#Dictionary nesting to create the rooms and items for the game
rooms = {
    'main hall':{'item':'LANTERN',
                 'WEST':'west ward hall',
                 'desc':'You find yourself in a strange dark corridor that seems to lead to many rooms. One, to the east, seems to have a strange sound coming from it. To the west, you see an ajar door leadng to another hall.\nWhat would you like to do?'
                 },
    'west ward hall':{'item' : 'CANDLE',
                    'EAST': 'main hall',
                    'desc':'Upon entering the hall you see '
                    },
    'migos room':{'item':'MI-GO WING',
                  'NORTH':'west ward hall'
                  },

}
#Global var declarations
congrats = 'Great job, you beat the game!'
pcRoom = rooms['main hall']
cardenal = ['NORTH','SOUTH','EAST','WEST']
options = ['QUIT','GET','Y', 'N']
pcItems = []
usrName = input('Please enter your player character''s name\n')
print('Welcome, {}, to my first game, HORROR HOTEL, a H.P. Lovecraft inspired text adventure game that runs in console. I hope that you will enjoy it.\n'.format(usrName))
#function for updating the player room
def updateRoom(direc):
    if direc in pcRoom:
        pcRoom == rooms[pcRoom[direc]]
        return pcRoom, print('working')
#function for looking
def find(item):
    if item in rooms[item]:
        look = print('You see a {}\n'.format(pcRoom.get('item')))
        return look, print('working')

#desc func
def desc():
    print(pcRoom.get('desc'))
#main game loop

while True:
    if pcItems == 6:
        print(congrats)
        exit()
    else:
        desc()                      #prints the description
        usrIn = str(input())        #gets user input for the command
        command = usrIn.capitalize()
    
        if command in cardenal:     
            updateRoom(command)
        elif command in options:
            pass
        elif command == 'LOOK':
            find(command)
        else:
            print('Sorry, I did not unterstand what you meant. Have you tried GET, LOOK, Y, N, QUIT, or a direction?\n' )