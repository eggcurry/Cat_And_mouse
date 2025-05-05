from Gridworld import Gridworld
from Environment import Environment
from CatAgent import CatAgent
from MouseAgent import MouseAgent
import numpy as np

if __name__ == '__main__':
    # set the locations where the cat and mouse should start
    # these can be randomly generated or chosen deliberately
    cat_start_pos = (3,4)
    mouse_start_pos = (5,6)

    g = Gridworld(dimensions=(20,20), cat_start=cat_start_pos, mouse_start=(mouse_start_pos), obstacles=10)

    # visualize the track in gridspace
    g.visualize()

    # create the two agents
    cat_agent = CatAgent(pos=cat_start_pos)
    mouse_agent = MouseAgent(pos=mouse_start_pos)

    # here we probably want two policies (for each agent)