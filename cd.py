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
