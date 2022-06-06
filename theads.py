from datetime import datetime 
import math

import threading
import multiprocessing

def main():
    cores = multiprocessing.cpu_count()
    print('Processando com %d cores' % cores)

    init = datetime.now()
    threads = []

    for n in range(1, cores + 1):
        ini = 50_000_000 * (n - 1) / cores
        fim = 50_000_000 * n / cores
        print(f'Core {n}: Processa {ini} a {fim}')
        threads.append(
            threading.Thread(
                target=compute,
                kwargs={'init': ini, 'final': fim},
                daemon=True
            )
        )
    
    [th.start() for th in threads]
    [th.join() for th in threads]

    time = datetime.now() - init
    print(f'Time: {time.total_seconds():.8f}')

def compute(final, init=1):
    pos = init
    fator = 1000 * 1000
    while pos < final:
        pos+=1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
    main()