import numpy as np

lvl = 1
exp = 0
nextlvl = 10
mploc = 1
potion = 1
kill = 0
combat = 0
campfire = 0
hp_id = 0
hp = ("Healthy.", "Tiny cuts.", "Deeper cuts.", "Huge cuts with lacerations.", "Collapsing.")
leavegm = 0

def commands():
    print("Controls.")
    print("(A)ttack (D)rink (C)ontrols (W)alk (I)nspect (F)lee (H)ero (L)eave.")
    menu() 

def hero():
    print('''{}
    Health: {}
    Level: {}
    Experience: {}
    Location: {}
    Potions left: {}
    Monsters Killed: {}
    '''
    .format(hName, hp[hp_id], lvl, exp, mploc, potion, kill))
    menu()

def leave():
    print("{} got out of the forest.".format(hName))
    exit()

def dice():
    global diRes
    diRes = np.random.randint(1, 7)

def deathHeroState():
    global hp_id
    if hp_id > 4:
        print('''Rest in Peace {}
        Level: {}
        Location: {}
        Potions left to scavengers: {}
        Monsters Defeated: {}
        '''.format(hName, lvl, mploc, potion, kill))
        exit()

def monsterAttack():
    global hp_id
    dice()
    if diRes < 5:
        print("{} dodged the attack.".format(hName))
    else:
        print("{} received the monster attack.".format(hName))
        hp_id = hp_id + 1
        deathHeroState()
    menu()

def evolveState():
    global exp, nextlvl, lvl
    if exp >= nextlvl:
        lvl = lvl + 1
        nextlvl = nextlvl + (1 + lvl) * 5
        print("{} feels stronger.".format(hName))

def heroAttack():
    global combat, kill, exp, mploc, lvl
    print("{} attacks the monster!".format(hName))
    dice()
    difficult=3 + lvl - mploc
    if diRes <= difficult or diRes == 1:
        print("{} killed the enemy.".format(hName))
        combat = 0
        kill = kill + 1
        exp = exp + (diRes % 4) + mploc
        evolveState()
    else:
        monsterAttack()

def attack():
    global combat
    if combat == 0:
        print("{} attacks the air, for no reason.".format(hName))
    else:
        dice()
        if diRes < 5:
            heroAttack()
        else:
            print("{} missed the attack".format(hName))
            monsterAttack()
    menu()

def drink():
    global potion, hp_id
    if potion > 0:
        print("{} drinks a potion and feels well.".format(hName))
        
        potion = potion - 1
        hp_id = 0
    else:
        print("{} looks for a potion, but founds none.".format(hName))
    menu()

def walk():
    global combat, campfire, potion
    if combat == 0:
        dice()
        if diRes > 4:
            print("{} found a monster.".format(hName))
            combat = 1
        elif diRes < 2:
            if campfire == 0:
                print("found a portal, you think about inspecting it.")
                campfire = 1
            else:
                print("found a potion.")
                potion = potion + 1
        else:
            print("{} walks among the forests, but found nothing.".format(hName))
    else:
        print("{} is fighting right now and can't explore.".format(hName))
    menu()

def inspect():
    global mploc, campfire
    if campfire == 1:
        print("{} enters the lit portal.".format(hName))
        mploc = mploc + 1
        campfire = 0
    else:
        print("{} can't find anything to inspect.".format(hName))
    menu()

def flee():
    global combat
    if combat == 1:
        dice()
        if diRes < 3:
            print("{} fleed the battle. pathetic.".format(hName))
            combat = 0
        else:
            print("{} tries to flee, but the enemy is persistent.".format(hName))
            monsterAttack()
    else:
        print("in a paranoia, you run deeper inside the forest.")
    menu()

def menu():
    opt = input(">{} awaits your command: ".format(hName))
    while True and leavegm == 0:
        if opt.lower() == "c":
            commands()

        elif opt.lower() == "h":
            hero()

        elif opt.lower() == "l":
            leave()

        elif opt.lower() == "a":
            attack()

        elif opt.lower() == "d":
            drink()

        elif opt.lower() == "i":
            inspect()

        elif opt.lower() == "w":
            walk()

        elif opt.lower() == "f":
            flee()

        elif opt.lower() == "roll a dice" or opt.lower() == "rad":
            for x in range(36):
                dice()
                print(diRes)
            menu()

        else:
            print("{} didn't understood your instruction... (Press C for Controls)".format(hName))
            menu()


def start():
    global hName
    print("A forest is seen, talls trees, little light, dark and cold")
    hName = input("but the hero is called upon humanity, and its name: ")
    menu()

start()