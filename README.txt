## Cache Simulator

### Introduction

The Cache Simulator is a software tool designed to simulate the behavior of a memory cache system and provide insights into
 its performance. This program allows you to explore various cache configurations and assess their impact on memory access patterns.

The primary goal of this simulator is to assist users in understanding how different cache parameters, such as cache size, 
mapping type, and replacement algorithm, affect memory access efficiency and the rate of cache hits and misses.

### Usage and Output

The Cache Simulator reads its configuration from an XML document and conducts memory read simulations based on the specified parameters. 
The simulation results are then saved to output files located in the `./output` directory relative to the `main.py` file.

By configuring the program via the XML document, users can explore different cache scenarios and assess the trade-offs between 
cache size, mapping strategies, and replacement algorithms.

### Getting Started

To use the Cache Simulator effectively, follow the instructions in this document for configuring the program using the provided XML 
file. Once configured, run the program to initiate the cache simulation. Analyze the generated output files to gain insights into cache 
performance and efficiency.

Whether you are studying cache systems, optimizing memory access patterns, or evaluating cache design choices, the Cache Simulator 
provides a valuable tool for exploring and understanding the behavior of memory caches.

# Configuration

The XML file is found in the same folder as your python files and is called config.xml

The XML configuration file should have the following structure:

<config>
    <memory_size>...</memory_size>
    <page_size>...</page_size>
    <cache_size>...</cache_size>
    <mapping_type>...</mapping_type>
    <k>...</k>
    <replacement_algorithm>...</replacement_algorithm>
    <num_reads>...</num_reads>
</config>

Replace ... with the desired values for each parameter as described below.

Configurable Parameters:

<memory_size>: Specify the total memory size. Use a format like "XKB," "XMB," or "XGB" where X is a 
positive integer representing the size (e.g., "256MB").

<page_size>: Set the page size for memory operations, following the same format as memory size (e.g., "4KB").

<cache_size>: Define the cache size using the same format as memory size (e.g., "64KB").

<mapping_type>: Choose the cache mapping type. Options include "direct," "associative," and "set-associative."

<k>: Specify the set size for set-associative mapping. If not applicable, use "null" 
(without quotes) or set to a positive integer (e.g., "4").

<replacement_algorithm>: Select the cache replacement algorithm. Options include "fifo" (First-In-First-Out) 
and "lru" (Least Recently Used).

<num_reads>: Set the number of memory read operations to simulate. Use a positive integer value.

Memory size, page size, cache size, and k must be values that could be 2^x where x is a positive integer.

## Understanding Output Files

The Cache Simulator generates three distinct output files, each providing valuable insights into the behavior and 
performance of the cache system. These output files are located in the `./output` directory relative to the `main.py` file:

### 1. `hit_replace.txt`

The `hit_replace.txt` file contains information related to cache hits, cache misses, and cache line replacements. 
Specifically, it includes:

- Hit Ratio: This section provides the hit ratio, expressed as a decimal. It represents the proportion of memory read 
operations that resulted in cache hits.

- Replace Count: This section details the number of times cache lines were replaced due to cache misses.

### 2. `spatial_locality.txt`

The `spatial_locality.txt` file offers insights into the spatial locality of memory access patterns. Spatial locality refers to 
the tendency of a program to access memory locations that are close to each other. This file includes:

- Memory Addresses: A list of memory addresses requested during the simulation.

- Request Count: The number of times each memory address was requested.

### 3. `temporal_locality.txt`

The `temporal_locality.txt` file provides information about the temporal locality of memory access patterns. Temporal locality 
refers to the tendency of a program to access the same memory locations repeatedly in a short time span. This file includes
- Memory Addresses: A list of memory addresses requested during the simulation, in the order in which they were accessed.

## Execution

To run the CPU scheduler simulator, follow these steps:

1. Open your console or terminal.

2. Navigate to the directory containing the simulator's source code and configuration files.

3. Ensure that you have configured the `config.xml` file to specify the desired simulation parameters.

4. Run the `main.py` script from the console by entering the following command:

--------------
python3 main.py
--------------