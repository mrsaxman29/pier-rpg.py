import random
import time
import sys
from playsound import playsound
import AppKit
from colorama import Fore, Back, Style

# print(Fore.RED + "TEST ETSTTS")
# print(Fore.BLACK)
# above are how to change text color and revert color


badwords = open("badwords.txt", "r")
content = badwords.read()

"""
NOTES:

Add cooldown period to items - determind by how many rooms or other items used

Item class should have paramater for description of what happens when in use


"""
world = {}
run = True
directs = ["N", "S", "E", "W"]
count = 0

def print_slow(str):
    for letter in str:
        j = random.randrange(1, 17) # second value should be ~100
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(j/1000)

def print_very_slow(str):
    for letter in str:
        j = random.randrange(1, 700)
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(j/10000)


class item:
    def __init__(self, name, desc, value):   #add another parameter that describes the use of the item
        self.name = name
        self. desc = desc
        self.value = value
        self.ready = True

    def __str__(self):
        return str(self.desc)

    def use(self):
        eee = phil.inventory[0]
        if eee.ready:
            print_slow("You used the " + self.name + ".")
            print()
            print(Fore.GREEN, "\nYou're score increased by " + str(self.value))
            print()
            phil.score += self.value
            score = phil.score
            print("You have " + str(score) + " points")
            self.ready = False
            print(Fore.BLACK)
            playsound("bell.mp3")
        else:
            print("\nYou just did that.  Why not do something else?")
            playsound("badbell.mp3")


class room:
    def __init__(self, name, desc, items, exits, people, list):  # make list in objects list to display of whats in room
        self.name = name
        self.desc = desc
        self.items = items
        self.exits = exits
        self.people = people
        self.list = list

    def __str__(self):
        return str(self.desc)

class player:
    def __init__(self, name, desc, room):
        self.name = name
        self.desc = desc
        self.maxscore = 100
        self.score = 0
        self.chat = 10
        self.inventory = []
        self.room = room

    def move(self, direction):
        global x
        global y
        self.direction = direction
        x = world[phil.room].exits
        y = x[direction]

    def question(self):
        if world[phil.room].people.name == "sir":   ## INTERESTING CODE  calls value in dictionary based on player's room attribute.  The value of that key is a function whose attribute name is accessed "people" 'room.people ' whose value is another function (player) whose parameter 'name' is accessed.
            ww = random.choice(scam_list)
            print()
            print_very_slow(ww)
            print()
        elif world[phil.room].people.name == "nathalie":
            ww = random.choice(nathalie_questions)
            print()
            print_very_slow(ww)
            print()
        elif world[phil.room].people.name == "charles":
            ww = random.choice(charles_questions)
            print()
            print_very_slow(ww)
            print()
        else:
            oo = random.choice(question_list)
            print()
            print_very_slow(oo)
            print()

    def talk(self, name):
        self.name = name
        # uu = world[phil.room].people.name     reference uu in string to customize query
        print_slow("Do you need any help?\n")
        gg = world[phil.room].people
        gg.question()
        print()
        ll = input("type your response:")
        # if any seperate word in string
        pp = ll.split(" ")
        print()
        if any(item in content for item in pp) == True:
            print("What did you just say to me!?")
            print("\n~They look pissed~\n")
            phil.score -= 10
            print(Fore.GREEN, "Your score is: " + str(phil.score))
            print(Fore.BLACK)
            playsound("badbell.mp3")
        else:
            print("~They look pleased with you and say 'Thanks'\n")
            phil.score += 15
            yyy = phil.score
            print("Your score has increased by 15 points! \n Your score is: " + str(yyy))
            playsound("bell.mp3")

    def __str__(self):
        return self.desc


class Game:
    def __init__(self):
            start = input(intro.desc)
            if start == "":
                global run
                global count
                while run:
                    count += 1
                    if count % 9 == True:           #adjust this number for length of reset on items (in # of actions)
                        for item in all_items:
                            item.ready = True
                    if count % 3 == True:
                        global aaa
                        global bbb
                        global ccc
                        global ddd
                        global eee
                        global fff
                        global ggg
                        aaa = random.choice(customer_rooms)
                        bbb = random.choice(customer_rooms)
                        ccc = random.choice(customer_rooms)
                        ddd = random.choice(staff_rooms)
                        eee = random.choice(staff_rooms)
                        fff = random.choice(staff_rooms)
                        ggg = random.choice(staff_rooms)
                        world[bbb].people = sir
                        world[aaa].people = customer
                        world[ccc].people = customer2
                        world[ddd].people = charles
                        world[eee].people = nick
                        world[fff].people = mark
                        world[ggg].people = nathalie
                        world[nick.room].people = ghost
                        world[sir.room].people = ghost
                        world[customer.room].people = ghost
                        world[customer2.room].people = ghost
                        world[charles.room].people = ghost
                        world[mark.room].people = ghost
                        world[nathalie.room].people = ghost
                        nick.room = eee
                        mark.room = fff
                        sir.room = bbb
                        customer.room = aaa
                        customer2.room = ccc
                        charles.room = ddd
                        nathalie.room = ggg

                    """print(charles.room)
                    print(nick.room)
                    print(nathalie.room)
                    print(mark.room)"""
                    print()
                    text = world[phil.room]
                    print_slow(text.desc)
                    print()
                    print(Fore.BLUE, "\nThere are exits:")
                    print(Fore.CYAN)
                    print(world[phil.room].exits)
                    print(Fore.BLUE)
                    choice = input("(l)ook around (p)ick up (u)se (i)nventory (t)alk (n)orth (s)outh (e)ast (w)est:  ")
                    print(Fore.BLACK)
                    doors = world[phil.room].exits

                    if choice.upper() == "L":
                        if world[phil.room].items:
                            print("In the " + world[phil.room].name + " you see:")
                            print(Fore.CYAN)
                            bb = world[phil.room].people
                            kk = world[phil.room].items  #instead do list.  for item in world[phil.room].items: slow_print(item)
                            if bb != None:
                                print_slow(str(bb))
                                print("\n")
                            print_slow(str(kk))
                            print(Fore.BLACK)
                              #Fix print of no people when looking (if statement)
                            #print(customer.room)
                            #print(sir.room)
                        else:
                            print_slow("\nYou don't see anything out of the ordinary.\n")

                    elif choice.upper() in doors:
                        if choice.upper() == "N":
                            print_slow("moving north............\n")
                        elif choice.upper() == "S":
                            print_slow("moving south............\n")
                        elif choice.upper() == "E":
                            print_slow("moving east............\n")
                        elif choice.upper() == "W":
                            print_slow("moving west............\n")
                        phil.move(choice.upper())
                        phil.room = y
                        playsound("walk.wav")

                    elif choice.upper() not in doors and choice.upper() in directs:
                        print("You can't go that direction.")

                    elif choice.upper() == "P":
                        if world[phil.room].items == None:
                            print_slow("There's nothing here to pick up. \n")

                        elif len(phil.inventory) > 0:
                            rrr = world[phil.room].items
                            phil.inventory.append(world[phil.room].items)
                            world[phil.room].items = phil.inventory[0]
                            temp = str(phil.inventory[0])
                            print_slow("You dropped: \n\n" + temp)
                            print_slow("\nAnd picked up a " + str(rrr))
                            print()
                            del phil.inventory[0]

                        else:     #Make these: for item in world[phil.room].items: phil.inventory.append(item)
                            phil.inventory.append(world[phil.room].items)
                            print_slow("You picked up a " + world[phil.room].items.name +".\n")
                            world[phil.room].items = None

                        if isinstance(phil.inventory[0], player):
                            print_slow("The customer struggles to get away from you and runs out the door.\nThe police are on their way.")
                            run = False

                    elif choice.upper() == "T":
                        if world[phil.room].people:
                            phil.talk(world[phil.room].people)
                        else:
                            print_slow("You're talking to yourself; no one is here.\n")
                        # something here to trigger a chat with customer and unique input as repsonse

                    elif choice.upper() == "I":
                        if len(phil.inventory) > 0:
                            print(Fore.BLUE, "\nYou are holding: \n")
                            print(Fore.BLACK)
                            l = len(phil.inventory)
                            for x in range(l):
                                print(phil.inventory[x])

                        else:
                            print_slow("You aren't carrying anything.\n")

                    elif choice.upper() == "U":
                        if len(phil.inventory) > 0:
                            if phil.inventory[0] != wallet:
                                phil.inventory[0].use()
                            elif phil.inventory[0] == wallet:
                                print_very_slow("You add Robbin's credit card info to your bot.\n")
                                phil.score -= 10
                                print(Fore.GREEN, "Your score is: " + str(phil.score))
                                print(Fore.BLACK)
                                playsound("badbell.mp3")
                                wallet.ready = False
                        else:
                            print_slow("You aren't carrying anything.\n")

                    if phil.score >= 100:
                        run = False
                        print_slow("YOU WIN - YOU ARE A PIER WINES MASTER - YOU WIN")
                        break

                else:
                    print_slow("You're banned from Pier Wines like Chris\n.....GAME OVER......\n")

            else:
                print("Please Restart Game")  # while loop ???


ghost = player("No one is here.", "No one is here", "")

phil = player("Phil", "A friendly employee and fiance.", "stockroom")
sir = player("sir", "A young buck with shiffty eyes.", "street")
customer = player("Robbin", "Robbin Ross: a grey streaked bougie white mom.", "store")
customer2 = player("Mr. Ortega", "Mr. Ortega: a large man with questionable employment.", "nowhere1")
charles = player("Charles Henery Starke II", "A top heavy doctor with hair that's never the same color as yesterday. He co-owns Pier Wines and pops in usually when he needs booze.", "nowhere3" )
nick = player("nick", "A young sales rep from Long Island", "nowhere4")
mark = player("mark", "Mark's last name is still unknown after a decade but it definitley ends in a vowel. Mark is a goomba and is the 'mayor' of Williamsburg. If you need something, Mark's got it.", "nowhere5")
nathalie = player("nathalie", "A cute asian-australian girl with high waisted pants is on her computer doing homework.","intro" )


broom = item("broom", "A Broom: A long pole with bristles at one end used for sweeping the floor.", 10)
mop = item("mop", "A Mop: A long plastic pole with a frayed head at the bottom used for cleaning the floor", 15)
package = item("package", "A small brown box addressed to Amanda Roberts", 5)
wallet = item("wallet", "A blue leather wallet with smooth finish. Inside are credit cards with the name Robin Ross", 5)
chairs = item("chairs", "Two metal planked chairs.", 5)
glasses = item("glasses", "Various glass ware of questionable size, shape and condition.", 10)
bottles = item("bottles", "Shiny glass wine bottles of assorted juices.", 5)

nowhere1 = room("nowhere1", "not anywhere", None, {}, customer2, [])
nowhere2 = room("nowhere2", "not anywhere", None, {}, None, [])
nowhere3 = room("nowhere3", "not anywhere", None, {}, charles, [])
nowhere4 = room("nowhere4", "not anywhere", None, {}, nick, [])
nowhere5 = room("nowhere5", "not anywhere", None, {}, mark, [])

intro = room("intro", "Press ENTER to start the game", None, {}, None, [])
bodega = room("bodega", "Inside the bodega there are random snacks, drinks and other products everywhere.", None, {"W": "street"}, None, [])
stockroom = room("stockroom", "You're in the STOCK ROOM. It's filled with various boxes and supplies for the store.", broom, {"E": "bathroom", "W": "desk"}, None, [])
bathroom = room("bathroom", "You are in a small BATHROOM with poorly painted white walls", mop, {"W": "stockroom"}, None, [])
desk = room("desk", "You see a DESK, some corkboards, a filing cabinet and chairs", package, {"E": "stockroom", "N": "register"}, None, [])
register = room("register", "An L-shaped counter with cash drawer, credit card machine and monitor is in front of you", wallet, {"E": "store", "S": "desk", "N": "door"}, None, [])
door = room("door", "A glass door", None, {"N": "street", "S": "store"}, None, [])
street = room("street", "The sidewalk in front of the store is covered by a black awning. \nThere is smeared dog poop on the sidewalk not far away.", chairs, {"S": "door", "E": "bodega"}, sir, [])
store = room("store", "The main selling floor is covered by bins filled with wine. \nAlong the wall shelves with neatly stacked bottles cover the far side of the store.", bottles, {"S": "bar", "W": "register", "N": "door"}, customer, [])
bar = room("bar", "A high counter covered in aluminium abutting a purple wall with port hole windows is across the room from the door.  \nBlack letter blocks with silver letters spell out PIER WINES", glasses, {"N": "store", "W": "desk"}, None, [])

world["intro"] = intro
world["stockroom"] = stockroom
world["bathroom"] = bathroom
world["desk"] = desk
world["register"] = register
world["door"] = door
world["street"] = street
world["store"] = store
world["bar"] = bar
world["bodega"] = bodega
world["nowhere1"] = nowhere1
world["nowhere2"] = nowhere2
world["nowhere3"] = nowhere3
world["nowhere4"] = nowhere4
world["nowhere5"] = nowhere5

question_list = ["Do you have orange wine?", "Do you have AIR Vodka?", "Do you have this chilled?", "Can I please use your bathroom?", "Can I get what I had last time?", "I had a wine on vacation six years ago in Malta that started with a P. Do you know what I'm talking about?", "Is this dry?", "What time do you close?", "Can I get a discount?", "Do you sell beer?"]
scam_list = ["Yo. Do you have Henny?", "What's up boss.  Do you guys have large Patron?", "Ey Pa.  You guys have Ciroc?", "Yo my man, do you take Kinch?"]
nathalie_questions = ["Have you seen my vape pen?", "Can I ask you some questions for my project?", "Did you see that episode of 90 Day Fiance with Eric-ie?  He's my favorite.", "I forget my keys...", "Where's Danny"]
charles_questions = ["How much money is in the safe?", "Do we have any good Amarones?", "What are you doing later for dinner?", "I love Trump. I think he owns the Fed; that little fa&!@t Bernake isn't s*$^."]
# make a few more lists of questions (for all non cusomter npcs - charles - nathalie - mark - nick


customer_rooms = ["nowhere1", "nowhere2", "bathroom", "street", "register", "bar", "store", "door", "bodega", "nowhere3", "nowhere4", "nowhere5",]
staff_rooms = ["bathroom", "street", "register", "bar", "store", "door", "bodega", "stockroom", "desk", "nowhere1", "nowhere2"]


all_items = [broom, mop, glasses, bottles, wallet, chairs, package]

thegame = Game()





