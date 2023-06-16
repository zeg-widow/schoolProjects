#Caleb Root for IT-140

#Dictionary nesting to create the rooms and items for the game
rooms = {
    'Main Hall':{'item':'Lantern',
                 'WEST':'West Ward Hall',
                 'desc':'You find yourself in a strange dark corridor that seems to lead to many rooms. One, to the east, seems to have a strange sound coming from it. To the west, you see an ajar door leadng to another hall.\nWhat would you like to do?'
                 },
    'West ward Hall':{'item' : 'Candle',
                    'EAST': 'Main Hall',
                    'desc':'Upon entering the hall you see '
                    },
    'Migos Room':{'item':'Mi-Go Wing',
                  'NORTH':'West Ward Hall'
                  },

}
#Global var declarations
pcRoom = rooms['Main Hall']
cardenal = ['NORTH','SOUTH','EAST','WEST']
options = ['QUIT','GET','LOOK','Y', 'N']
pcItems = []
##  errorMSG = print('Sorry, I didn''t unterstand what you meant. Have you tried GET, LOOK, Y, N, QUIT, or a direction?')
death = False
usrName = input('Please enter your player character''s name\n')
print('Welcome, {}, to my first game, HORROR HOTEL, a H.P. Lovecraft inspired text adventure game that runs in console. I hope that you will enjoy it.\n'.format(usrName))
#function for updating the player room
def updateRoom():
    pcIn = input().upper()
    newRoom = pcRoom
    if pcIn in cardenal:
        for pcIn in rooms:
            newRoom == rooms[pcIn]
            return newRoom
#function for looking
def find(item):
    look = print('You see a {}\n'.format(pcRoom.get('item')))

#desc func
def desc():
    print(pcRoom.get('desc'))
#main game loop

while death != True:
    desc()
    updateRoom()