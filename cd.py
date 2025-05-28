from ab import *
import time

def GeneticAlgorithm(generations, population_size, mutation_prob, cities, coordinates):
    population = [random.sample(list(cities), len(cities)) for _ in range(population_size)]
    for i in range(generations):
        population.sort(key=lambda tour: distance_calculator(tour, coordinates))
        new_population = population[:population_size // 2]
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(new_population, 2)
            size = len(parent1)
            start, end = sorted(random.sample(range(size), 2))
            child = [None] * size
            child[start:end] = parent1[start:end]
            p2_index = 0
            for i in range(size):
                if child[i] is None:
                    while parent2[p2_index] in child:
                        p2_index += 1
                    child[i] = parent2[p2_index]
            if random.random() < mutation_prob:
                i, j = random.sample(range(len(child)), 2)
                child[i], child[j] = child[j], child[i]
            new_population.append(child)
        population = new_population
    population.sort(key=lambda tour: distance_calculator(tour, coordinates))
    best = population[0]
    best_dist = distance_calculator(best, coordinates)
    print("Best Solution (genetic):", best + [best[0]])
    print("Shortest Distance (genetic):", round(best_dist, 3))

# --- Ana program (main) ---

cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

coordinates = {
    'A': (16.47, 96.10),
    'B': (14.05, 98.12),
    'C': (20.09, 92.54),
    'D': (22.39, 93.37),
    'E': (25.23, 97.24),
    'F': (22.00, 96.05),
    'G': (20.47, 97.02),
    'H': (17.20, 96.29),
    'I': (16.30, 97.38)
}

population = 10
generations = 900
mutation_prob = 0.05  # yüzde 5

GeneticAlgorithm(generations, population, mutation_prob, cities, coordinates)












'''
start_time_swap = time.time()
SingleSwapSearch(cities, k)
end_time_swap = time.time()
duration_swap = end_time_swap - start_time_swap
print(f"Single Swap Search süresi: {duration_swap:.4f} saniye\n")

# --- Genetic Algorithm Süresi ---
start_time_genetic = time.time()
GeneticAlgorithm(generations, population_size, mutation_rate)
end_time_genetic = time.time()
duration_genetic = end_time_genetic - start_time_genetic
print(f"Genetik Algoritma süresi: {duration_genetic:.4f} saniye")
'''

