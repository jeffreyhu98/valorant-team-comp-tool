from agents.omen import Omen
from agents.breach import Breach
from agents.chamber import Chamber
from agents.kayo import Kayo
from agents.sova import Sova

'''
    Handles the text-based UI system (loops until the user quits the program)
'''
class System():

    def __init__(self):
        pass

    def run(self):
        agents = ""
        while(agents != 'q'):
            agents = input("enter agents (q to quit): ")
            agents.split(" \n\t")                           #validate input here (5 valid agents)
            print(agents)                                   #analyze team comp here