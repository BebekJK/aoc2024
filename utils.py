import requests
from dotenv import load_dotenv
import os

load_dotenv()
session = os.getenv('SESSION')
day = 18

if __name__ == '__main__':
    data = requests.get(f'https://adventofcode.com/2024/day/{day}/input', cookies={'session': session}).text
    with open(f'input/day{day}.txt', 'w') as f:
        f.write(data)