class GreedyAlgorithm:

    def __init__(self):
        self.states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
        self.stations = {}
        self.stations["k1"] = {"id", "nv", "ut"}
        self.stations["k2"] = {"wa", "id", "mt"}
        self.stations["k3"] = {"or", "nv", "ca"}
        self.stations["k4"] = {"nv", "ut"}
        self.stations["k5"] = {"ca", "az"}
        self.final_stations = set()

    def findCoverage(self):
        while self.states_needed:
            best_station = None
            states_covered = set()

            for station, states_station_covers in self.stations.items():
                covered = self.states_needed & states_station_covers
                if len(covered) > len(states_covered):
                    best_station = station
                    states_covered = covered

            self.states_needed -= states_covered
            self.final_stations.add(best_station)

    def getCoverage(self):
        return self.final_stations
