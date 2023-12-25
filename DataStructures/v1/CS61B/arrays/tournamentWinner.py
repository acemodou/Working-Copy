from typing import List
from simpleAssert import simple_assert

HOME_TEAM = 1

def tournamentWinner(competitions : List[str], results : List[int]) -> str:
    current_best = ""
    scores = {current_best : 0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition
        is_winner = home_team if result == HOME_TEAM else away_team
        update_score(is_winner, 3, scores)

        if scores[is_winner] > scores[current_best]:
            current_best = is_winner
    return current_best

def update_score(winner : str, points : int, scores : dict) -> None:
    scores.setdefault(winner, 0)
    scores[winner] += points


simple_assert(tournamentWinner([
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ],[0, 0, 1] ), "Python")