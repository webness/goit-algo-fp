import random
import matplotlib.pyplot as plt
import pandas as pd


def monte_carlo_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sums_count[dice_sum] += 1

    probabilities = {s: count / num_rolls for s, count in sums_count.items()}
    return probabilities


def theoretical_probabilities():
    outcomes = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    sums_count = {i: 0 for i in range(2, 13)}

    for die1, die2 in outcomes:
        dice_sum = die1 + die2
        sums_count[dice_sum] += 1

    total_outcomes = len(outcomes)
    probabilities = {s: count / total_outcomes for s, count in sums_count.items()}
    return probabilities


def plot_probabilities(monte_carlo_probs, theoretical_probs):
    sums = sorted(monte_carlo_probs.keys())
    mc_values = [monte_carlo_probs[s] for s in sums]
    theoretical_values = [theoretical_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, mc_values, color='blue', alpha=0.6, label="Monte Carlo Probabilities", width=0.4)
    plt.bar([s + 0.4 for s in sums], theoretical_values, color='orange', alpha=0.6, label="Theoretical Probabilities", width=0.4)
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability")
    plt.title("Monte Carlo vs. Theoretical Probabilities of Dice Sums")
    plt.xticks(sums)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    num_rolls = 100000

    mc_probs = monte_carlo_dice_rolls(num_rolls)

    theoretical_probs = theoretical_probabilities()

    results_table = pd.DataFrame({
        "Sum": sorted(mc_probs.keys()),
        "Monte Carlo Probability": [mc_probs[s] for s in sorted(mc_probs.keys())],
        "Theoretical Probability": [theoretical_probs[s] for s in sorted(theoretical_probs.keys())]
    })
    print(results_table)

    plot_probabilities(mc_probs, theoretical_probs)
