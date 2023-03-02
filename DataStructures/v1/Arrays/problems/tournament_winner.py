def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

AWAY_TEAM_WINNER = 0
def tournamentWinner(competitions, results):
    is_winner = ""
    output = {}
    for idx, values in enumerate(competitions):
        home, away = values 
        is_winner = away if results[idx] == AWAY_TEAM_WINNER else home  
        update_winner(output, is_winner)
    
    # Get the maximum value 
    max_value = max(output.values())

    # Find the key associated with the maximum vlaue 
    max_key = [k for k, v in output.items() if v== max_value]
    return max_key[0]


def update_winner(results, is_winner):
    if is_winner not in results:
        results.update({is_winner: 1}) 
    else:
        results[is_winner] += 1
    return results 


simple_assert(tournamentWinner([["HTML", "C#"],["C#", "Python"],["Python", "HTML"]], 
[0, 0, 1]), "Python")
simple_assert(tournamentWinner([["HTML", "Java"],
["Java", "Python"],
["Python", "HTML"]], [0, 1, 1]), "Java")
simple_assert(tournamentWinner( [["HTML", "Java"],
["Java", "Python"],["Python", "HTML"],
["C#", "Python"],
["Java", "C#"],["C#", "HTML"]], [0, 1, 1, 1, 0, 1]), "C#")
simple_assert(tournamentWinner([["HTML", "Java"],
["Java", "Python"],["Python", "HTML"],
["C#", "Python"],["Java", "C#"],["C#", "HTML"],
["SQL", "C#"],["HTML", "SQL"],["SQL", "Python"],
["SQL", "Java"]], [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]), "C#")
simple_assert(tournamentWinner([["Bulls", "Eagles"]], [1]), "Bulls")
