from microbit import*
import gc
import micropython


def mem_stat():
    print('MEMORY STATS')
    gc.collect()
    micropython.mem_info()
    print('Initial free: {} allocated: {}'.format(
        gc.mem_free(), gc.mem_alloc()))
    print('END OF REPORT')


sleep(500)
mem_stat()
# Output will be printed via serial (115200 baud rate)
