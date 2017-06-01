import pyupm_mic as mic

m = mic.Microphone(0)

c = mic.thresholdContext()
c.averageReading = 0
c.runningAverage = 0
c.averagedOver = 2

while True:
    buffer = mic.uint16Array(128)
    len = m.getSampledWindow(2, 128, buffer)
    if len:
        t = m.findThreshold(c, 30, buffer, len)
        print t