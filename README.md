Hyperloop Passenger Booking System
----------------------------------
The Hyperloop Passenger Booking System is a command-line application designed to manage passenger bookings 
and pod operations for a hyperloop transport system. The system allows users to initialize the network of 
interconnecting routes, add passengers to the booking queue, start pods with the oldest passengers, and print 
the current passenger queue. It is built using Python and aims to demonstrate a simplified simulation of 
passenger management within a hyperloop transport network.

Features
--------
Initialize System:
******************
The system can be initialized with a number of interconnecting routes and the starting station.
Users can input the details of interconnections (boarding station, destination station, and distance) 
to establish the routes.

Add Passengers:
***************
Users can add passengers to the booking queue with their names, ages, and destination stations.
Multiple passengers can be added in a single command.

Start Pods:
***********
The system can start pods with passengers based on the age of passengers and the shortest interconnection path 
to their destinations.
The oldest passenger in the queue is given priority to board the pod, and the best route is determined using 
a simple shortest path algorithm.

Print Queue:
************
Users can print the details of passengers remaining in the booking queue.
The count of remaining passengers and their names and ages are displayed.

Exit:
*****
Users can exit the application, and a thank you message is displayed.

Usage Examples
--------------
You can run this Project in command prompt by using this following commands;
- cd path\to\directory
- python program.py

1. Initialize the system:
*************************
1. Initialize System
2. Add Passengers
3. Start Pods
4. Print Queue
5. Exit
Choose a command: 1
Enter total number of interconnections: 7
Enter starting station: a
Enter interconnections (boarding, destination, distance): a b 3
Enter interconnections (boarding, destination, distance): b d 4
Enter interconnections (boarding, destination, distance): c e 4
Enter interconnections (boarding, destination, distance): a c 2
Enter interconnections (boarding, destination, distance): d f 5
Enter interconnections (boarding, destination, distance): a f 3
Enter interconnections (boarding, destination, distance): b d 2

Add passengers:
**************
1. Initialize System
2. Add Passengers
3. Start Pods
4. Print Queue
5. Exit
Choose a command: 2
Enter number of passengers: 4        
Enter passenger name: Tamil
Enter passenger age: 54
Enter destination station: d
Enter passenger name: Isaac 
Enter passenger age: 22
Enter destination station: c
Enter passenger name: hepshiba
Enter passenger age: 21
Enter destination station: f
Enter passenger name: jeyashree
Enter passenger age: 46
Enter destination station: b

Start pods:
**********
1. Initialize System
2. Add Passengers
3. Start Pods
4. Print Queue
5. Exit
Choose a command: 3
START_POD
The shortest interconnection path for Tamil is:
a -> b -> d
Tamil has started their journey.
1. Initialize System
2. Add Passengers
3. Start Pods
4. Print Queue
5. Exit
Choose a command: 4
Total remaining passengers are: 3
They are:
Isaac 22
hepshiba 21
jeyashree 46
1. Initialize System
2. Add Passengers
3. Start Pods
4. Print Queue
5. Exit
Choose a command: 3
START_POD
The shortest interconnection path for jeyashree is:
a -> b
jeyashree has started their journey.
1. Initialize System
2. Add Passengers
3. Start Pods
4. Print Queue
5. Exit
Choose a command: 3
START_POD
The shortest interconnection path for Isaac is:
a -> c
Isaac has started their journey.
1. Initialize System
2. Add Passengers
3. Start Pods
4. Print Queue
5. Exit
Choose a command: 3
START_POD
The shortest interconnection path for hepshiba is:
a -> f
hepshiba has started their journey.

Print remaining queue:
*********************
1. Initialize System
2. Add Passengers
3. Start Pods
4. Print Queue
5. Exit
Choose a command: 4
Total remaining passengers are: 0

Exit the application:
********************
1. Initialize System
2. Add Passengers
3. Start Pods
4. Print Queue
5. Exit
Choose a command: 5
EXIT
Thank you for using the Hyperloop Passenger Booking System!
