from pyo import *
import time

s = Server().boot()
s.start()

osc = Sine(freq=440, mul=0.2).out()

print("Reproduciendo 440 Hz")
time.sleep(2)

osc.stop()
s.stop()
