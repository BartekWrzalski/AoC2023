from multiprocessing import Process, Manager
import math

with open("day5/day5.txt", "r", encoding="utf-8") as file:
    input = file.read()

sections = input.split("\n\n")

seeds = [int(seed) for seed in sections[0].split()[1:]]
mapping_tables = []

for i in range(1, len(sections)):
    mapping_tables.append([[int(num) for num in line.split()] for line in sections[i].split("\n")[1:]])
    mapping_tables[i - 1].sort(key=lambda x: x[1], reverse=True)


def get_location(seed):
    current_val = seed
    for i, map_section in enumerate(mapping_tables):
        for _map in map_section:
            if current_val < _map[1]:
                continue
            
            if current_val <= _map[1] + _map[2] - 1:
                current_val = _map[0] + current_val - _map[1]
            break
            
    return current_val


def one():
    location = get_location(seeds[0])
    for seed in seeds[1:]:
        location = min(location, get_location(seed))

    print(location)


def loop_seed(start, stop, return_list):
    print("Started - ", start, "to", stop)
    inner_loc = math.inf
    for seed in range(start, stop):
        inner_loc = min(inner_loc, get_location(seed))
    return_list.append(inner_loc)


def two():
    manager = Manager()
    locations = manager.list()

    jobs = []
    for i, first_seed in enumerate(seeds[::2]):
        p = Process(target=loop_seed, args=(first_seed, first_seed + seeds[2 * i + 1], locations,))
        
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()
    
    print(min(locations))


if __name__ == "__main__":
    # one()
    two()
