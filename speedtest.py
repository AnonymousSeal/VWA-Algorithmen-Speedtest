#!/usr/bin/env python2
from time import time
from datetime import datetime
from primefac import *
from subprocess import check_output
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, BigInteger

#########################################

batch_size = 5
input_file = 'primeproducts.txt'
device = 'MacBook Pro (Mid 2014): 2.8 GHz Dual-Core Intel Core i5'

#########################################

db = create_engine('sqlite:///VWA-Algorithmus-Speedtest.db')
db.connect()
metadata = MetaData()

results = Table('results', metadata,
   Column('number', String, nullable=False),
   Column('prime1', String, nullable=False),
   Column('prime2', String, nullable=False),
   Column('ecm', String, nullable=False),
   Column('mpqs', String, nullable=False),
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
        ins = results.insert().values(number=result[0], prime1=result[1][0][2],
        prime2=result[1][0][3], ecm=result[1][0][1], mpqs=result[1][1][1])
        conn = db.connect()
        r = conn.execute(ins)
    # delete batch from primeproducts.txt
    with open(input_file, 'r') as f:
        remaining_lines = f.readlines()[batch_size:]
    with open(input_file, 'w') as f:
        for remaining_line in remaining_lines:
            f.write(remaining_line)

def ecm(n):
    start = time()
    output = check_output(['python', '-m', 'primefac', '-m=ecm ', str(n)])
    speed = time() - start
    _, p1, p2 = output.strip('\n').split(' ')
    return [speed, p1, p2]

def mpqs(n):
    start = time()
    output = check_output(['python', '-m', 'primefac', '-m=mpqs ', str(n)])
    speed = time() - start
    _, p1, p2 = output.strip('\n').split(' ')
    return [speed, p1, p2]


algorithms = {'ecm':ecm, 'mpqs':mpqs}

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

#######################################

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
