from pathlib import Path


class SubSteerer:

    def __init__(self):
        with open(Path(__file__).parent / 'input.txt', 'r') as f:
            raw_input = f.read().split('\n')
        self.directions = [
            direction.split(' ')
            for direction in raw_input[:-1]
        ]

    def steer_sub(self):
        horizontal = 0
        depth = 0
        for direction in self.directions:
            if direction[0] == 'forward':
                horizontal = horizontal + int(direction[1])
            elif direction[0] == 'down':
                depth = depth + int(direction[1])
            elif direction[0] == 'up':
                depth = depth - int(direction[1])
        return horizontal, depth

    def steer_sub_with_aim(self):
        horizontal = 0
        depth = 0
        aim = 0
        for direction in self.directions:
            if direction[0] == 'forward':
                horizontal = horizontal + int(direction[1])
                depth = depth + aim * int(direction[1])
            elif direction[0] == 'down':
                aim = aim + int(direction[1])
            elif direction[0] == 'up':
                aim = aim - int(direction[1])
        return horizontal, depth, aim


if __name__ == '__main__':
    sub_steerer = SubSteerer()
    horizontal_1, depth_1 = sub_steerer.steer_sub()
    horizontal_2, depth_2, aim_2 = sub_steerer.steer_sub_with_aim()
    print(f'Solution 1: horizontal = {horizontal_1}, depth = {depth_1}, product = {horizontal_1 * depth_1}')
    print(f'Solution 1: horizontal = {horizontal_2}, depth = {depth_2}, aim = {aim_2} product = {horizontal_2 * depth_2}')
    assert horizontal_1 * depth_1 == 1459206
    assert horizontal_2 * depth_2 == 1320534480
