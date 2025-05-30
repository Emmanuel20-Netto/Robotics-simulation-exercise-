# Hardware-in-the-Loop(HIL) Simulation
### Introduction 
The goal of this simulation is to improve the line following behavior of our robot so it can only follow the outer most line of the field and being able to return on the black line when it goes away from it. we will also implement Dijkstra's algorithm to find the shortest path on the map, programed in micropython. 
### Features
- ESP 32: this will be the control part of the simulation, and will be programmed in micropython to recieves sensor readings from webot and send control data back to webot via serial communication on our computer.
- Dijkstra algorithm: this will be used to find the shortest path on the graph between nodes as described above and will be programmed in micropython.
- Thonny: We will use the Thonny ide for programming and flashing our ESP 32 with micropython.
- webot: webot is used to run the simulation.
### Dijkstra's algorithm 
Finding the shortest path we will impement dijkstra algorithm in the following steps:
- 
