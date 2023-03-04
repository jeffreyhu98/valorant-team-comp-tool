from agents.omen import Omen
from agents.breach import Breach
from agents.chamber import Chamber
from agents.kayo import Kayo
from agents.sova import Sova
from agents.viper import Viper
from agents.reyna import Reyna
from agents.fade import Fade

valid_agents = ["omen", "breach", "chamber", "kayo", "sova", "viper", "reyna", "fade"]

''' 
    an empty dict to use as a template
'''
info_template = {
    "role": "", 
    "smoke": "", 
    "trip": "", 
    "soft recon": "", 
    "hard recon": "",
    "drone": "",
    "flash": "",
    "nearsight": "",
    "stun": "",
    "operator": "",
    "flush": "",
    "delay": ""
}

'''
    Handles the text-based UI system (loops until the user quits the program)
'''
class System():

    def __init__(self):
        pass

    def run(self):
        command = ""
        while(command.lower() != 'q'):
            command = input("enter agents (q to quit): ")
            team = command.split()                           #validate input here (5 valid agents)
            self.analyze(team)

    '''
        displays team comp info
        @param team: a list of strings for each agent on the team
    '''
    def analyze(self, team:list)->None:
        info_map = dict(info_template)              # making a copy of the info dict
        for agent in team:
            if agent in valid_agents:
                agent = agent.capitalize()+"()"
                character = eval(agent)
                