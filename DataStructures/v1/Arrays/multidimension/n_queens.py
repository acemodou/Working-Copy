def solve_queens(n):
    # Record visited cols and diagonals 
    col = set()
    posDiag = set()
    negDiag = set()
    board = [["."] * n for _ in range(n)]
    result = []

    def backtrack(row):
        if row == n:
            copy_results = ["".join(row) for row in board]
            result.append(copy_results)
            return 
        
        for values in range(n):
            if values in col or (row + values) in posDiag or (row - values) in negDiag:
                continue
            col.add(values)
            posDiag.add(row + values)
            negDiag.add(row - values)
            board[row][values] = 'Q'
            backtrack(row + 1)

            col.remove(values)
            posDiag.remove(row + values)
            negDiag.remove(row - values)
            board[row][values] = '.'
        
    backtrack(0)
    print(result)
    return result


solve_queens(4)