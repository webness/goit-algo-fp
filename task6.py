items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_calories = 0
    selected_items = []

    for name, data in sorted_items:
        if budget >= data["cost"]:
            selected_items.append(name)
            budget -= data["cost"]
            total_calories += data["calories"]

    return selected_items, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]

    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n][budget]
    return selected_items, total_calories


if __name__ == "__main__":
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    print("Greedy Algorithm Result:")
    print(f"Selected items: {greedy_result[0]}")
    print(f"Total calories: {greedy_result[1]}")

    dp_result = dynamic_programming(items, budget)
    print("\nDynamic Programming Result:")
    print(f"Selected items: {dp_result[0]}")
    print(f"Total calories: {dp_result[1]}")
