import utime

prevTime = {}


def tick(ms, callback):
    if (ms not in prevTime):
        prevTime[ms] = 0
    if utime.ticks_diff(utime.ticks_ms(), prevTime[ms]) > ms:
        callback()
        prevTime[ms] = utime.ticks_ms()
