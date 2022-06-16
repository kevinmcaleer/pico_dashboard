# Pico Dashboard
# Kevin McAleer
# June 2022

# import picodisplay2 as display
from chart import Chart
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
THEME = {'red': 255, 'green': 171, 'blue': 57}
THEME2 = {'red': 252, 'green': 193, 'blue': 109}
THEME3 = {'red': 151, 'green': 250, 'blue': 121}
WHITE = {'red': 255, 'green': 255, 'blue': 255}
LIGHT_GREY = {'red': 240, 'green': 240, 'blue': 240}
BLUE = {'red': 0, 'green': 0, 'blue': 255}
GREEN = {'red': 0, 'green': 220, 'blue': 0}

display.set_pen(WHITE['red'],WHITE['green'], WHITE['blue'])
display.rectangle(0,0,WIDTH,HEIGHT)
display.update()

# Frame background colour
BACKGROUND = {'red': 255, 'green': 171, 'blue': 57}

border = 20
# frame(border,border,width-(border*2),height-(border*2),BACKGROUND)

chart1 = Chart(display, title='Temperature', x_values=data)
chart2 = Chart(display, title='Humidity', x_values=data)
chart3 = Chart(display, title="Pressure", x_values=data)

chart1.data_colour = THEME
chart2.data_colour = BLUE
chart3.data_colour = GREEN

chart1.title_colour = THEME
chart2.title_colour = BLUE
chart3.title_colour = GREEN

chart1.border_colour = BACKGROUND
chart2.border_colour = BLUE
chart3.border_colour = GREEN
chart1.background_colour = WHITE
chart2.background_colour = WHITE
chart3.background_colour = WHITE

chart1.grid_colour = LIGHT_GREY
chart2.grid_colour = LIGHT_GREY
chart3.grid_colour = LIGHT_GREY


chart1.border_width = 1
chart2.border_width = 1
chart3.border_width = 1

chart1.x = 0
chart1.y = 0
chart1.width = WIDTH//2 
chart1.height = HEIGHT //2 

chart2.x = (WIDTH//2 * 1)  
chart2.y = 0
chart2.width = WIDTH//2 
chart2.height = HEIGHT //2 
chart2.data_point_radius = 2

chart3.x = 0
chart3.y = HEIGHT //2 
chart3.width = WIDTH
chart3.height = HEIGHT //2

chart2.show_bars = False
chart2.show_lines = True
chart3.data_point_radius = 2

chart3.show_datapoints = True
chart3.show_bars = False
chart3.show_labels = True
chart3.show_lines = True

chart1.grid = True
chart3.grid = False

chart1.update()
chart2.update()
chart3.update()

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

data = [20,34]
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

