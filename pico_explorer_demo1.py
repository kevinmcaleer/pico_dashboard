# Pico Dashboard
# Kevin McAleer
# June 2022

# import picodisplay2 as display
from pichart import Chart, Card, Container
from colour import hsv2rgb, rgb2hsv, fade
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, DISPLAY_PICO_EXPLORER
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, rotate=0)
import gc 
import machine
from time import sleep
from random import randint
import jpegdec 
#  WIDTH, HEIGHT = 320, 240 # Pico Display 2.0
# WIDTH, HEIGHT = display.get_bounds()
WIDTH, HEIGHT = 240,240

#  display = ST7789(WIDTH, HEIGHT, rotate180=False)

gc.collect()

data = [10,11,9,13,2,10,12,10,10,9,7,11,10,11,9,13,2,10,12,10,10,9,7,11]

# Set the theme colour
THEME = {'red': 255, 'green': 171, 'blue': 57}
THEME2 = {'red': 252, 'green': 193, 'blue': 109}
THEME3 = {'red': 151, 'green': 250, 'blue': 121}
WHITE = {'red': 255, 'green': 255, 'blue': 255}
LIGHT_GREY = {'red': 240, 'green': 240, 'blue': 240}
BLUE = {'red': 20, 'green': 155, 'blue': 206}
LIGHT_BLUE = {'red': 55, 'green': 170, 'blue': 213}
BLACK = {'red': 0, 'green': 0, 'blue': 0}
GREEN = {'red': 0, 'green': 220, 'blue': 0}

LIGHT_GREEN = fade(GREEN, WHITE, 0.15)
DARK_GREEN = fade(GREEN, BLACK, 0.15)
ORANGE = {'red': 255, 'green': 171, 'blue': 57}
LIGHT_ORANGE = {'red': 255, 'green': 195, 'blue': 110}

# Frame background colour
BACKGROUND = {'red': 255, 'green': 171, 'blue': 57}

border = 20
# frame(border,border,width-(border*2),height-(border*2),BACKGROUND)

chart1 = Chart(display, title='Temperature', x_values=data)
chart2 = Card(display, title='Humidity')
chart3 = Chart(display, title="Pressure", x_values=data)
chart4 = Chart(display, title="Air Quality", x_values=data)

chart1.background_colour = BLACK
chart1.data_colour = WHITE
chart1.title_colour = WHITE
chart1.border_colour = WHITE
chart1.grid_colour = DARK_GREEN

chart1.border_width = 1
chart2.margin = 30
chart3.border_width = 1
chart4.border_width = 1

container = Container(display)
container.add_chart(chart1)
container.add_chart(chart2)
container.add_chart(chart3)
container.add_chart(chart4)

container.background_colour = BLACK
container.grid_colour = DARK_GREEN
container.data_colour = WHITE
container.title_colour = WHITE
container.border_colour = GREEN
container.border_width = 1

chart2.show_bars = False
chart2.show_lines = True
chart3.data_point_radius = 2

chart3.show_datapoints = True
chart3.show_bars = False
chart3.show_labels = True
chart3.show_lines = True

chart4.show_labels = True

container.cols = 2

container.update()

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

data = [20,34]
chart1.x_values = data
chart2.x_values = data
chart3.x_values = data
chart4.x_values = [0,50]

chart1.scale_data()
chart3.scale_data()
chart4.scale_data()

data = []
air_quality_data = []

chart1.x_values = data
chart3.x_values = data
chart4.x_values = air_quality_data

while True or KeyboardInterrupt:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = int(27 - (reading - 0.706)/0.001721)
    data.append(temperature)
    air_quality_data.append(randint(0, 50))
    print(data)
    if len(data) == 15:
        data.pop(0)
    if len(air_quality_data) == 15:
        air_quality_data.pop(0)
    chart1.x_values = data
    chart2.title = str(data[-1])
    chart3.x_values = data
    chart4.x_values = air_quality_data

    container.update()
    
    sleep(0.5)

