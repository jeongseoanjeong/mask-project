import RPi.GPIO as g
g.setwarnings(False)
g.setmode(g.BCM)
g.setup(17,g.OUT)
g.output(17,False)
