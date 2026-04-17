# Port Status Monitoring Tool (POX + Mininet)

## Problem Statement
Monitor and log switch port status changes.

## Objective
- Detect port up/down events
- Log changes
- Generate alerts
- Display status

## Tools Used
- Mininet
- POX Controller
- Python

## Setup Steps
1. Install Mininet
2. Clone POX:
   git clone https://github.com/noxrepo/pox
3. Run controller:
   ./pox.py openflow.of_01 misc.port_monitor
4. Run Mininet:
   sudo mn --topo single,3 --controller remote

## Execution
- Run pingall
- Bring port down:
  link s1 h1 down
- Observe alerts

## Expected Output
- Alerts printed in terminal
- Port status displayed
- Logs saved in file

  ## Screenshots

### 🔹 Normal Network (Ping Test)
<img width="679" height="240" alt="Screenshot 2026-04-17 071633" src="https://github.com/user-attachments/assets/019309c3-21f8-4705-aa63-c92c6d5afaa1" />


### 🔹 Port Down Simulation
<img width="679" height="91" alt="Screenshot 2026-04-17 071721" src="https://github.com/user-attachments/assets/66a6027d-d1e7-42d7-9672-add0c8cf4619" />


### 🔹 Controller Alert
<img width="1040" height="221" alt="Screenshot 2026-04-17 071740" src="https://github.com/user-attachments/assets/8660383c-25da-4780-b3ed-e52c217291cf" />


### 🔹 Logs Output
<img width="846" height="312" alt="Screenshot 2026-04-17 071821" src="https://github.com/user-attachments/assets/a6f5aae7-456e-4c9e-916f-814057c2eae0" />

