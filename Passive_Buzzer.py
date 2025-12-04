from machine import Pin, PWM
import time

# buzzer pin select (example: GPIO15)
buzzer = PWM(Pin(15))

def play_tone(frequency, duration):
    buzzer.freq(frequency)   # set frequency in Hz
    buzzer.duty_u16(32768)   # 50% duty cycle (max 65535)
    time.sleep(duration)
    buzzer.duty_u16(0)       # stop sound

# Example melody
play_tone(3000, 5)   # 1000 Hz tone for 0.5 sec
time.sleep(1)
play_tone(500, 5)    # 500 Hz tone for 0.5 sec
time.sleep(1)
play_tone(1500, 5)   # 1500 Hz tone for 0.5 sec

# Turn off buzzer completely
buzzer.deinit()
