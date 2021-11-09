from sys import exit
from random import randint
from textwrap import dedent
import time
winning = False

class Scene(object):
    def enter(self):
        print("Scene not configured. Try again later")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Preamble(Scene):
    def enter(self):

        print(dedent("""
        Ages ago when dragons still flew, the mighty drake Icefire was entombed
        in a glacier by a spell.
        It has been 300 years. The queen dragon Taglia flies again but as the last
        of her kind, when she dies, dragons will once again fall into entinction.

        You are on a quest to free the last male dragon from his icy prison, in
        hopes of saving these majestic creatures from eternal extinction.

        It was an arduous journey, but you traveled to the glacier covered island
        where Icefire is trapped. But it is also, you discover, the lair of the
        mysterious Pale Woman-- the very one whose spell entombed Icefire all those
        ages ago!

        Her lair is cut into the glacier its self, and immeshes with ruins of a
        building built by the dragon worshiping ancients. You have disovered a way
        in, and have set your heart to freeing the dragon.
        """))
        time.sleep(1.0)
        return 'maze'

class Maze(Scene):
    def enter(self):

        print(dedent("""
        Carefully, you sneak into the Pale Woman's icy refuge. It looks as though
        the glacier has overtaken a palace built by the ancient ones. As you walk
        down the corridor, you see the occasional door, frozen over and stuck.
        At the end of the corridor, you can turn either left or right.
        """))

        print("Which way do you go?")

        turn_1 = input().lower()

        if turn_1 == 'left':
            print(dedent("""
                All the doors you see are frozen shut. One is open, just a crack
                and when you look in you are shocked to see human remains!
                Carefully you keep walking until you reach the end of the
                hallway.

                You round the corner and are spotted by the Pale Womans mercenaries!
                Valiantly, you fight but they overcome you.
                You die cold, in the icy corridors knowing dragons will never
                grace the skies again.
                """))

            return 'finished'

        elif turn_1 == 'right':
            return 'lab'

        else:
            print("Didn't catch that. Left or right?\n")

        time.sleep(1.0)
        return 'maze'
        # return 'elegant_chamber'
    # Dead End, Door
class ElegantChamber(Scene):
    def enter(self):

        print("I know this is not the problem.")

        return 'throne_room'
class Lab(Scene):
    def enter(self):

        print(dedent("""
        You check 3 doors on your walk. One of them, you barely
        manage to shoulder open. Looking through the crack, you see such wanton
        destruction and, disgustingly, what looks like human excrement polluting
        a once graceful room. You are approaching the corner and what looks Like
        a well maintained door! There's signs of a person entering and leaving...
        You decide to investigate. Carefully, you ease the door open and confirm
        the room is currently empty. You ease your way in and close the door
        behind you. You are in, what looks to be, a chamber for alchemical study.

        The room is lined with overflowing shelves-- scrolls, books, sheafs
        of papers are scattered everywhere. In amongst the clutter are some
        interesting looking items.

        """))

        print("Should you risk the time and search? >")

        choice_1 = input().lower()
        passed = ['yes', 'inspect', 'look']

        if any (x in choice_1 for x in passed ):
            print(dedent("""
                Descriptive writing, but you end up being able to steal a few
                items from here. You can take 2 items. Your choices are:

                    ice axe
                    vial of red liquid
                    vial of green liquid
                    jeweled sword
                    unusal arm bracers
                    explosives
                    interesting scroll
                    ruby encrusted crown

                    Which 2 do you choose? >
                """))

            choice_2 = input().lower()
            win = ['explosives', 'explosive', 'bomb']

            if any (x in choice_2 for x in win):
                global winning
                winning = True
                print(dedent("""
                Great selections. Now prepare to move on.\n
                """))

            else:
                print("Loot in hand, you leave. \n")

        return 'throne_room'
        time.sleep(1.0)

class ThroneRoom(Scene):
    def enter(self):
        print(dedent("""
        Descritive text, she attacks you with a ice blast.
        """))
    
        return 'boss_fight'

class BossFight(Scene):
    def enter(self):

        health = 4

        while health >= 0:
            iceblast = randint(1,20)
            health -= 1

            if iceblast == 20:
                print("She crits you and you die.")
                health -= 4
                return 'finished'

            elif iceblast < 20 and iceblast > 1:
                print("She hurls an ice blast at you and you take damage!\n")
                time.sleep(1.5)

            else:
                print("She botches and kills herself. Proceed to the dragon. ")
                return 'dragon'

        print(dedent("""
        You have survived her attacks! You have throwing knives
        with instant poison on them-- all you need is one of your 5 knives to
        hit her, and she'll be dead and you can free Icefire! So close!
        """))

        return 'hero_fight'

class HeroFight(Scene):
    def enter(self):
        # throw 5 knives, if one hits with a 10 or better you kill her.
        knives = 4

        if knives >= 0:
            throw = randint(1,20)
            knives -= 1

            if throw == 1:
                print(dedent("""
                In the process of throwing,  you trip and fall and
                impale yourself. You die, you damn clutz.
                """))

                return 'finished'

            elif throw <10:
                print("try again")
                time.sleep(1.5)

            else:
                print(f"{throw}")
                print("You got her! She dies and you go free Icefire.")
                return 'dragon'

        print("You go go grab the next set of knives, and she takes this time to attack!")
        return 'boss_fight'

class Dragon(Scene):
    def enter(self):

        print(dedent("""
        dragon scene, describe Icefire trapped in the glacier
        """))
        if winning == True:
            print("Win")
            return 'finished'

        else:
            print(dedent("""
            You have no means of opening the glacier. No explosives, no hammer.
            While you hack away at the ice with your sword, the Pale Woman's surviving
            minions find you and kill you.
            """))
            return 'finished'


class Finished(Scene):
    def enter(self):
        print(dedent("""
        exit game
        """))

        exit()


class Map(object):

    scenes = {
        'preamble': Preamble(),
        'maze': Maze(),
        'elegant_chamber': ElegantChamber(),
        'lab': Lab(),
        'throne_room': ThroneRoom(),
        'boss_fight': BossFight(),
        'hero_fight': HeroFight(),
        'dragon': Dragon(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('preamble')
a_game = Engine(a_map)
a_game.play()
