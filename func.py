import dice
import random

def roll(num, sides):
    return random.randint(num, sides * num)

def throw(faces, sides):
    return faces[roll(1, sides) - 1]

def fifthChar():
    r = throw(dice.race, 12)
    c = throw(dice.occupation, 12)
    l = throw(dice.law, 3)
    g = throw(dice.good, 3)
    return f"How about a {l} {g}, {r} {c}?"

def dungeon():
    route = throw(dice.corridor, 6)
    if route == 'Door':
        doorState = throw(dice.door, 6)
        return f"The corridor is a {route} and it is {doorState}"
    return f"The corridor is {route}"

def loot():
    treasure = throw(dice.loot12, 12)
    if treasure == 'Chest':
        return f"{treasure}: {throw(dice.loot6, 6)} and {throw(dice.loot6, 6)}"
    elif treasure == 'Hoard':
        return f"{treasure}: {throw(dice.loot6, 6)}, and {throw(dice.loot6, 6)}, and {throw(dice.loot6, 6)}"
    elif treasure == 'Nothing':
        return treasure
    else:
        return f"{treasure}: {throw(dice.loot6, 6)}"
    
def critical():
    hit = throw(dice.crit, 12)
    if hit == "Location numbed" or hit == "Dismember" or hit == "Bone broken" or hit == "Weapon stuck":
        return f"{hit}: {throw(dice.highLow, 10)} {throw(dice.bipedLoc, 12)} for Biped or {throw(dice.quadLoc, 12)} for Quadruped"
    return hit
    
def weather():
    return throw(dice.weather, 10)

def disposition():
    return throw(dice.mood, 10)

def trap():
    type = throw(dice.trap6, 6)
    element = throw(dice.trap12, 12)
    return f"{element} {type}"

def encount():
    first = throw(dice.encounter10, 10)
    second = throw(dice.enounter12, 12)
    if second == 'No encounter':
        return second
    return f"A(n) {first} encounter of {second}"

def extraCrit(weapon):
    if weapon == "a":
        return throw(dice.arrowCrit, 12)
    elif weapon == "b":
        match roll(1, 4):
            case 1:
                return throw(dice.bludgArm, 12)
            case 2:
                return throw(dice.bludgHead, 12)
            case 3:
                return throw(dice.bludgLeg, 12)
            case 4:
                return throw(dice.bludgTorso, 12)
    elif weapon == "p":
        match roll(1, 4):
            case 1:
                return throw(dice.pierceArm, 12)
            case 2:
                return throw(dice.pierceHead, 12)
            case 3:
                return throw(dice.pierceLeg, 12)
            case 4:
                return throw(dice.pierceTorso, 12)
    elif weapon == "s":
        match roll(1, 4):
            case 1:
                return throw(dice.slashArm, 12)
            case 2:
                return throw(dice.slashHead, 12)
            case 3:
                return throw(dice.slashLeg, 12)
            case 4:
                return throw(dice.slashTorso, 12)
    elif weapon == "u":
        match roll(1, 2):
            case 1:
                return throw(dice.unarmedKick, 12)
            case 2:
                return throw(dice.unarmedPunch, 12)
    elif weapon == "v":
        return throw(dice.vorpal, 12)
    elif weapon == "c":
        return throw(dice.cursed, 12)
    
def dragonAD(ad):
    if ad == 1:
        return throw(dice.dragonAttacking, 12)
    elif ad == 2:
        return throw(dice.dragonDefending, 12)

def fumble(weapon):
    if weapon == "b":
        return throw(dice.fumbleBow, 12)
    elif weapon == "m":
        return throw(dice.fumbleMelee, 12)
    elif weapon == "t":
        return throw(dice.fumbleThrown, 12)