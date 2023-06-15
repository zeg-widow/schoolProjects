#Caleb Root for IT-140

#Dictionary nesting to create the rooms and items for the game
rooms = {
    'Main Hall':{'item':'Lantern',
                 'West':'West Ward Hall',
                 'desc':'You find yourself in a strange dark corridor that seems to lead to many rooms. One, to the east, seems to have a strange sound coming from it. To the west, you see an ajar door leadng to another hall.\nWhat would you like to do?'
                 },
    'West ward Hall':{'item' : 'Candle',
                    'Main Hall': 'East',
                    'desc':'Upon entering the hall you see '
                    },
    'Migos Room':{'item':'Mi-Go Wing',
                  'North':'West Ward Hall'
                  },

}
#Global var declarations
playerRoom = rooms['']
directions = ['NORTH','SOUTH','EAST','WEST']
options = ['QUIT','GET','LOOK','Y', 'N']
playerItems = {}
look = print('You see a {}\n'.format(playerRoom.get('item')))
errorMSG = print('Sorry, I didn''t unterstand what you meant. Have you tried GET, LOOK, Y, N, QUIT, or a direction?')
death = False
prDesc = print(playerRoom.get('desc'))
usrName = input('Please enter your player character''s name\n')
#Main game loop happens while player is alive
while death != True:
    print('Welcome,{}, to my first game, HORROR HOTEL, a H.P. Lovecraft inspired text adventure game that runs in console. I hope that you will enjoy it.\n'.format(usrName))
    playerRoom = rooms['Main Hall']
    prDesc
    