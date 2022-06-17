# Pico Dashboard
# Kevin McAleer
# June 2022

# import picodisplay2 as display
from pichart import Chart
from st7789 import ST7789
import gc 
import machine
from time import sleep
WIDTH, HEIGHT = 320, 240 # Pico Display 2.0

display = ST7789(WIDTH, HEIGHT, rotate180=False)

gc.collect()

# Set the display backlight to 50%
display.set_backlight(1.0)

data = [10,11,9,13,2,10,12,10,10,9,7,11,10,11,9,13,2,10,12,10,10,9,7,11]

# Set the theme colour
THEME = {'red': 255, 'green': 126, 'blue': 121}
THEME2 = {'red': 252, 'green': 210, 'blue': 0}
THEME3 = {'red': 151, 'green': 250, 'blue': 121}

# Frame background colour
BACKGROUND = {'red': 100, 'green': 100, 'blue': 100}
GRID = {'red': 100//4, 'green': 100//4, 'blue': 100//4}

def draw_data():
    """ render the data on the graph, scaling to the axix """

border = 20
# frame(border,border,width-(border*2),height-(border*2),BACKGROUND)

chart1 = Chart(display, title='Temperature', x_values=data)
chart2 = Chart(display, title='Humidity', x_values=data)
chart3 = Chart(display, title="Pressure", x_values=data)

chart1.data_colour = THEME
chart2.data_colour = THEME2
chart3.data_colour = THEME3

chart1.title_colour = THEME
chart2.title_colour = THEME2
chart3.title_colour = THEME3

chart1.grid_colour = GRID
chart2.grid_colour = GRID
chart3.grid_colour = GRID

chart1.border_colour = chart2.border_colour = chart3.border_colour = BACKGROUND
# chart2.border_colour = BACKGROUND
#  = BACKGROUND

chart1.border_width = 1
chart2.border_width = 1
chart3.border_width = 1

chart1.x = 0
chart1.y = 0
chart1.width = WIDTH
chart1.height = HEIGHT//3

chart2.x = 0
chart2.y = HEIGHT//3*1
chart2.width = WIDTH
chart2.height = HEIGHT//3
chart2.data_point_radius = 2

chart3.x = 0
chart3.y = HEIGHT //3*2
chart3.width = WIDTH 
chart3.height = HEIGHT//3

chart2.show_bars = False
chart2.show_lines = True
chart3.data_point_radius = 2

chart3.show_datapoints = True
chart3.show_bars = False
# chart3.show_lines = True

chart1.grid = True
chart2.grid = True
chart3.grid = True

chart1.update()
chart2.update()
chart3.update()

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

data = [10,34]
chart1.x_values = data
chart2.x_values = data
chart3.x_values = data
chart1.scale_data()
chart2.scale_data()
chart3.scale_data()

data = []

chart1.x_values = data
chart2.x_values = data
chart3.x_values = data


while True or KeyboardInterrupt:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = int(27 - (reading - 0.706)/0.001721)
    data.append(temperature)
    print(data)
    if len(data) == 29:
        data.pop(0)
    chart1.x_values = data
    chart2.x_values = data
    chart3.x_values = data
    print(chart1.x_values)#
    chart1.update()
    chart2.update()
    chart3.update()
    sleep(0.5)

