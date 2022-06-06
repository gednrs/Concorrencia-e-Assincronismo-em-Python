from datetime import datetime 
import math
import asyncio

def main():
    el = asyncio.get_event_loop()
    init = datetime.now()
    # el.run_until_complete(compute(final=50_000_000))
    task1 = el.create_task(compute(final=10_000_000))
    task2 = el.create_task(compute(init=10_000_001, final=20_000_000))
    task3 = el.create_task(compute(init=20_000_001, final=30_000_000))
    task4 = el.create_task(compute(init=30_000_001, final=40_000_000))
    task5 = el.create_task(compute(init=40_000_001, final=50_000_000))

    tasks = asyncio.gather(task1, task2, task3, task4, task5)
    el.run_until_complete(tasks)
    time = datetime.now() - init
    print(f'Time: {time.total_seconds():.2f}')

async def compute(final, init=1):
    pos = init
    fator = 1000 * 1000
    while pos < final:
        pos+=1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
    main()