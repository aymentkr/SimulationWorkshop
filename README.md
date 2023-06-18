# SimulationWorkshop

## The aim is to graphically represent workshop production (script page 25). 
To do this, individual machines are defined that have a certain capacity (script from page 33). 

To do this, jobs are defined that have different processing sequences and whose work steps take different amounts of time. 
There is no specific direction of flow in processing - parts can move back and forth between machines. 
This creates traffic jams in front of the individual machines. That means the parts must be in one Buffer stores wait until the next processing. It should be shown how the parts go from machine to machine, when they are on the machine for processing and when they are in the buffer store. The simulation should be able to be stopped at any time and the current status should be visible.
For each part, the throughput time (beginning of the 1st machine to the end of the last machine), the processing time (the time it spent on the machines) and the idle time (the time the part spent in the buffer stores) and the downtime of the machines (the time when no part is being processed and the next part is being waited for).
Data is provided and may need to be converted to an SQL database. 
The result is delivered in the form of an app or exe and the associated source code.
