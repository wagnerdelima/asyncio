from multiprocessing import Process
import os, time, datetime, tracemalloc

tracemalloc.start()
children = 100
maxdelay = 6


def status():
    return ('Time: ' +
            str(datetime.datetime.now().time()) +
            '\t Malloc, Peak: ' +
            str(tracemalloc.get_traced_memory()))


def child(num):
    delay = maxdelay
    print(f"{status()}\t\tProcess "
          f"{num}, PID: {os.getpid()}, Delay: {delay} seconds...")
    time.sleep(delay)
    print(f"{status()}\t\tProcess {num}: Done.")


if __name__ == '__main__':
    start = time.time()
    print(f'Parent PID: {os.getpid()}')
    processes = []
    for i in range(children):
        proc = Process(target=child, args=(i,))
        proc.start()

        processes.append(proc)

    for proc in processes:
        proc.join()

    end = time.time()
    print(f'Slapsed time: {end-start}')
