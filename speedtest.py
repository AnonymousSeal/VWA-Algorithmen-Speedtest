#!/usr/bin/env python3
from lenstra_algorithm.lenstra import lenstra
from time import time
from datetime import datetime


input_file = 'primeproducts.txt'
output_file = 'results.txt'
batch_size = 2
device = 'MacBook Pro (Mid 2014): 2.8 GHz Dual-Core Intel Core i5'

def import_batch(input_file=input_file, batch_size=batch_size):
    # get batch from primeproducts.txt
    with open(input_file, 'r') as f:
        return [int(line.strip('\n')) for line in f.readlines()[:batch_size]]

# https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
# ==================================================================================================
def file_len(fname):
    with open(fname) as f:
        #i = None
        for i, l in enumerate(f):
            pass
        if i is None:
            print('file empty')
            return 0
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

def ecm(n):
    for i in range(10):
        start = time()
        result = lenstra(n, 1000*10**i)
        speed = time() - start
        if result is not False:
            return [result, speed]
    return [result, speed]

algorithms = [ecm]

def speedtest(algorithms=algorithms, device=device):
    batch = import_batch()
    results = []
    for data in batch:
        algorithm_results = []
        for algorithm in algorithms:
            result, speed = algorithm(data)
            algorithm_results.append(str(algorithm) + ' : ' + str(result) + ' | ' + str(speed))
        results.append(str(data) + ' | ' + ', '.join(algorithm_results) + ' | ' + str(datetime.utcnow()) + ' | ' + device)
    export_results(results)

if __name__ == '__main__':
    file_length = file_len(input_file)
    print('===============================')
    print('running speedtest for %i numbers' % (file_length))
    print('input file: %s' % (input_file))
    print('output file: %s' % (output_file))
    print('batch size: %s' % (batch_size))
    print('device: %s' % (device))
    print('===============================')
    print('running batch...')
    for i in range(file_length//batch_size):
        speedtest()
        print('batch[' + str(i+1) + '/' + str(file_length//batch_size) + ']')
    print('finished...')
    print('you can now view the results in the output_file')
    print('===============================')
