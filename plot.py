from matplotlib import pyplot as plt
import math

numbers = [math.log(int(line.rstrip()),10) for line in open('primeproducts.txt')]

nums = [line.rstrip() for line in open('ecm.txt')]
nums = nums[::2]
numbers = []
for num in nums:
    index = num.find(':')
    number = math.log(int(num[:index]), 10)
    numbers.append(number)

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

ecm_timings = get_timings('ecm.txt')
mpqs_timings = get_timings('mpqs.txt')

print(ecm_timings)
print(mpqs_timings)

fig, ax = plt.subplots()
ax.set_title("Speedtest")
ax.set_xlabel("Length of number (log(n))")
ax.set_ylabel("Time taken (seconds)")
ax.scatter(numbers, ecm_timings, label='ecm')
ax.scatter(numbers, mpqs_timings, label='mpqs')
ax.legend(loc='upper left')
plt.show()
