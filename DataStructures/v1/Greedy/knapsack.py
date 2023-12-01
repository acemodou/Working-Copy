def knapsack(weights, profits, capacity):
    items = list(zip(weights, profits))
    items.sort(key = lambda item: item[1] / item[0], reverse=True)
    
    selected_items = []
    max_profit = 0

    for item in items:
        if capacity >= item[0]:
            max_profit += item[1]
            selected_items.append(item)
            capacity -= item[0]
    return max_profit, selected_items


weights = [2, 3, 5, 7, 1, 4, 1]
profits = [10, 5, 15, 7, 6, 18, 3]
capacity = 15
max_profit, selected_items = knapsack(weights, profits, capacity)
print("Maximum Profit: ", max_profit)
print("Selected items: ", selected_items)
















