# micropython-automatic-watering
micropython automatic watering


his code was developed to be used with nodemcu esp8266, but can be modified to work with other boards (esp32, raspberry pi pico and pyboard).

micropython https://micropython.org/


## nodemcu pins
| Micropython  | NodeMCU   |
| ------------ | ------------ |
|   0 | D3  |
|   2|D4  |
|   4|D2  |
|  5 |D1   |
|  9 | SD2  |
|  10 |  SD3 |
| 12  |  D6 |
|  13 | D7  |
|  14 | D5  |
|  15 | D8  |
|  16 |D0|

### the following pins were used in the code
#### pin 0 = D3  - relay 1.
#### pin 12 = D6 - relay 2.
#### pin 15 = D8 - soil moisture sensor.
