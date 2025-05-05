from Gridworld import Gridworld
from Environment import Environment
from CatAgent import CatAgent
from MouseAgent import MouseAgent
import numpy as np

if __name__ == '__main__':
    # or you can pass through dimensions of a randomly generated grid you wish to use
    g = Gridworld(dimensions=(20,20), cat_start=(3,4), mouse_start=(5,6), obstacles=10)

    # visualize the track in gridspace
    g.visualize()
