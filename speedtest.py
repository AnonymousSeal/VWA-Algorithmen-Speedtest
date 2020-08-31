#!/usr/bin/env python3
from lenstra_algorithm.lenstra import lenstra
from time import time
from datetime import datetime


algorithms = [lenstra]
input_file = 'primeproducts.txt'
output_file = 'results.txt'
batch_size = 10
device = 'MacBook Pro (Mid 2014): 2.8 GHz Dual-Core Intel Core i5'

def import_batch(input_file=input_file, batch_size=batch_size):
    # get batch from primeproducts.txt
    with open(input_file, 'r') as f:
        return [line.strip('\n') for line in f.readlines()[:batch_size]]

# https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
# ==================================================================================================
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
# ==================================================================================================

def export_results(results, output_file=output_file, input_file=input_file, batch_size=batch_size):
    # write test results to results.txt
    with open(output_file, 'a') as f:
        for result in results:
            f.write(result + '\n')
        f.write('\n')
    # delete batch from primeproducts.txt
    with open(input_file, 'r') as f:
        remaining_lines = f.readlines()[batch_size:]
    with open(input_file, 'w') as f:
        for remaining_line in remaining_lines:
            f.write(remaining_line)

def speedtest(algorithms=algorithms, device=device):
    batch = import_batch()
    results = []
    for data in batch:
        algorithm_results = []
        for algorithm in algorithms:
            start = time()
            result = algorithm(i)
            speed = time() - start
            algorithm_results.append(str(algorithm) + ' : ' + speed)
        results.append(data + ' | ' +
                    ', '.join(algorithm_results) + ' | ' +
                    str(datetime.utcnow()) + ' | ' +
                    device)
    export_results(results)

file_length = file_len(input_file)
for i in range(file_length//batch_size):
    speedtest()
