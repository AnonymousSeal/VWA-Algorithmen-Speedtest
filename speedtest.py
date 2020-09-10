#!/usr/bin/env python3
from time import time
from datetime import datetime
from lenstra_algorithm.lenstra import lenstra
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, BigInteger

#########################################

batch_size = 5
input_file = 'primeproducts.txt'
device = 'MacBook Pro (Mid 2014): 2.8 GHz Dual-Core Intel Core i5'

#########################################

db = create_engine('sqlite:///VWA-Algorithmus_Speedtest.db')
db.connect()
metadata = MetaData()

results = Table('results', metadata,
   Column('number', String, nullable=False),
   Column('prime1', String, nullable=False),
   Column('prime2', String, nullable=False),
   Column('ecm', String, nullable=False),
   Column('device', String, default=device),
   Column('time_added', DateTime, default=datetime.utcnow))

metadata.create_all(db)

#########################################


def import_batch(input_file=input_file, batch_size=batch_size):
    # get batch from primeproducts.txt
    with open(input_file, 'r') as f:
        return [int(line.strip('\n')) for line in f.readlines()[:batch_size]]

def file_len(filename):
    with open(filename) as f:
        i = None
        for i, l in enumerate(f):
            pass
    return i + 1

def export_results(batch_results, input_file=input_file, batch_size=batch_size):
    for result in batch_results:
        ins = results.insert().values(number=result[0], prime1=result[1][0][1],
        prime2=result[1][0][2], ecm=result[1][0][3])
        conn = db.connect()
        r = conn.execute(ins)
    # delete batch from primeproducts.txt
    with open(input_file, 'r') as f:
        remaining_lines = f.readlines()[batch_size:]
    with open(input_file, 'w') as f:
        for remaining_line in remaining_lines:
            f.write(remaining_line)

def ecm(n):
    for i in range(10):
        if i > 3:
            print(i)
        start = time()
        result = lenstra(n, 1000*10**i)
        speed = time() - start
        if result is not False:
            p1, p2 = min(result, int(n/result)), max(result, int(n/result))
            return [p1, p2, speed]
    return [False, speed]

algorithms = {'ecm':ecm}

def speedtest(algorithms=algorithms, device=device):
    batch = import_batch()
    batch_results = []
    for number in batch:
        algorithm_results = []
        for algorithm in algorithms:
            p1, p2, speed = algorithms[algorithm](number)
            algorithm_results.append([algorithm, str(p1), str(p2), speed])
        batch_results.append([str(number), algorithm_results])
    export_results(batch_results)

#########################################

if __name__ == '__main__':
    file_length = file_len(input_file)
    print('===============================')
    print('running speedtest for %i numbers' % (file_length))
    print('input file: %s' % (input_file))
    print('batch size: %s' % (batch_size))
    print('device: %s' % (device))
    print('===============================')
    print('running batch...')
    for i in range(file_length//batch_size):
        speedtest()
        print('batch[' + str(i+1) + '/' + str(file_length//batch_size) + ']')
    print('finished...')
    print('you can now view the results in the database')
    print('===============================')
