from threading import Thread
import os, time, datetime, random, tracemalloc

tracemalloc.start()
children = 4
maxdelay = 6


def status():
    return ('Time: ' +
            str(datetime.datetime.now().time()) +
            '\t Malloc, Peak: ' +
            str(tracemalloc.get_traced_memory()))


def child(num):
    delay = random.randrange(maxdelay)
    print(f"{status()}\t\tProcess "
          f"{num}, PID: {os.getpid()}, Delay: {delay} seconds...")
    time.sleep(delay)
    print(f"{status()}\t\tProcess {num}: Done.")


if __name__ == '__main__':
    print(f'Parent PID: {os.getpid()}')
    threads = []
    for i in range(children):
        thread = Thread(target=child, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
