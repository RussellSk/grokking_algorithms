# Chapter 8
# Set covering problem

# List of states you want to cover
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

# List of stations
stations = {}
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            states_covered = covered
            best_station = station
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
