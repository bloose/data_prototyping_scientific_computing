#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modified on Nov 2021

@author: OCG 404

Core clock to confirm parallel processing.
"""

if __name__ == '__main__':

    # Load these two functions from dask.distributed
	from dask.distributed import Client, LocalCluster
	
	from dask.distributed import progress
	import time
	cluster = LocalCluster()
	client = Client(cluster)
	print(client)



	# WRITE coreclock() module that does the following:
	# 1. Take input, x.
	# 2. Do operation on x (this is optional).
	# 3. Sleep for 1 second. (This is the key line for testing that parallel processing is working.
	# 4. Return x or f(x).

	
	# Use the funciton client.map(module,list_of_x) to distribute the operations of 'module' on 'list_of_x', amongst
	# the available cpus. Modify the inputs to client.map() to perform the coreclock()
	# module on a list of 500 values of x.    
	# f = client.map(module,list_of_500_x)

	
	# Display and update the processor progress.
	progress(f)

    # Don't forget to include code to measure the start time and end time for this entire script to run.
    # Use that start and end time to compute a dt and compare with the time you expected it to run if using
    # only one cpu.  For further instruction, refer back to HPC_Parallel_Processing.ipynb.
