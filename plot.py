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
ax.set_xlabel("Länge der Zahl (als log)")
ax.set_ylabel("Laufzeit (in s)")
ax.scatter(get_numbers('results/ecm.txt'), get_timings('results/ecm.txt'), label='ECM')
ax.scatter(get_numbers('results/mpqs.txt'), get_timings('results/mpqs.txt'), label='QS')
ax.scatter(get_numbers('results/basic.txt'), get_timings('results/basic.txt'), label='Einf. Suchalg.')
ax.legend(loc='upper left')
fig.savefig('results/plot0.pdf')

fig, ax = plt.subplots()
ax.set_title("Speedtest")
ax.set_xlabel("Länge der Zahl (als log)")
ax.set_ylabel("Laufzeit (als log der s)")
ax.scatter(get_numbers('results/ecm.txt'), array_log(get_timings('results/ecm.txt')), label='ECM')
ax.scatter(get_numbers('results/mpqs.txt'), array_log(get_timings('results/mpqs.txt')), label='QS')
ax.scatter(get_numbers('results/basic.txt'), array_log(get_timings('results/basic.txt')), label='Einf. Suchalg.')
ax.set_yticks([])
ax.legend(loc='upper left')
fig.savefig('results/plot1.pdf')
