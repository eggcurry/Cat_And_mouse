import numpy as np

class Environment(object):
    # the session terminates if:
    # 1) the cat catches the mouse
    # 2) the mouse hits a wall or obstacle

    def __init__(self, gridworld, cat, mouse):
        self.gridworld = gridworld
        self.cat = cat
        self.mouse = mouse

    def cat_reward(self, new_pos):
        # if this is the mouse (3), we terminate the game
        if self.gridworld.evaluate(new_pos[0],new_pos[1]) == 3:
            return "done"

        # if this is near the mouse (3)
        # checks if the mouse is anywhere in the 8 (max) surrounding squares
        # because of the boundary at the walls, the agent can never look out of bounds
        for i,j in [(-1, 0), (1, 0), (0, -1), (0, 1), (1,1), (-1,1), (-1,-1), (1,-1)]:
            if self.gridworld.evaluate(new_pos[0]+i,new_pos[1]+j) == 3:
                return np.random.normal(3, 0.25)


        # if this is anything else, slight negative cost
        return np.random.normal(-0.5, 0.25)

    def mouse_reward(self, new_pos):
        # if this is the cat (2), we terminate the game
        if self.gridworld.evaluate(new_pos[0],new_pos[1]) == 2:
            return "done"

        # if this is an obstacle or wall (0), we get a negative reward
        if self.gridworld.evaluate(new_pos[0],new_pos[1]) == 0:
            return np.random.normal(-3, 0.25)

        # if we are in the vicinity of the cat (2 within the 8 blocks surrounding mouse), give higher reward
        for i,j in [(-1, 0), (1, 0), (0, -1), (0, 1), (1,1), (-1,1), (-1,-1), (1,-1)]:
            if self.gridworld.evaluate(new_pos[0]+i,new_pos[1]+j) == 2:
                return np.random.normal(3, 0.25)

        # if we are at nothing (open floor) add a minimal reward, noise
        return np.random.normal(0.5, 0.25)

    def run(self, cat_action, mouse_action):
        # runs one step of the simulation
        # takes in the cat_action and mouse action
        # returns the cat reward and mouse reward respectively

        # maybe we want a sudden change in direction with 10% change to emulate erratic behavior in mouse
        if np.random.rand() <= 0.1:
            pass