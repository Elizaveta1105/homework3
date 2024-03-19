from multiprocessing import cpu_count, Pool, current_process
from time import ctime


def factorize(*numbers):
    print(f'Start {ctime()}')
    for number in numbers:
        arr = [1]
        for i in range(2, number + 1):
            if number % i == 0:
                arr.append(i)
        yield arr
    print(f'End {ctime()}')


def factorize_cpu(*numbers):
    for number in numbers:
        arr = [1]
        for i in range(2, number + 1):
            if number % i == 0:
                arr.append(i)
        return arr


def init_worker():
    current_process().daemon = False


def worker(*numbers):
    print(f'Start cpu {ctime()}')
    with Pool(cpu_count(), initializer=init_worker) as pool:
        results = pool.map(factorize_cpu, numbers)
        print("Current process:", current_process().name)
    print(f'End cpu {ctime()}')
    return results


if __name__ == '__main__':
    a, b, c, d = worker(128, 255, 99999, 10651060)
    print("Results:", a, b, c, d)

a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
             1521580, 2130212, 2662765, 5325530, 10651060]
