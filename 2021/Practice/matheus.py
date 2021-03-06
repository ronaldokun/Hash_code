# TODO import your packages
import numpy as np
import operator
from common import scorer
from tqdm import tqdm


def count_ingredients(pizzas):
    count_ingred = {}
    for pizza in pizzas:
        for ig in pizza:
            if ig not in count_ingred.keys():
                count_ingred[ig] = 1
            elif ig in count_ingred.keys():
                count_ingred[ig] = count_ingred[ig] + 1
    return count_ingred


class Pizza:
    def __init__(self, pizza, idx, count_ingred):
        self.score = sum([1 / count_ingred[key] for key in set(pizza)])
        self.idx = idx


def matheus_solution(info, **kwargs):
    # TODO write your solution here!
    M, T2, T3, T4, pizzas = info

    # Count all ingredients to use as score
    ing = count_ingredients(pizzas)

    new_pizzas = []
    for i, val in enumerate(pizzas):
        new_pizzas.append(Pizza(val, i, ing))

    sorted_new_pizzas = sorted(
        new_pizzas, key=operator.attrgetter("score"), reverse=True
    )

    draw_arr = []
    for i in range(T4):
        draw_arr.append(4)
    for i in range(T3):
        draw_arr.append(3)
    for i in range(T2):
        draw_arr.append(2)

    def assign_pizzas():
        solution = []
        curr_idx = 0
        for val in draw_arr:
            end_idx = curr_idx + val
            if end_idx <= len(sorted_new_pizzas):
                choices = [n.idx for n in sorted_new_pizzas[curr_idx:end_idx]]
                team_size = val
                new_entry = [team_size,] + choices
                solution.append(new_entry)
            curr_idx += val

        score = scorer(solution, info)

        return solution, score

    # Try different draw orders for a best score
    best_score = 0
    num_iters = kwargs.get("num_iters", 1)
    final_solution, best_score = assign_pizzas()

    return final_solution, best_score
