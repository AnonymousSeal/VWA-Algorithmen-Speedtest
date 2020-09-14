from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from random import randint
import geckodriver_autoinstaller


batch_size = 5
per_bit = 1
min_length = 8
max_length = 12
number_file = 'primeproducts.txt'

geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists and if it doesn't exist, download it automatically, then add geckodriver to path

def file_len(filename):
    with open(filename) as f:
        i = None
        for i, l in enumerate(f):
            pass
    return i + 1

def get_number(bit_len=128):
    binary_len = driver.find_element_by_id('prime')
    submit = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/table/tbody/tr/td/form/p/input[2]')
    binary_len.clear()
    binary_len.send_keys(bit_len)
    submit.click()
    return driver.find_element_by_id('random3').get_property('value')

def make_int(num):
    out_num = ''
    while len(num) > 3:
        out_num = num[-3:] + out_num
        num = num[:-4]
    return int(num + out_num)

def export_prime_products(prime_products, number_file=number_file):
    with open(number_file, 'a') as f:
        for prime_product in prime_products:
            f.write(prime_product + '\n')

def main(size=per_bit*batch_size, max_length=max_length, min_length=min_length, number_file=number_file):
    file_length = file_len(number_file)
    for i in range(min_length + (file_length//size), max_length + 1):
        numbers = []
        bit_length = i
        for j in range(size):
            # rather hacky but it helpes and the programm almost never crashes
            try:
                numbers.append(str(make_int(get_number(bit_len=bit_length))))
            except:
                try:
                    print('request failed - trying again...')
                    numbers.append(str(make_int(get_number(bit_len=bit_length))))
                except:
                    print('failed twice')
                    exit()
        export_prime_products(numbers)
        print('batch[' + str(i-min_length+1) + '/' + str(max_length-min_length+1) + ']')

def sort_em(number_file=number_file):
    with open(number_file, 'r') as f:
        numbers = [int(line.strip('\n')) for line in f.readlines()]
    numbers = sorted(numbers)
    i = 1
    while i < len(numbers):
        if numbers[i] == numbers[i-1]:
            del numbers[i]
            i -= 1
        i += 1
    numbers = [str(number) for number in numbers]
    open(number_file, 'w').close()
    export_prime_products(numbers)



if __name__ == '__main__':
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        print('accessing https://asecuritysite.com/encryption/random3')
        driver.get('https://asecuritysite.com/encryption/random3')

        print('fetching content...')
        main()

        print('sorting the numbers by size...')
        sort_em()

        driver.quit()
    finally:
        try:
            brower.close()
        except:
            pass
