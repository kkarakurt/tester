from ab import *
import time

def distance(city1, city2):
    return ((cities[city2][0] - cities[city1][0]) ** 2 + (cities[city2][1] - cities[city1][1]) ** 2) ** 0.5

def total_distance(tour):
    return sum(distance(tour[i], tour[(i + 1) % len(tour)]) for i in range(len(tour)))

def initial_population(size):
    return [random.sample(list(cities.keys()), len(list(cities.keys()))) for _ in range(size)]

def evaluate_population(population):
    return sorted(population, key=total_distance)

def crossover(parent1, parent2):
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
    return child

def mutate(tour, mutation_rate=0.05):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def next_generation(population, mutation_rate=0.05):
    population = evaluate_population(population)
    new_population = population[:len(population) // 2]
    while len(new_population) < len(population):
        parent1, parent2 = random.sample(new_population, 2)
        child = crossover(parent1, parent2)
        child = mutate(child, mutation_rate)
        new_population.append(child)
    return new_population

def genetic_algorithm(generations, population_size=20, mutation_rate=0.05):
    population = initial_population(population_size)
    for _ in range(generations):
        population = next_generation(population, mutation_rate)
    best = evaluate_population(population)[0]
    best_dist = total_distance(best)
    print("Best Solution (genetic):", best + [best[0]])
    print("Shortest Distance (genetic):", round(best_dist, 3))

def timer(fonksiyon, *args, **kwargs):
    start = time.time()
    fonksiyon(*args, **kwargs)
    end = time.time()
    return (end - start) * 1000  # Milisaniye

# --- Ana program (main) ---

# Şehirler ve koordinatları
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

population_size = 10      # Kaç birey oluşturulacak
generations = 900       # Kaç jenerasyon çalıştırılacak
mutation_rate = 0.05      # Mutasyon ihtimali

k = 3

start_time_swap = time.time()
single_swap_search(cities, k)
end_time_swap = time.time()
duration_swap = end_time_swap - start_time_swap
print(f"Single Swap Search süresi: {duration_swap:.4f} saniye\n")

# --- Genetic Algorithm Süresi ---
start_time_genetic = time.time()
genetic_algorithm(generations, population_size, mutation_rate)
end_time_genetic = time.time()
duration_genetic = end_time_genetic - start_time_genetic
print(f"Genetik Algoritma süresi: {duration_genetic:.4f} saniye")



