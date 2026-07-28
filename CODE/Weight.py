from hx711_gpio import HX711
from machine import Pin
import time
import random

data_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
clock_pin = Pin(18, Pin.OUT)

RUN_DURATION_SEC = 30
FLUSH_INTERVAL_COUNT = 500 # save every 500 samples so that all data doesn't get lost in case of catastrophic failure but also doesn't impact loop times as much.

hx711 = HX711(clock_pin, data_pin)

hx711.tare()

unique_id = time.ticks_us() # avoids duplicate  filenames
filename = f"log_{unique_id}.csv"
print(f"Creating data file: {filename}")

with open(filename, "w") as f:
    f.write("timestamp_us,raw_reading\n")

file = open(filename, "a")

timestamps = [0] * FLUSH_INTERVAL_COUNT
readings = [0] * FLUSH_INTERVAL_COUNT

start_time_ms = time.ticks_ms()
end_time_ms = start_time_ms + (RUN_DURATION_SEC * 1000)

sample_count = 0
total_samples_saved = 0
buffer_index = 0

print("log start")

try:
    while(time.ticks_ms() < end_time_ms):
        raw_wt = hx711.read()
        scale_factor = (97/40700) * (9.81/1000) #gets grams then converts to newtons
        
        weight = raw_wt * scale_factor
        # time.ticks_us() avoids heavy memory allocation overhead
        timestamps[buffer_index] = time.ticks_us()
        readings[buffer_index] = weight
        
        #print data
        print(f"{weight:.1f} Newtons", end="     \r")
        
        buffer_index += 1
        sample_count += 1
        
        if buffer_index >= FLUSH_INTERVAL_COUNT:
            lines = "".join(
                f"{time.ticks_diff(timestamps[i], start_time_us) / 1000000.0:.6f},{readings[i]}\n" 
                for i in range(FLUSH_INTERVAL_COUNT)
            )
            file.write(lines)
            file.flush() 
            
            total_samples_saved += FLUSH_INTERVAL_COUNT
            buffer_index = 0
    if buffer_index > 0:
        lines = "".join(f"{timestamps[i]},{readings[i]}\n" for i in range(buffer_index))
        file.write(lines)
        total_samples_saved += buffer_index

finally:
    file.close()
    print("Log done.")
    print(f"Total samples recorded: {total_samples_saved}")
    print(f"Average sample rate: {round(total_samples_saved / RUN_DURATION_SEC, 2)} Hz")

