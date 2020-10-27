from matplotlib import pyplot as plt
import math

def get_numbers(filename):
    nums = [line.rstrip() for line in open(filename)]
    nums = nums[::2]
    numbers = []
    for num in nums:
        index = num.find(':')
        number = math.log(int(num[:index]), 10)
        numbers.append(number)
    return numbers

def get_timings(filename):
    timings = [line.rstrip() for line in open(filename)]
    timings = timings[1::2]
    timings = [time.strip('real\t') for time in timings]
    time_float = []
    for time in timings:
        m_index = time.find('m')
        minutes, seconds = time[:m_index], time[m_index+1:-1]
        time_float.append(float(minutes)*60 + float(seconds))
    return time_float

def array_log(inputlist):
    return [math.log(elem) for elem in inputlist]

fig, ax = plt.subplots()
ax.set_title("Speedtest")
ax.set_xlabel("Length of number (log(number))")
ax.set_ylabel("Time taken (log(seconds))")
ax.scatter(get_numbers('results/ecm.txt'), array_log(get_timings('results/ecm.txt')), label='ecm')
ax.scatter(get_numbers('results/mpqs.txt'), array_log(get_timings('results/mpqs.txt')), label='mpqs')
ax.scatter(get_numbers('results/basic.txt'), array_log(get_timings('results/basic.txt')), label='basic')
ax.legend(loc='upper left')
fig.savefig('results/plot0.png', dpi=1000, transperent=True)
fig.savefig('results/plot0.svg')

fig, ax = plt.subplots()
ax.set_title("Speedtest")
ax.set_xlabel("Length of number (log(number))")
ax.set_ylabel("Time taken (seconds)")
ax.scatter(get_numbers('results/ecm.txt'), get_timings('results/ecm.txt'), label='ecm')
ax.scatter(get_numbers('results/mpqs.txt'), get_timings('results/mpqs.txt'), label='mpqs')
ax.scatter(get_numbers('results/basic.txt'), get_timings('results/basic.txt'), label='basic')
ax.legend(loc='upper left')
fig.savefig('results/plot1.png', dpi=1000, transperent=True)
fig.savefig('results/plot1.svg')
