from models import Defender
# TODO: IMPLEMENT SELECTION METHODS

# TODO: ROULETTE

# TODO: UNIVERSAL

# TODO: BOLTZMANN

# TODO: DETERMINISTIC TOURNAMENT

# TODO: PROBABILISTIC TOURNAMENT

# TODO: RANKING

def elite(N, population):

    if N < len(population):
        population.sort(key=lambda p: p.fitness, reverse=True)
        return population[0:N]
    elif N == len(population):
        return population

