from quarto import Quarto
import random
import numpy as np


class Play():
    def __init__(self) -> None:
        self.count = 0
        self.win_count_A = 0
        self.win_count_B = 0

    
    def game(self):
        quarto = Quarto()
        if random.randrange(2):
            p1 = 'A'
            p2 = 'B'
        else:
            p1 = 'B'
            p2 = 'A'
        
        turn = 0
        while not quarto.is_game_end():
            if turn:
                block = quarto.next_block
                coord_choice = np.isnan(quarto.board)
                index = np.random.choice(np.where(coord_choice.reshape(-1,))[0])
                coord = [int(index/coord_choice.shape[1]), index%coord_choice.shape[1]]
                quarto.set_board(coord, block)
            if quarto.remaining_blocks:
                quarto.next_block = np.random.choice(quarto.remaining_blocks)
            else:
                break
            turn += 1
        player_won = eval(f"p{turn%2+1}")
        self.count += 1
        if player_won == "A":
            self.win_count_A += 1
        if player_won == "B":
            self.win_count_B += 1
        print(f"Player {player_won} win [turn: {int(turn/2)}]")
        quarto.__init__()


    def train(self):
        try:
            while True:
                self.game()
        except KeyboardInterrupt:
            print(f"PlayerA: {self.win_count_A} wins : win rate {self.win_count_A/self.count}")
            print(f"PlayerB: {self.win_count_B} wins : win rate {self.win_count_B/self.count}")



if __name__ == "__main__": 
    play = Play()
    play.train()
