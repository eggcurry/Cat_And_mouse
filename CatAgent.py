import numpy as np

class CatAgent:
    # the cat agent's goal is to capture the mouse
    # thus it will be rewarded for reaching the same square as the mouse or narrowly missing it, i.e. reaching a space next to the mouse
    # the cat is a living creature and we will assume it expends energy to travel, so there is a slight cost to movement
    def __init__(self):
        pass