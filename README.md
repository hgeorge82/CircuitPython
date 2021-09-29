# CircuitPython
My python notebook
# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here


### Evidence



### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code
Using a metro board and circuit python I programed a micro servo to turn 0 and 180°.


```python
from adafruit_motor import servo
import time
import board
import pwmio


# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

while True:
    print("forward")
    my_servo.throttle = 1.0
    time.sleep(2.0)
    print("stop")
    my_servo.throttle = 0.0
    time.sleep(2.0)
    print("reverse")
    my_servo.throttle = -1.0
    time.sleep(2.0)
    print("stop")
    my_servo.throttle = 0.0
    time.sleep(4.0)
```


### Evidence
<img src="Images/ServoGif.gif" alt="ServoGif" style="width:200px;">

### Wiring
![image](https://user-images.githubusercontent.com/71407017/133789559-d49ee117-f785-4d80-adae-6a994fef2e17.png)

### Reflection
I struggled with my code, but turns out it was just that I wired my servo wrong.

## CircuitPython Cap touch

### Description & Code

```
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

while True:
    print("forward")
    my_servo.throttle = 1.0
    time.sleep(2.0)
    print("stop")
    my_servo.throttle = 0.0
    time.sleep(2.0)
    print("reverse")
    my_servo.throttle = -1.0
    time.sleep(2.0)
    print("stop")
    my_servo.throttle = 0.0
    time.sleep(4.0)
```

### Evidence
![image](https://user-images.githubusercontent.com/71407017/134009936-093b8fb5-c762-445b-b3fc-ac347ece4b05.png)

### Wiring

### Reflection






## CircuitPython_LCD

### Description & Code

```python
import time

import board
import analogio


# Initialize analog input connected to photocell.
photocell = analogio.AnalogIn(board.A1)
photocell = analogio.AnalogIn(board.A2)

# Make a function to convert from analog value to voltage.
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

# Main loop reads value and voltage every second and prints them out.
while True:
    # Read the value, then the voltage.
    val = photocell.value
    volts = analog_voltage(photocell)
    # Print the values:
    print('Photocell value: {0} voltage: {1}V'.format(val, volts))
    # Delay for a second and repeat!
    time.sleep(1.0)
```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
