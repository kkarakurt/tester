from ab import *
import time

def GeneticAlgorithm(cities, generations, sample_size, mutation_prob):
    city_names = list(cities.keys())
    sample = [random.sample(list(city_names), len(city_names)) for i in range(sample_size)]
    for i in range(generations):
        sample.sort(key=lambda queue: distance_calculator(queue, cities))
        new_sample = sample[:sample_size // 2]
        while len(new_sample) < sample_size:
            parent1, parent2 = random.sample(new_sample, 2)
            size = len(parent1)
            start, end = sorted(random.sample(range(size), 2))
            child = [None] * size
            child[start:end] = parent1[start:end]
            temp = 0
            for i in range(size):
                if child[i] is None:
                    while parent2[temp] in child:
                        temp = temp + 1
                    child[i] = parent2[temp]
                    temp = temp + 1
            if random.random() < mutation_prob:
                i, j = random.sample(range(len(child)), 2)
                child[i], child[j] = child[j], child[i]
            new_sample.append(child)
        sample = new_sample
    sample.sort(key=lambda queue: distance_calculator(queue, cities))
    best_queue = sample[0]
    best_distance = distance_calculator(best_queue, cities)
    print("Best Solution (genetic):", best_queue)
    print("Shortest Distance (genetic):", round(best_distance, 2))

# --- Ana program (main) ---

cities = {
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

sample = 5
generations = 100
mutation_prob = 0.05  # yüzde 5

k = 100

start_time_swap = time.time()
SingleSwapSearch(cities, k)
end_time_swap = time.time()
duration_swap = (end_time_swap - start_time_swap)*1000
print(f"Single Swap Search süresi: ", round(duration_swap, 2), "Ms\n")

# --- Genetic Algorithm Süresi ---
start_time_genetic = time.time()
GeneticAlgorithm(cities, generations, sample, mutation_prob)
end_time_genetic = time.time()
duration_genetic = (end_time_genetic-start_time_genetic)*1000
print("Genetik Algoritma süresi: ", round(duration_genetic, 2), "Ms")