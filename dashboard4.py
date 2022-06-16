# Pico Dashboard4 - for smaller displays
# Kevin McAleer
# June 2022

# import picodisplay2 as display
from chart import Chart
from st7789 import ST7789
import gc 
import machine
from time import sleep
from random import randint
# WIDTH, HEIGHT = 320, 240 # Pico Display 2.0
WIDTH, HEIGHT = 240, 135 # Pico Display Pack

display = ST7789(WIDTH, HEIGHT, rotate180=False)

gc.collect()

# Set the display backlight to 50%
display.set_backlight(1.0)



data = [10,11,9,13,2,10,12,10,10,9,7,11,10,11,9,13,2,10,12,10,10,9,7,11]

# Set the theme colour
THEME = {'red': 255, 'green': 171, 'blue': 57}
THEME2 = {'red': 252, 'green': 193, 'blue': 109}
THEME3 = {'red': 151, 'green': 250, 'blue': 121}
WHITE = {'red': 255, 'green': 255, 'blue': 255}
LIGHT_GREY = {'red': 240, 'green': 240, 'blue': 240}
BLUE = {'red': 20, 'green': 155, 'blue': 206}
LIGHT_BLUE = {'red': 55, 'green': 170, 'blue': 213}
GREEN = {'red': 0, 'green': 220, 'blue': 0}
ORANGE = {'red': 255, 'green': 171, 'blue': 57}
LIGHT_ORANGE = {'red': 255, 'green': 179, 'blue': 94}

# Frame background colour
BACKGROUND = {'red': 255, 'green': 171, 'blue': 57}

border = 20
# frame(border,border,width-(border*2),height-(border*2),BACKGROUND)

chart1 = Chart(display, title='Temperature', x_values=data)
chart1.data_colour = WHITE
chart1.title_colour = WHITE
chart1.border_colour = WHITE
chart1.background_colour = BLUE
chart1.grid_colour = LIGHT_BLUE
chart1.border_width = 1

chart1.x = 0
chart1.y = 0
chart1.width = WIDTH
chart1.height = HEIGHT
chart1.grid = True
chart1.update()
chart1.show_labels = True
chart1.show_lines = True
chart1.show_bars = False
chart1.show_datapoints = True

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

data = [20,34]
chart1.x_values = data
chart1.scale_data()
data = []
chart1.x_values = data

while True or KeyboardInterrupt:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = int(27 - (reading - 0.706)/0.001721)
    data.append(temperature)
    print(data)
    if len(data) == 29:
        data.pop(0)

    chart1.x_values = data

    print(chart1.x_values)#
    chart1.update()
    sleep(0.5)