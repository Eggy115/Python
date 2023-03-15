from random import randint
try:
        print("\n================================================\n             RPG Character Generator\n================================================\n\n")
        text_file = open("names.txt", "r")
        lines = open('names.txt').read().splitlines()
        placefile = open("places.txt", "r")
        placefilelines = open('places.txt').read().splitlines()
        while(True):
                namelist = lines[randint(1,8842)]
                racelist = ["Human","Dwarf","Elf","Angel","Birdfolk","Centaur","Dark Elf","Demon","Dragon","Dracaenae","Dragonkin","Dryad","Ent","Gargoyle","Genie","Giant","Ghoul","Gnome","Goblin","Gorgon","Golem","Griffin","Half-Elf","Half-Orc","Hellhound","Hobbit","Hydra","Imp","Lizardfolk","Manticore","Minotaur","Mermaid","Naga","Raven","Nymph","Orc","Ogre","Satyr","Phoenix","Faun","Siren","Sphinx","Spiderfolk","Titan","Troll","Valkyrie","Vampire","Werewolf","Yeti"]
                parentlist = lines[randint(1,8842)]
                placelist = placefilelines[randint(1,10196)]
                gender = [" son of "," daughter of "]
                print("Name: " + namelist + gender[randint(0,1)] + parentlist + "\nPlace of Origin: " + placelist + "\nRace: " + racelist[randint(0,48)] + "\nHealth: " + str(randint(1,200)) + "\nAttack: " + str(randint(1,200)) + "\nDefence: " + str(randint(1,200)) + "\nSpeed: " + str(randint(1,200)) + "\nMagic: " + str(randint(1,200)) + "\n")           
                input()
        text_file.close()
        placefile.close()
except KeyboardInterrupt:
        print("")