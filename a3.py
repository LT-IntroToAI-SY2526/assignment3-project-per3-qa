# Include the videogame database, named game_db
from games import games_db
from match import match
from typing import List, Tuple, Callable, Any 
# The projection functions, that give us access to certain parts of a "game" (a tuple)
def get_title(game: Tuple[str, str, int, List[str]]) -> str:
    return game[0]


def get_publisher(game: Tuple[str, str, int, List[str]]) -> str:
    return game[1]


def get_year(game: Tuple[str, str, int, List[str]]) -> int:
    return movie[2]


def get_developers(game: Tuple[str, str, int, List[str]]) -> List[str]:
    return movie[3]
