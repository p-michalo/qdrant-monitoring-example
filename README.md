## Table of contents
* [Summary](#Summary)
* [Prerequisites](#Prerequisites)
* [Usage](#Usage)
* [Metrics](#Metrics)
* [Usage](#Usage)

## Summary
Script was created to monitor and logs system base metrics of CPU, RAM and DISK IO usage throughput during the startup period of the Qdrant vector database.

## Prerequisites:
- Linux based system (e.g. Ubuntu) - it requires to be run on Linux based systems
- python3 - e.g. to install on ubuntu "apt-get install python3"
- Python3 packages:
  - python3-psutil - e.g. to install on ubuntu `apt-get install python3-psutil`
  - python3-pygal - e.g. to install on ubuntu `apt install python3-pygal`
  - python3-prettytable - e.g. to install on ubuntu `apt install  python3-prettytable`
  - qdrant-client - e.g. pip install qdrant-client

## Usage:
 - To monitor system metrics during the startup period of Qdrant database run the script on the machine with Qdrant installed.
 - Before running the script update following parameters by editing the `monitor.py`:
    - `timeout` - put number of seconds after which script should finish collecting the results
    - `sampleInterval` - put the number of seconds to set interval of metrics sampling
    - `metricsPrintInterval` - put number of seconds to set interval metrics printing on the screen
    - `snapshotURL` - put URL of the snapshot to test
- Execute the script by running command from the directory with the scripts: `python3 monitor.py`
- Monitor the process by observing shown metrics on the terminal

> Script will finish monitoring automatically when timeout reached or can it be forced to quit by pressing CTRL-C!!

> Script at the end creates charts in svg format


## Metrics:
While running the script base system metrics are being collected.

	List of system metrics to monitor: 
		- CPU Percent (CPU%) - shows the current system-wide CPU utilization as a percentage
		- Memory Swap Used (MemSwU) - shows used swap memory in bytes
		- Memory Swap Percent (MemSw%) - shows the swap memory percentage usage calculated as (total - available) / total * 100
		- Memory Virtual Used (MemVUsed) - shows memory used
		- Memory Virtual Percent (MemV%) - the percentage usage calculated as (total - available) / total * 100.
		- Disk Write Count (DiskWC) - number of disk reads
		- Disk Read Count (DiskRC) - number of disk writes
		- Disk Busy Time (DiskBT) - disk time pent doing actual I/Os (in miliseconds)
		- Disk Write Time (DiskWT) - time spent writing to disk (in miliseconds)
		- Disk Read Time (DiskRT) - time spent reading to disk (in miliseconds)


		
## Results:
### Screen results
Below is an example of the screen results. Every next record is shown after defined interval when monitoring is running:
```bash
root@7416ac054043:/qdrant/storage# python3 test.py

Snapshot recovery is running under PID-> 2197
__________________________
Monitoring in progress ...
+------+--------+--------+------------+-------+--------+--------+--------+---------+--------+
| CPU% | MemSwU | MemSw% |  MemVUsed  | MemV% | DiskWC | DiskRC | DiskBT |  DiskWT | DiskRT |
+------+--------+--------+------------+-------+--------+--------+--------+---------+--------+
| 0.1  |   0    |  0.0   | 1411092480 |  20.9 | 70758  | 11568  | 255040 | 2766993 |  3324  |
+------+--------+--------+------------+-------+--------+--------+--------+---------+--------+
!!!!!!!!! Starting recovery with -> https://snapshots.qdrant.io/arxiv_titles-3083016565637815127-2023-05-29-13-56-22.snapshot
+------+--------+--------+------------+-------+--------+--------+--------+---------+--------+
| CPU% | MemSwU | MemSw% |  MemVUsed  | MemV% | DiskWC | DiskRC | DiskBT |  DiskWT | DiskRT |
+------+--------+--------+------------+-------+--------+--------+--------+---------+--------+
| 9.8  |   0    |  0.0   | 1408782336 |  20.8 | 70758  | 11568  | 255040 | 2766993 |  3324  |
+------+--------+--------+------------+-------+--------+--------+--------+---------+--------+
+------+--------+--------+------------+-------+--------+--------+--------+---------+--------+
| CPU% | MemSwU | MemSw% |  MemVUsed  | MemV% | DiskWC | DiskRC | DiskBT |  DiskWT | DiskRT |
+------+--------+--------+------------+-------+--------+--------+--------+---------+--------+
| 13.5 |   0    |  0.0   | 7086944256 |  88.8 | 50817  | 263253 | 561490 | 3646340 | 618483 |
+------+--------+--------+------------+-------+--------+--------+--------+---------+--------+
...
```
### File results
All the collected metrics are being saved into four svg files at the end of the script to show detailed CPU usage, Memory utilization, Disk utilization. Here are the examples:
![20240331-184338_cpuPercent.svg](results_examples%2F20240331-184338_cpuPercent.svg)
![20240331-184338_memSwap.svg](results_examples%2F20240331-184338_memSwap.svg)
![20240331-184338_memVirt.svg](results_examples%2F20240331-184338_memVirt.svg)
![20240331-184338diskIO.svg](results_examples%2F20240331-184338diskIO.svg)