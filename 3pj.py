
from games import game_db
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "movie" (a tuple)
def get_title(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[0]


def get_series(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[1]


def get_year(movie: Tuple[str, str, int, List[str]]) -> int:
    return movie[2]


def get_characters(movie: Tuple[str, str, int, List[str]]) -> List[str]:
    return movie[3]


# Below are a set of actions. Each takes a list argument and returns a list of answers
# according to the action and the argument. It is important that each function returns a
# list of the answer(s) and not just the answer itself.


def title_by_year(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made in the passed in year
    """
    year = int(matches[0])
    result = []
    print(year)
    for game in game_db:
        if get_year(game) == year:
            result.append(get_title(game))
    return result


def title_by_year_range(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get movies from 1991-1994 matches would look like
            this - ["1991", "1994"] Note that these years are passed as strings and
            should be converted to ints.

    Returns:
        a list of movie titles made during those years, inclusive (meaning if you pass
        in ["1991", "1994"] you will get movies made in 1991, 1992, 1993 & 1994)
    """
    year1 = int(matches[0])
    year2 = int(matches[1])
    result = []
    for game in game_db:
        if get_year(game) < year1:
            if get_year(game) > year2;
                result.append(get_title(game))
    return result


def title_before_year(matches: List[str]) -> List[str]:
    """Finds all movies made before the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made before the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any movies made that year, only before)
    """
    year = int(matches[0])
    result = []
    for game in game_db:
        if get_year(game) < year:
            result.append(get_title(game))
    return result


def title_after_year(matches: List[str]) -> List[str]:
    """Finds all movies made after the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made after the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any movies made that year, only after)
    """
    year = int(matches[0])
    result = []
    for game in game_db:
        if get_year(game) > year:
            result.append(get_title(game))
    return result


def series_by_title(matches: List[str]) -> List[str]:
    """Finds director of movie based on title

    Args:
        matches - a list of 1 string, just the title

    Returns:
        a list of 1 string, the director of the movie
    """
    title = matches[0]
    result = []
    for game in game_db:
        if get_title(game) == title:
            result.append(get_series(game))
    return result


def title_by_series(matches: List[str]) -> List[str]:
    """Finds movies directed by the passed in director

    Args:
        matches - a list of 1 string, just the director

    Returns:
        a list of movies titles directed by the passed in director
    """
    series = matches[0]
    result = []
    for game in game_db:
        if get_series(game) == series:
            result.append(get_title(game))
    return result


def characters_by_title(matches: List[str]) -> List[str]:
    """Finds actors who acted in the passed in movie title

    Args:
        matches - a list of 1 string, just the movie title

    Returns:
        a list of actors who acted in the passed in title
    """
    title = matches[0]
    result = []
    for game in game_db:
        if get_title(game) == title:
            result.append(get_characters(game))
    return result


def year_by_title(matches: List[str]) -> List[int]:
    """Finds year of passed in movie title

    Args:
        matches - a list of 1 string, just the movie title

    Returns:
        a list of one item (an int), the year that the movie was made
    """
    title = matches[0]
    result = []
    for game in game_db:
        if get_title(game) == title:
            result.append(get_title(game))
    return result


def title_by_character(matches: List[str]) -> List[str]:
    """Finds titles of all movies that the given actor was in

    Args:
        matches - a list of 1 string, just the actor

    Returns:
        a list of movie titles that the actor acted in
    """
    character = matches[0]
    result = []
    for game in game_db:
        if get_characters(game) == character:
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
    # note there are two valid patterns here two different ways to ask for the director
    # of a movie
    (str.split("what was in the series, %"), series_by_title),
    (str.split("what is the series of %"), series_by_title),
    (str.split("what games were in the series, %"), title_by_series),
    (str.split("what characters where in %"), characters_by_title),
    (str.split("when was % made"), year_by_title),
    (str.split("in what games did % appear"), title_by_character),
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
        mat = match(pat, src)

        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers"]
        
    return ["I don't understand"]


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
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


# uncomment the following line once you've written all of your code and are ready to try
# it out. Before running the following line, you should make sure that your code passes
# the existing asserts.
# query_loop()

if __name__ == "__main__":
    assert isinstance(title_by_year(["1974"]), list), "title_by_year not returning a list"
    assert sorted(title_by_year(["1996"])) == sorted(
        ["Pokemon Red", "Pokemon Blue", "Super Mario 64"]
    ), "failed title_by_year test"
    assert isinstance(title_by_year_range(["1996", "1998"]), list), "title_by_year_range not returning a list"
    assert sorted(title_by_year_range(["1996", "1998"])) == sorted(
        ["Pokemon Red", "Pokemon Blue", "Super Mario 64","Kirby Dream Land 3","Pokemon Yellow","Legend Of Zelda: Ocacrina of Time"]
    ), "failed title_by_year_range test"
    assert isinstance(title_before_year(["1989"]), list), "title_before_year not returning a list"
    assert sorted(title_before_year(["1989"])) == sorted(
        ["Super Mario Bros. 2","The Legend of Zelda: The Adventure of Link","The Legend of Zelda","Super Mario Bros."]
    ), "failed title_before_year test"
    assert isinstance(title_after_year(["2021"]), list), "title_after_year not returning a list"
    assert sorted(title_after_year(["2021"])) == sorted(
        ["Pokemon Legends: Arceus","Pokemon Scarlet","Pokemon Violet","Kirby and the Forgotten Land","Tears of The Kingdom]
    ), "failed title_after_year test"
    assert isinstance(series_by_title(["Pokemon Red"]), list), "series_by_title not returning a list"
    assert sorted(series_by_title(["Pokemon Red"])) == sorted(
        ["Pokemon"]
    ), "failed series_by_title test"
    assert isinstance(title_by_series(["steven spielberg"]), list), "title_by_series not returning a list"
    assert sorted(title_by_series(["steven spielberg"])) == sorted(
        ["Pokemon Red", "Pokemon Blue", "Pokemon Yellow", "and so on"]
    ), "failed title_by_series test"
    assert isinstance(characters_by_title(["Pokemon Red"]), list), "characters_by_title not returning a list"
    assert sorted(characters_by_title(["Pokemon Red"])) == sorted(
        [
            "Red",
            "Blue",
            "Prof. Oark",
            "Giovanni",
            "Charizard",
        ]
    ), "failed characters_by_title test"
    assert sorted(characters_by_title(["game not in database"])) == [], "failed characters_by_title not in database test"
    assert isinstance(year_by_title(["Pokemon Red"]), list), "year_by_title not returning a list"
    assert sorted(year_by_title(["Pokemon Red"])) == sorted(
        [1996]
    ), "failed year_by_title test"
    assert isinstance(title_by_character(["Red"]), list), "title_by_character not returning a list"
    assert sorted(title_by_actor(["Red"])) == sorted(
        ["Pokemon Red", "Pokemon Blue"]
    ), "failed title_by_character test"
    
    
    assert sorted(search_pa_list(["hi", "there"])) == sorted(
        ["I don't understand"]
    ), "failed search_pa_list test 1"
    assert sorted(search_pa_list(["what", "series","is", "Pokemon Red"])) == sorted(
        ["Pokemon"]
    ), "failed search_pa_list test 2"
    assert sorted(
        search_pa_list(["what", "games", "were", "made", "in", "2020"])
    ) == sorted(["No answers"]), "failed search_pa_list test 3"

    print("All tests passed!")
