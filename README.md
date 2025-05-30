# Hardware-in-the-Loop(HIL) Simulation
### Introduction 
The goal of this simulation is to improve the line following behavior of our robot so it can only follow the outer most line of the field and being able to return on the black line when it goes away from it. we will also implement Dijkstra's algorithm to find the shortest path on the map, programed in micropython. 
### Features
- ESP 32: this will be the control part of the simulation, and will be programmed in micropython to recieves sensor readings from webot and send control data back to webot via serial communication on our computer.
- Dijkstra algorithm: this will be used to find the shortest path on the graph between nodes as described above and will be programmed in micropython.
- Thonny: We will use the Thonny ide for programming and flashing our ESP 32 with micropython.
- webot: webot is used to run the simulation.
- USB cable: we will use it to connect the ESP32 to the computer and for uploading code to EPS32.
### Dijkstra's algorithm 
Finding the shortest path we will impement dijkstra algorithm in the following steps:
- step 1:
Identify every point(node) where two lines meet with a letter or number( e.g A.....D)
- step 2:
  Assign the a cost of infinity(∞) to every given node and always set the start node to zero(0) because the distance from the same point to that point is zero(0).
- step 3:
  Find the adjescent nodes to between every nodes and write them down as like this (A  = {B, C,}.
- step 4:
  Write down the cost to move between this nodes, from the starting node. using this formular
  cost(adjescent node) = cost(starting) + distance from starting node to neighbor node. for        example if the starting node is 'A' and 'A' has a distance of '0' then the adjescent neighbor    from 'A' is 'B' and the distance at between them is   '10' then the cost to move from A to be    with be 0 + 10. after this change the maximum distance from infinity('∞') to 10.
- step 5:
   find the minimum cost neighbor for the next starting point, and mark all visited nodes do not    do it two times.
- step 6:
  compare the calculated cost with the present cost. if the present cost is less than the          calculated cost, replace it with the calculated cost to get the minimum cost between. if not     just keep the present cost to that node.

     
