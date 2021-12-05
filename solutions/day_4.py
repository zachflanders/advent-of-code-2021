import pandas
import requests
from collections import OrderedDict

from settings import cookie


class BingoSubsystem:

    def __init__(self):
        raw_input = requests.get(
            'https://adventofcode.com/2021/day/4/input',
            headers={'cookie': cookie}
        ).text.split('\n')[:-1]
        self.numbers = [int(num) for num in raw_input[0].split(',')]
        self.boards = [
            pandas.concat([
                pandas.DataFrame(data=[int(num) for num in row.split(' ') if num != '']).T
                for row in raw_input[i + 1:i + 6]
            ]).reset_index(drop=True)
            for i, row in enumerate(raw_input) if row == ''
        ]
        self.marks = [
            pandas.DataFrame({i: [False, False, False, False, False] for i in range(0, 5)})
            for _ in range(0, len(self.boards))
        ]

    def play(self):
        wins = OrderedDict()
        for num in self.numbers:
            for i, board in enumerate(self.boards):
                self.marks[i] = self.marks[i] + board.isin([num])
                if i not in wins and (self.marks[i].all().any() or self.marks[i].all(axis='columns').any()):
                    wins[i] = self.calc_score(num, board, self.marks[i])
        return wins.popitem(last=False)[1], wins.popitem()[1]

    @staticmethod
    def calc_score(num, board, marks):
        unmarked_sum = board.mask(marks).sum().sum()
        return int(unmarked_sum * num)


if __name__ == '__main__':
    bs = BingoSubsystem()
    solution_1, solution_2 = bs.play()
    print(f'Solution 1 = {solution_1}')
    print(f'Solution 2 = {solution_2}')
