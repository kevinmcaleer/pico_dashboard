# Pico Dashboard
# Kevin McAleer
# June 2022

# import picodisplay2 as display
from pichart import Chart, Card, Container, Image_tile
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, DISPLAY_PICO_EXPLORER
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, rotate=0)
import gc 
import machine
from time import sleep
from random import randint
#  WIDTH, HEIGHT = 320, 240 # Pico Display 2.0
# WIDTH, HEIGHT = display.get_bounds()
WIDTH, HEIGHT = 240,240

#  display = ST7789(WIDTH, HEIGHT, rotate180=False)

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
LIGHT_ORANGE = {'red': 255, 'green': 195, 'blue': 110}

# Frame background colour
BACKGROUND = {'red': 255, 'green': 171, 'blue': 57}

border = 20
# frame(border,border,width-(border*2),height-(border*2),BACKGROUND)

chart1 = Chart(display, title='Temperature', x_values=data)
chart2 = Card(display, title='Humidity')
chart3 = Image_tile(display, filename='kev.jpg')

print(chart3.filename)
chart4 = Chart(display, title="Air Quality", x_values=data)

chart1.data_colour = WHITE
# chart3.data_colour = WHITE
chart4.data_colour = WHITE

chart1.title_colour = WHITE
chart2.title_colour = WHITE
# chart3.title_colour = WHITE
chart4.title_colour = WHITE

chart1.border_colour = WHITE
chart2.border_colour = WHITE
chart3.border_colour = WHITE
chart4.border_colour = WHITE

chart1.background_colour = BLUE
chart2.background_colour = GREEN
# chart3.background_colour = BLUE
chart4.background_colour = ORANGE

chart1.grid_colour = LIGHT_BLUE
chart2.grid_colour = LIGHT_BLUE
# chart3.grid_colour = LIGHT_BLUE
chart4.grid_colour = LIGHT_ORANGE

chart1.border_width = 1
chart2.margin = 30
# chart3.border_width = 1
chart4.border_width = 1

container = Container(display)
container.add_chart(chart4)
container.add_chart(chart3)
container.add_chart(chart2)
container.add_chart(chart1)

container.cols = 2

container.update()

chart2.show_bars = False
chart2.show_lines = True
chart3.data_point_radius = 2

chart3.show_datapoints = True
chart3.show_bars = False
chart3.show_labels = True
chart3.show_lines = True

chart4.show_labels = True
chart2.grid = False

# chart1.grid = True
# chart3.grid = False

# chart1.update()
# chart2.update()
# chart3.update()
# chart4.update()

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

data = [20,34]
chart1.x_values = data
chart2.x_values = data
# chart3.x_values = data
chart4.x_values = [0,50]

chart1.scale_data()
#chart3.scale_data()
chart4.scale_data()

data = []
air_quality_data = []

chart1.x_values = data
# chart3.x_values = data
chart4.x_values = air_quality_data

print(f'x: {chart3.x}, y: {chart3.y}, chart3.width {chart3.width}, chart3.height {chart3.height}')

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
#     chart3.x_values = data
    chart4.x_values = air_quality_data
#     print(chart1.x_values)##
    container.update()
    # chart1.update()
    # chart2.update()
    # chart3.update()
    # chart4.update()
    
    sleep(0.5)

