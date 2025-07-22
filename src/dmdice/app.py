"""
Various DM assistance from dice
"""

import dmdice.func as func
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class DMDice(toga.App):
    def startup(self):

        main_box = toga.Box()

        leftContent = toga.Box(style=Pack(direction=COLUMN))

        leftContent.add(toga.Button(
            "5e Character",
            on_press=self.button1,
            style=Pack(margin=10)
        ))
        leftContent.add(toga.Button(
            "Dungeon Layout",
            on_press=self.button2,
            style=Pack(margin=10)
        ))
        leftContent.add(toga.Button(
            "Loot",
            on_press=self.button3,
            style=Pack(margin=10)
        ))
        leftContent.add(toga.Button(
            "Trap",
            on_press=self.button4,
            style=Pack(margin=10)
        ))
        leftContent.add(toga.Button(
            "NPC Disposition",
            on_press=self.button5,
            style=Pack(margin=10)
        ))
        leftContent.add(toga.Button(
            "Weather",
            on_press=self.button6,
            style=Pack(margin=10)
        ))
        leftContent.add(toga.Button(
            "Encounter",
            on_press=self.button7,
            style=Pack(margin=10)
        ))
        leftContent.add(toga.Button(
            "Fumble Melee",
            on_press=self.button8,
            style=Pack(margin=10)
        ))
        leftContent.add(toga.Button(
            "Fumble Bow",
            on_press=self.button9,
            style=Pack(margin=10)
        ))
        leftContent.add(toga.Button(
            "Fumble Thrown",
            on_press=self.button10,
            style=Pack(margin=10)
        ))

        rightContent = toga.Box(style=Pack(direction=COLUMN))
        
        rightContent.add(toga.Button(
            "General Crit",
            on_press=self.button11,
            style=Pack(margin=10)
        ))
        rightContent.add(toga.Button(
            "Arrow Crit",
            on_press=self.button12,
            style=Pack(margin=10)
        ))
        rightContent.add(toga.Button(
            "Bludgeoning Crit",
            on_press=self.button13,
            style=Pack(margin=10)
        ))
        rightContent.add(toga.Button(
            "Piercing Crit",
            on_press=self.button14,
            style=Pack(margin=10)
        ))
        rightContent.add(toga.Button(
            "Slashing Crit",
            on_press=self.button15,
            style=Pack(margin=10)
        ))
        rightContent.add(toga.Button(
            "Unarmed Crit",
            on_press=self.button16,
            style=Pack(margin=10)
        ))
        rightContent.add(toga.Button(
            "Vorpal Weapon Crit",
            on_press=self.button17,
            style=Pack(margin=10)
        ))
        rightContent.add(toga.Button(
            "Cursed Weapon Crit",
            on_press=self.button18,
            style=Pack(margin=10)
        ))
        rightContent.add(toga.Button(
            "PC Crit on Dragon",
            on_press=self.button19,
            style=Pack(margin=10)
        ))
        rightContent.add(toga.Button(
            "Dragon Crit on PC",
            on_press=self.button20,
            style=Pack(margin=10)
        ))

        leftContainer = toga.ScrollContainer(flex=1)
        leftContainer.content = leftContent

        rightContainer = toga.ScrollContainer(flex=1)
        rightContainer.content = rightContent

        split = toga.Box(style=Pack(direction=ROW))
        split.add(leftContainer)
        split.add(rightContainer)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = split
        self.main_window.show()


    def button1(self, widget):
        self.main_window.info_dialog("5e Character", func.fifthChar())
    
    def button2(self, widget):
        self.main_window.info_dialog("Dungeon Layout", func.dungeon())

    def button3(self, widget):
        self.main_window.info_dialog("Loot", func.loot())
        
    def button4(self, widget):
        self.main_window.info_dialog("Trap", func.trap())
        
    def button5(self, widget):
        self.main_window.info_dialog("NPC Disposition", func.disposition())
        
    def button6(self, widget):
        self.main_window.info_dialog("Weather", func.weather())
    
    def button7(self, widget):
        self.main_window.info_dialog("Encounter", func.encount())
        
    def button8(self, widget):
        self.main_window.info_dialog("Fumble Melee", func.fumble("m"))
        
    def button9(self, widget):
        self.main_window.info_dialog("Funmble Bow", func.fumble("b"))
        
    def button10(self, widget):
        self.main_window.info_dialog("Fumble Thrown", func.fumble("t"))
        
    def button11(self, widget):
        self.main_window.info_dialog("General Crit", func.critical())
        
    def button12(self, widget):
        self.main_window.info_dialog("Arrow Crit", func.extraCrit("a"))
        
    def button13(self, widget):
        self.main_window.info_dialog("Bludgeoning Crit", func.extraCrit("b"))
        
    def button14(self, widget):
        self.main_window.info_dialog("Piercieng Crit", func.extraCrit("p"))
        
    def button15(self, widget):
        self.main_window.info_dialog("Slashing Crit", func.extraCrit("s"))
        
    def button16(self, widget):
        self.main_window.info_dialog("Unarmed Crit", func.extraCrit("u"))
        
    def button17(self, widget):
        self.main_window.info_dialog("Vorpal Weapon Crit", func.extraCrit("v"))
        
    def button18(self, widget):
        self.main_window.info_dialog("Cursed Weapon Crit", func.extraCrit("c"))
        
    def button19(self, widget):
        self.main_window.info_dialog("Dragon Defending Crit", func.dragonAD(2))
        
    def button20(self, widget):
        self.main_window.info_dialog("Dragon Attacking Crit", func.dragonAD(1))
        

def main():
    return DMDice()
