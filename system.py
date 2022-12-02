from omen import Omen
from breach import Breach
from chamber import Chamber
from kayo import Kayo
from sova import Sova

class System():

    def __init__(self):
        pass

    def run(self):
        agents = ""
        while(agents != 'q'):
            agents = input("enter agents (q to quit): ")
            agents.split(" \n\t")                           #validate input here (5 valid agents)
            print(agents)                                   #analyze team comp here