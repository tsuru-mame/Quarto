import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools


class Quarto:
    def __init__(self) -> None:
        self.board = np.array([[np.nan]*4]*4)
        self.blocks = {}
        for i, v in enumerate(itertools.product([True, False], repeat=4)):
            self.blocks[i] = np.array(v)
        print(self.blocks)

        block_attr = [
            {True: 'black', False: 'white'},    # 'color'
            {True: 'big', False: 'small'},      # 'height'
            {True: 'cube', False: 'round'},     # 'shape'
            {True: 'hole', False: 'nohole'}     # 'hole'
            ]

    def get_board(self):
        return self.board
    
    def set_board(self, i, j, block):
        if np.isnan(self.board[i, j]):
            self.board[i, j] = block
            return True
        else:
            return False

    def check_line(self, line):
        f_list = np.array([False, False, False, False])
        t_list = np.array([True, True, True, True])
        for block in line:
            f_list += self.blocks[block]
            t_list *= self.blocks[block]
        if False in f_list or True in t_list:
            return True
        else:
            return False

    def check(self):
        for i in range(4):
            if ~np.isnan(self.board[i,:]).any():
                if self.check_line(self.board[i,:]):
                    print(f"row:{i}")
                    return True
            if ~np.isnan(self.board[:,i]).any():
                if self.check_line(self.board[:,i]):
                    print(f"col:{i}")
                    return True
        if ~np.isnan(np.diag(self.board)).any():
            if self.check_line(np.diag(self.board)):
                print(f"diag:{i}")
                return True

        return False

def main():
    quarto = Quarto()
    moves = [
        [0,1,3],
        [1,1,6],
        [2,0,15],
        [0,2,7],
        [1,2,10],
        [1,3,2],
        [3,2,0],
        [3,3,9],
        [2,3,11],
        [0,0,14],
        [1,0,13],
        [3,0,12],
        ]
    for move in moves:
        quarto.set_board(move[0], move[1], move[2])
        print(quarto.get_board())
        if quarto.check():
            break
        


if __name__ == "__main__": 
    main() 