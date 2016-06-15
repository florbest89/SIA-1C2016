from models import Defender
# TODO: IMPLEMENT SELECTION METHODS

# TODO: ROULETTE

# TODO: UNIVERSAL

# TODO: BOLTZMANN

# TODO: DETERMINISTIC TOURNAMENT

# TODO: PROBABILISTIC TOURNAMENT

# TODO: RANKING

# TODO: ELITE
def elite(N, population):
    sorted(population, key=lambda individual: individual.fitness, reverse=True)