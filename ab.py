import random

def calculate_tour_length(solution, coordinates):
    total_length = 0
    num_cities = len(solution)
    for i in range(num_cities):
        city1_index = solution[i]
        city2_index = solution[(i + 1) % num_cities]
        dist = ((coordinates[city1_index][0] - coordinates[city2_index][0]) ** 2 +
                (coordinates[city1_index][1] - coordinates[city2_index][1]) ** 2) ** 0.5
        total_length += dist
    return total_length

def single_swap_search(cities, k):
    city_names = list(cities.keys())
    city_coordinates = [cities[name] for name in city_names]

    initial_solution = list(range(len(city_coordinates)))
    random.shuffle(initial_solution)

    current_solution = list(initial_solution)
    current_objective_value = calculate_tour_length(current_solution, city_coordinates)
    unsuccessful_swap_count = 0

    iteration = 1
    while unsuccessful_swap_count < k:
        temp_solution = list(current_solution)
        num_cities = len(temp_solution)

        idx1, idx2 = random.sample(range(num_cities), 2)
        temp_solution[idx1], temp_solution[idx2] = temp_solution[idx2], temp_solution[idx1]
        new_objective_value = calculate_tour_length(temp_solution, city_coordinates)

        if new_objective_value < current_objective_value:
            current_solution = list(temp_solution)
            current_objective_value = new_objective_value
            unsuccessful_swap_count = 0
        else:
            unsuccessful_swap_count += 1

        iteration += 1

    # Şehir isimlerini sonuçta göstermek için çözüm sırasını şehir isimlerine çevir
    best_solution_named = [city_names[i] for i in current_solution]
    print(f"Best Solution (single swap): {best_solution_named}")
    print(f"Shortest Distance (single swap): {current_objective_value:.2f}")

