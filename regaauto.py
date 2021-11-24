import machine
import time

#pin 0 = D3
#pin 12 = D6
#pin 15 = D8

relay1 = machine.Pin(0, machine.Pin.OUT)
relay2 = machine.Pin(12, machine.Pin.OUT)
sensor = machine.Pin(15, machine.Pin.IN)
relay1.value(1)
relay2.value(1)

def verificar():
    while True:
        print(sensor.value())
        valor_sensor = sensor.value()
        time.sleep(2)
        if valor_sensor == 0:
            relay1.value(1)
            relay2.value(1) 
        else:
            relay1.value(0)
            relay2.value(0)
            

verificar()
    
