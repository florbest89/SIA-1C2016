# TODO: REPLACEMENT METHODS

# REPLACEMENT METHODS 2
# k padres
def replacement_method_2(population, k, selection, mutation):
    index_parents = sample(range(0, len(population) - 1), k)

    selected = []
    selected_result = []

    for idx in index_parents:
        selected.append(population[idx])

    selected_result =