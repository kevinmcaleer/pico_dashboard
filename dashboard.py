# Pico Dashboard
# Kevin McAleer
# June 2022

import picodisplay2 as display
from chart import Chart
import gc 
width = display.get_width()
height = display.get_height()
print(f"width: {width}, height {height}")
gc.collect()
display_buffer = bytearray(width * height * 2)
display.init(display_buffer)

# Set the display backlight to 50%
display.set_backlight(0.5)

data = [10,11,9,13,2,10,12,10,10,9,7,11,10,11,9,13,2,10,12,10,10,9,7,11]

# Set the theme colour
THEME = {'red': 255, 'green': 126, 'blue': 121}
THEME2 = {'red': 252, 'green': 210, 'blue': 0}

# Frame background colour
BACKGROUND = {'red': 100, 'green': 100, 'blue': 100}

def draw_data():
    """ render the data on the graph, scaling to the axix """

def frame(x, y, w, h, colour):
    """ Draw a frame on the display """

    print(f'x: {x}, y: {y}, w: {w}, h: {h}')
    # Draw a frame
    display.set_pen(colour['red'], colour['green'], colour['blue'])
    display.rectangle(x, y, w, h)
#     display.clear()

    frame_width = 1

    display.set_pen(0, 0, 0)
    x1 = x+frame_width
    y1 = y+frame_width
    w1 = w-frame_width*2
    h1 = h-frame_width*2
    
    display.rectangle(x1, y1, w1, h1)
    print(f'x1: {x1}, y1: {y1}, w1: {w1}, h1: {h1}')

    display.set_pen(255, 255, 255)
    display.text("Pico Dashboard", 2, 2, w)

    # time to update the display
    display.update()

    bar_width = 5

border = 20
# frame(border,border,width-(border*2),height-(border*2),BACKGROUND)

temp_chart = Chart('Temperature', 'Time', 'Temperature', data)
temp_chart2 = Chart('Humidity', 'Time', 'Temperature', data)

temp_chart.data_colour = THEME
temp_chart2.data_colour = THEME2
temp_chart.title_colour = THEME
temp_chart2.title_colour = THEME2
temp_chart2.data_colour = THEME2
temp_chart.border_colour = BACKGROUND
temp_chart2.border_colour = BACKGROUND
temp_chart.border_width = 1
temp_chart2.border_width = 1

temp_chart.x = 0
temp_chart.y = 0
temp_chart.width = display.get_width()
temp_chart.height = display.get_height()//2

temp_chart2.x = 0
temp_chart2.y = (display.get_height()//2) + 1
temp_chart2.width = display.get_width()
temp_chart2.height = display.get_height()//2 - 1

temp_chart.update()
temp_chart2.update()