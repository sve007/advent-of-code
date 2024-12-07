import os

import requests
from pathlib import Path
import http
def get_input(year: str, puzzle: str):
    """
    If puzzle input is not yet present in project, download it and write to file.
    year: year of puzzle
    puzzle: number of the puzzle, 1 <= puzzle <= 24

    return: None
    """

    puzzle_file = puzzle if len(puzzle) > 1 else '0' + puzzle
    input_file = Path(f"input_data/input_problem{year}{puzzle_file}.txt")
    if not input_file.exists():
        print(f"Puzzle {puzzle} from {year} not yet present. Downloading from AoC website.")
        token = os.getenv(key="AOC_SESSION")
        url = f"https://adventofcode.com/{year}/day/{puzzle}/input"
        try:
            puzzle_input = requests.get(url=url, headers={"Cookie": f"session={token}"})
            with open(str(input_file), 'bw+') as file:
                file.write(puzzle_input.content)
        except requests.exceptions.ConnectionError:
            print(f"Connection with {url} could not be made")

    else:
        print("Input already on device.")
