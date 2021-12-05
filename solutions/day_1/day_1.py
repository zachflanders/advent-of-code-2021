from pathlib import Path


class DepthAnalyzer:

    def __init__(self):
        with open(Path(__file__).parent / 'input.txt', 'r') as f:
            raw_input = f.read().split('\n')
        self.depths = list(map(
            int,
            raw_input[:-1]
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
    assert depth_analyzer.num_increasing() == 1226
    assert depth_analyzer.num_increasing(window=3) == 1252
