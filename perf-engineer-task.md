Hello! This is a test task for the position of Test/Performance Engineer at Qdrant.

## Motivation

At Qdrant, we highly prioritize the performance of the system.
A key responsibility of the performance engineer is to identify potential bottlenecks and areas of resource over-utilization.
It is important to pinpoint the locations of these bottlenecks with as much precision as possible to enable developers to fix the problem with minimal delay.

## Objective

Your task is to create a script in Bash or Python that monitors and logs the CPU, RAM, and Disk IO usage throughout the startup period of the Qdrant vector database.
This database should be initialized with a pre-existing dataset (for instance, one from this list: https://qdrant.tech/documentation/datasets/#available-datasets, although smaller datasets are also acceptable).

Your script must generate a chart that displays the resource usage over time, from the start to the end of the database's startup process.
The end of the process can be determined either by a specified timeout parameter or by the script being stopped manually.

The test task should be submitted as a GitHub repository.
This repository should include detailed instructions for installing dependencies, running the script, and examples of the results produced by the script.

The use of any external, open-source tools is permitted.
