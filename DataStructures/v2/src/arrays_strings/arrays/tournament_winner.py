from typing import List 

def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

HOME_TEAM_WON = 1

# O(n) time | O(k) space: K is the number of winners
def tournamentWinner(competitions :  List[List[str]], results : List[int]):
    current_best_team = ""
    scores = {current_best_team : float('-inf')}

    for idx, teams in enumerate(competitions):
        home_team, away_team = teams
        score = results[idx]
        winner = home_team if score == HOME_TEAM_WON else away_team
        update_scores(winner, scores)
        current_winner = winner
        if scores[current_winner] >  scores[current_best_team]:
           current_best_team = current_winner
    return current_best_team

def update_scores(team, scores):
    if team not in scores:
        scores[team] = 0 
    scores[team] += 3
        
    

competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]
expected = "Python"
actual = tournamentWinner(competitions, results)
simple_assert(actual, expected)