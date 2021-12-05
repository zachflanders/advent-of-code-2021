import click
import requests

from settings import cookie


@click.command()
@click.option('--day', prompt='Input day')
def get_input(day):
    raw_input = requests.get(f'https://adventofcode.com/2021/day/{day}/input', headers={'cookie': cookie}).text
    with open(f'day_{day}/input.txt', 'w') as f:
        f.write(raw_input)


if __name__ == '__main__':
    get_input()