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
