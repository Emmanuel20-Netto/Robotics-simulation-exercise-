# Hardware-in-the-Loop(HIL) Simulation
### Introduction 
The goal of this simulation is to improve the line following behavior of the e-puck robot so it can only follow the outer most line of the field and being able to return on the black line when it goes away from it. we will also implement Dijkstra's algorithm to find the shortest path on the map, programed in micropython. 
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
  use this formular to find the cost of the neighbor node; ###cost(neighbor) = cost(current) + distance (current→neighbor)
- step 5:
   find the minimum cost neighbor for the next starting point, and mark all visited nodes do not    do it two times.
- step 6:
  compare the calculated cost with the present cost. if the present cost is less than the calculated cost, replace it with the calculated cost to get the minimum cost between. if not just keep the present cost to that node.
### Map to be followed by the Robot
The image below is the map to be followed by the Robot with each nose and an estimated distance between them.
![image](https://github.com/user-attachments/assets/6ce49664-ca9f-4abd-84c5-e329f8ad9ef2)
### Requirement and installations
- To run the following code you must flash your eap32 with the latest bin file available on thonny for this we personoally    used the Variant of Espressive ESP32 WROOM with version 1.25.0.
- we use a couple of libriaries for both code's which included:
  1. Matplot lib: for ploting and visualisations.
  2. math: used for replacement on micropython to create arrays.
  3. json: Handles JSON enconding and decoding.
  4. time: provides timing for delays.
  5. socket: used for TCP/IP communication between webot and the ESP-32 over wiffi.
  6. network: to manage WI-FI interface.
  7. machine, Pin: Control the GPIO pins on the ESP-32.
### How to use the code's
- step 1: change the SSID and password using your network.
- step 2: make sure you are on the same network.
- step 3: Run the code to optain and IP-address which you later on add to the webot code.
- step 4: Run the simulation on wwebot, no need to close thonny since information is been sent over wifi.
### Communication between Webot and ESP-32 Flow chart
![image](https://github.com/user-attachments/assets/e0a810cc-e653-4eb5-95ad-c3e05979eb1a)






     
