import random

from engine_base import EngineBase


class RandomMove(EngineBase):
    def generate_next_move(self):
        moves = []
        for lm in self.game.board.legal_moves:
            moves.append(lm)
        next_move = random.choice(moves)
        return next_move
