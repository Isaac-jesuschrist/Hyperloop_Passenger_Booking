class HyperloopSystem:
    def __init__(self):
        self.routes = {}
        self.passenger_queue = []
        self.starting_station = []

    def initialize_system(self, N, starting_station):
        self.starting_station = starting_station
        self.routes = {station: {} for station in starting_station}
        for _ in range(N):
            source, dest, distance = input("Enter interconnections (boarding, destination, distance): ").split()
            distance = int(distance)
            if source not in self.routes:
                self.routes[source] = {}
            if dest not in self.routes:
                self.routes[dest] = {}
            self.routes[source][dest] = distance
            self.routes[dest][source] = distance

    def add_passenger(self, num_passengers):
        for _ in range(num_passengers):
            name = input("Enter passenger name: ")
            age = int(input("Enter passenger age: "))
            dest = input("Enter destination station: ")
            self.passenger_queue.append((name, age, dest))

    def find_shortest_path(self, boarding, destination):
        visited = set()
        queue = [(boarding, [])]

        while queue:
            current, path = queue.pop(0)
            if current == destination:
                path.append(current)
                print(" -> ".join(path))
                return
            if current in visited:
                continue
            visited.add(current)
            for neighbor, distance in self.routes[current].items():
                if neighbor not in visited:
                    queue.append((neighbor, path + [current]))

    def start_pod(self):
        if not self.passenger_queue:
            print("No passengers in the queue.")
        else:
            oldest_passenger = max(self.passenger_queue, key=lambda x: x[1])
            print("START_POD")
            print(f"The shortest interconnection path for {oldest_passenger[0]} is:")
            self.find_shortest_path(self.starting_station[0], oldest_passenger[2])
            self.passenger_queue.remove(oldest_passenger)
            print(f"{oldest_passenger[0]} has started their journey.")

    def print_queue(self):
        print(f"Total remaining passengers are: {len(self.passenger_queue)}")
        print("They are:")
        for passenger in self.passenger_queue:
            print(f"{passenger[0]} {passenger[1]}")

def main():
    hyperloop = HyperloopSystem()
    while True:
        print("1. Initialize System")
        print("2. Add Passengers")
        print("3. Start Pods")
        print("4. Print Queue")
        print("5. Exit")
        choice = input("Choose a command: ")
        
        if choice == "1":
            N = int(input("Enter total number of interconnections: "))
            starting_station = [input("Enter starting station: ")]
            hyperloop.initialize_system(N, starting_station)
        elif choice == "2":
            try:
                num_passengers = int(input("Enter number of passengers: "))
                hyperloop.add_passenger(num_passengers)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            hyperloop.start_pod()
        elif choice == "4":
            hyperloop.print_queue()
        elif choice == "5":
            print("EXIT")
            print("Thank you for using the Hyperloop Passenger Booking System!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
