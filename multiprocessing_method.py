from datetime import datetime 
import math
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor

def main():
    cores = multiprocessing.cpu_count()

    init = datetime.now()
    with ProcessPoolExecutor(max_workers=cores) as executor:
        for n in range(1, cores + 1):
            ini = 50_000_000 * (n - 1) / cores
            fim = 50_000_000 * n / cores
            print(f'Processo {n}: Processa de {ini} a {fim}')
            executor.submit(compute, init=ini, final=fim)

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