# Include the games database, named game_db
from games import games_db
from match import match
from typing import List, Tuple, Callable, Any 
# The projection functions, that give us access to certain parts of a "game" (a tuple)
def get_title(game: Tuple[str, str, int, List[str]]) -> str:
    return game[0]


def get_publisher(game: Tuple[str, str, int, List[str]]) -> str:
    return game[1]


def get_year(game: Tuple[str, str, int, List[str]]) -> int:
    return game[2]


def get_developers(game: Tuple[str, str, int, List[str]]) -> List[str]:
    return game[3]

def title_by_year(matches: List[str]) -> List[str]:
    """Finds all videogames made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of videogame titles made in the passed in year
    """
    # ["1990"]
    year = int(matches[0])
    result = []
    for game in games_db:
        if get_year(game) == year:
            result.append(get_title(game))
            return result

def title_by_year_range(matches: List[str]) -> List[str]:
    """Finds all games made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get games from 1990-2000 matches would look like
            this - ["1990", "2000"] 

    Returns:
        a list of videogame titles made during those years, inclusive (meaning if you pass
        in ["1990", "2000"] you will get movies made in 1990, 1993, 1995, 1997 & 2000)
    """
    start_year = int(matches[0])
    end_year = int(matches[1])
    result = []
    for game in games_db:
        if start_year <= game_year <= end_year:
            result.append(get_title(game))
    return result

def title_before_year(matches: List[str]) -> List[str]:
    """Finds all videogames made before the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of videogame titles made before the passed in year, exclusive (meaning if you
        pass in 1997 you won't get any movies made that year, only before)
    """
    year = int(matches[0])
    result = []
    for game in games_db:
        if get_year(game) < year:
            result.append(get_title(game))
    return result


def title_after_year(matches: List[str]) -> List[str]:
    """Finds all videogames made after the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of videogame titles made after the passed in year, exclusive (meaning if you
        pass in 1997 you won't get any movies made that year, only after)
    """
    year = int(matches[0])
    result = []
    for game in games_db:
        if get_year(game) > year:
            result.append(get_title(game))
    return result

def publisher_by_title(matches: List[str]) -> List[str]:
    """Finds publisher of videogame based on title

    Args:
        matches - a list of 1 string, just the title

    Returns:
        a list of 1 string, the publisher of the videogame
    """
    title = matches[0]
    result = []
    for game in games_db:
        if get_title(game) == title:
            result.append(get_publisher(game))
    return result


def title_by_publisher(matches: List[str]) -> List[str]:
    """Finds videogames released by the passed in publisher

    Args:
        matches - a list of 1 string, just the publisher

    Returns:
        a list of videogame titles published by the passed in publisher
    """
    publisher = matches[0]
    result = []
    for game in games_db:
        if get_publisher(game) == publisher:
            result.append(get_title(game))
    return result


def developers_by_title(matches: List[str]) -> List[str]:
    """Finds developers who worked in the passed in videogame title

    Args:
        matches - a list of 1 string, just the videogame title

    Returns:
        a list of developers who worked in the passed in title
    """
    title = matches[0]
    result = []
    for game in games_db:
        if get_title(game) == title:
            result = get_developers(movie)
    return result


def year_by_title(matches: List[str]) -> List[int]:
    """Finds year of passed in videogame title

    Args:
        matches - a list of 1 string, just the videogame title

    Returns:
        a list of one item (an int), the year that the videogame was released
    """
    title = matches[0]
    result = []
    for game in games_db:
        if get_title(game) == title:
            result.append(get_year(game))
    return result


def title_by_developer(matches: List[str]) -> List[str]:
    """Finds titles of all videogames that the given developer was in

    Args:
        matches - a list of 1 string, just the developer

    Returns:
        a list of videogame titles that the developer worked in
    """
    developer = matches[0]
    result = []
    for game in games_db:
        if developer in get_developers(game):
            result.append(get_title(game))
    return result

def title_by_developers(matches: List[str]) -> List[str]:
    "Finds titles of all videogames that have that number of developers"
    developers = matches[0]
    num = int (matches[1])
    result = []
    for game in games_db:
        if get_developers(game) == num:
            result.append(get_title(game))
    return result

# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

    # The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what games were made in _"), title_by_year),
    (str.split("what games were made between _ and _"), title_by_year_range),
    (str.split("what games were made before _"), title_before_year),
    (str.split("what games were made after _"), title_after_year),
    # note there are two valid patterns here two different ways to ask for the publisher
    # of a movie
    (str.split("who published %"), publisher_by_title),
    (str.split("who was the publisher of %"), publisher_by_title),
    (str.split("what games were published by %"), title_by_publisher),
    (str.split("who developed in %"), developers_by_title),
    (str.split("when was % made"), year_by_title),
    (str.split("in what games did % appear"), title_by_developer),
    (str.split("in what year was % made"), year_by_title),
    (str.split("what game had % developers"), title_by_developers),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        print(f"pattern: {pat}, source: {src}, action: {act}")
        mat = match (pat, src)
        print(f"match:{mat}")
    
        if mat is not None:
            ans = act (mat)
            print(f"answer: {ans}")
            return ans if ans else ["No answers"]

    return["I don't understand"]

       

def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the videogame database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")



if __name__ == "__main__":
    assert isinstance(title_by_year(["1990"]), list), "title_by_year not returning a list"
    assert sorted(title_by_year(["1990"])) == sorted(
        ["super mario world", "mega man 3"]
    ), "failed title_by_year test"
    assert isinstance(title_by_year_range(["1995", "1997"]), list), "title_by_year_range not returning a list"
    assert sorted(title_by_year_range(["1995", "1997"])) == sorted(
        ["star wars: dark forces", "final fantasy vii"]
    ), "failed title_by_year_range test"
    assert isinstance(title_before_year(["2000"]), list), "title_before_year not returning a list"
    assert sorted(title_before_year(["1997"])) == sorted(
        ["super mario world", "mega man 3", "mortal kombat ii", "star wars: dark forces"]
    ), "failed title_before_year test"
    assert isinstance(title_after_year(["1990"]), list), "title_after_year not returning a list"
    assert sorted(title_after_year(["1990"])) == sorted(
        ["super mario world", "mega man 3"]
    ), "failed title_after_year test"
    assert isinstance(director_by_title(["super mario world"]), list), "director_by_title not returning a list"
    assert sorted(director_by_title(["super mario world"])) == sorted(
        ["nintendo"]
    ), "failed director_by_title test"
    assert isinstance(title_by_director(["nintendo"]), list), "title_by_director not returning a list"
    assert sorted(title_by_director(["nintendo"])) == sorted(
        ["super mario world"]
    ), "failed title_by_director test"
    assert isinstance(developers_by_title(["super mario world"]), list), "developers_by_title not returning a list"
    assert sorted(developers_by_title(["super mario world"])) == sorted(
        [
            "shigeru miyamoto", 
            "katsuya eguchi hideki konno",
            "toshihiko nakago",
            "shigefumi hino",
            "koji kondo",
        ]
    ), "failed developers_by_title test"
    assert sorted(developers_by_title(["game not in database"])) == [], "failed developers_by_title not in database test"
    assert isinstance(year_by_title(["jaws"]), list), "year_by_title not returning a list"
    assert sorted(year_by_title(["super mario world"])) == sorted(
        [1990]
    ), "failed year_by_title test"
    assert isinstance(title_by_developer(["konrad tomaszkiewicz"]), list), "title_by_developer not returning a list"
    assert sorted(title_by_developer(["konrad tomaszkiewicz"])) == sorted(
        ["the witcher 3: wild hunt", "cyberpunk 2077"]
    ), "failed title_by_developer test"
    assert sorted(search_pa_list(["hi", "there"])) == sorted(
        ["I don't understand"]
    ), "failed search_pa_list test 1"
    assert sorted(search_pa_list(["who", "directed", "call of duty"])) == sorted(
        ["steven spielberg"]
    ), "failed search_pa_list test 2"
    assert sorted(
        search_pa_list(["what", "games", "were", "made", "in", "2021"])
    ) == sorted(["No answers"]), "failed search_pa_list test 3"

    print("All tests passed!")