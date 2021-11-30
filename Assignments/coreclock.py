#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modified on Nov 2021

@author: OCG 404

Core clock to confirm parallel processing.
"""

if __name__ == '__main__':

	from dask.distributed import Client, LocalCluster
	
	from dask.distributed import progress
	import time
	cluster = LocalCluster()
	client = Client(cluster)
	print(client)



	# WRITE coreclock() module:
	# Take input, x.
	# Do operation on x (this is optional).
	# Sleep for 1 second.
	# Return x or f(x).


	
	# client.map(module,list) will distribute the operations of module on list, amongst
	# the available processes. Modify the inputs to client.map() to perform the coreclock()
	# module on 500 values of x.    
	# f = client.map(module,list_of_500_x)

	
	# Display and update the processor progress.
	progress(f)
