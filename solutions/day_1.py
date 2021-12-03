import requests

from settings import cookie


class DepthAnalyzer:

    def __init__(self):
        self.depths = list(map(
            int,
            requests.get('https://adventofcode.com/2021/day/1/input', headers={'cookie': cookie}).text.split('\n')[:-1]
        ))

    def num_increasing(self, window=1):
        return sum([
            sum(self.depths[i:i+window]) > sum(self.depths[i-1:i-1+window])
            for i in range(1, len(self.depths))
        ])


if __name__ == '__main__':
    depth_analyzer = DepthAnalyzer()
    print(f'Solution 1: {depth_analyzer.num_increasing()}')
    print(f'Solution 2: {depth_analyzer.num_increasing(window=3)}')
