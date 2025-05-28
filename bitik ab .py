def distance_calculator(queue, coordinates):
    distance = 0
    city_amount = len(queue)
    for i in range(city_amount):
        city1_coords = queue[i]
        city2_coords = queue[(i + 1) % city_amount]
        mini_distance = ((coordinates[city1_coords][0]-coordinates[city2_coords][0])**2+(coordinates[city1_coords][1]-coordinates[city2_coords][1])**2)**0.5
        distance = distance + mini_distance
    return distance

def SingleSwapSearch(cities, k):
    city_names = list(cities.keys())
    city_coordinates = [cities[i] for i in city_names]
    first_queue = list(range(len(city_coordinates)))
    random.shuffle(first_queue)
    current_queue = list(first_queue)
    current_distance = distance_calculator(current_queue, city_coordinates)
    errors = 0
    replays = 1
    while errors < k:
        temp = list(current_queue)
        city_amount = len(temp)
        selected1, selected2 = random.sample(range(city_amount), 2)
        temp[selected1], temp[selected2] = temp[selected2], temp[selected1]
        new_distance = distance_calculator(temp, city_coordinates)
        if new_distance < current_distance:
            current_queue = list(temp)
            current_distance = new_distance
            errors = 0
        else:
            errors = errors + 1
        replays = replays + 1
    best_queue = [city_names[i] for i in current_queue]
    print("Best Solution (single swap): ", best_queue)
    print("Shortest Distance (single swap): ", int(current_distance))
