from gpiozero import OutputDevice, LED
from time import sleep

# gpio pins
enable_pin = 26
puls_pin = 19
direction_pin = 13

enable = OutputDevice(enable_pin)
puls = OutputDevice(puls_pin)
direction = OutputDevice(direction_pin)

steps_per_rotation = 1600

try:
    while True:
        direction.on() # if you wanna go in the reverse direction, try direction.off()

        num_rotations = int(input("Please insert number of rotations: "))
        
        for _ in range(num_rotations * steps_per_rotation):
            puls.on()
            sleep(0.0005)
            puls.off()
            sleep(0.0005)
        
        sleep(1)

except KeyboardInterrupt:
    enable.off()
