from datetime import datetime 
import math

def main():
    init = datetime.now()
    compute(final=50_000_000)
    time = datetime.now() - init
    print(f'Time: {time.total_seconds():.2f}')

def compute(final, init=1):
    pos = init
    fator = 1000 * 1000
    while pos < final:
        pos+=1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
    main()