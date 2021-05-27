import time

bt = time.time()
def lt(bt):
    return time.time() - bt

def log(msg):
    return '%s (%.3fs)' % (msg,lt(bt))

def nlen(n):
    r = 0
    while n != 0:
        n //= 10
        r += 1
    return r

print(log("Initializing..."))

print(log("Loading modules..."))
from guietta import B, G, R1, Gui, Quit, Exceptions, HSeparator, VSeparator, _, ___, III
import random

print(log("Rendering screen... (1/3)"))
numinput = Gui(
    ['<center>Starting Number:</center>', '__start__', '<center>Ending Number:</center>', '__end__']
)
numinput.fonts(
    [('Maplestory', 13), _, ('Maplestory', 13), _]
)

print(log("Rendering screen... (2/3)"))
resultscreen = Gui(
    ['Result:', 'result']
)
resultscreen.fonts(
    [('Maplestory', 17),('D2Coding', 15, 50)]
)

print(log("Rendering screen... (3/3)"))
gui = Gui(
    ["<center>Random Picker!</center>",   ___  , B('Go!')],
    [HSeparator],
    [             G('Input')             ,   ___  ,   ___   ],
    [HSeparator],
    [             G('Output')            ,   ___  ,    _    ],
    [                  _                 ,    _   ,   Quit  ],
    exceptions = Exceptions.SILENT
)
gui.Input = numinput
gui.Output = resultscreen
gui.fonts(
    [('NanumSquare', 17, 100),_,('NanumSquare', 11, 80)],
    [_],
    [('NanumSquare', 13, 80)],
    [_],
    [('NanumSquare', 13, 80)],
    [_,_,('NanumSquare', 11, 80)]
)

print(log("Configuring functions..."))
numlimit = 200
with gui.Go:
    if not gui.is_running:
        resultscreen.result = ''
    else:
        try:
            start = int(numinput.start)
            end = int(numinput.end)
        except Exception as e:
            resultscreen.result = e
        n = end - start + 1
        if n <= 0:
            resultscreen.result = '?'
        elif n > numlimit:
            resultscreen.result = 'Please try less than %d' % numlimit
        else:
            try:
                pick = random.sample(range(start, end+1), n)
                ret = ''
                for i in range(max(0, n//10)+1):
                    ret += ', '.join(str(x).rjust(nlen(end)) for x in pick[10*i:10*(i+1)]) + '\n'
                resultscreen.result = ret.rstrip()
            except Exception as e:
                resultscreen.result = e

print(log("Starting..."))
gui.run()

print(log("Closing..."))
