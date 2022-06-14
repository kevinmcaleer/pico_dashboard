import picodisplay2 as display

class Chart:
    __title = ''
    __x_label = ''
    __y_label = ''
    __x_values = []
    __x_scale = 1
    __y_scale = 1
    __x_offset = 0
    __y_offset = 0
    __x_range = 0
    __y_range = 0
    __background_colour = {'red': 0, 'green': 0, 'blue': 0}
    __grid_colour = {'red': 0, 'green': 0, 'blue': 0}
    __border_colour = {'red': 0, 'green': 0, 'blue': 0}
    __title_colour = {'red': 0, 'green': 0, 'blue': 0}
    __data_colour = {'red': 0, 'green': 0, 'blue': 0}
    __data_point_radius = 1
    __data_point_width = 10
    __data_point_height = 1
    __data_point_x_offset = 0
    __data_point_y_offset = 0
    __x = 0
    __y = 0
    __width = 100
    __height = 100
    __border_width = 2
    __text_height = 40

    def __init__(self, title, x_label, y_label, x_values):
        self.__title = title
        self.__x_label = x_label
        self.__y_label = y_label
        self.__x_values = x_values

    @property
    def border_width(self):
        """ Get the border width """
        return self.__border_width

    @border_width.setter
    def border_width(self, border_width):
        """ Set the border width """
        self.__border_width = border_width

    @property
    def x(self):
        """ Get the x position of the chart """
        return self.__x

    @x.setter
    def x(self, x):
        """ Set the x position of the chart """
        self.__x = x

    @property   
    def y(self):
        """ Get the y position of the chart """
        return self.__y

    @y.setter
    def y(self, y):
        """ Set the y position of the chart """
        self.__y = y

    @property
    def width(self):
        """ Get the width of the chart """
        return self.__width

    @width.setter
    def width(self, width):
        """ Set the width of the chart """
        self.__width = width
        
    @property
    def height(self):
        """ Get the height of the chart """
        return self.__height

    @height.setter
    def height(self, height):
        """ Set the height of the chart """
        self.__height = height

    @property
    def data_colour(self):
        """ Get the data colour """
        return self.__data_colour

    @data_colour.setter
    def data_colour(self, colour):
        """ Set the data colour """
        self.__data_colour = colour

    @property
    def title_colour(self):
        """ Get the title colour """
        return self.__title_colour

    @title_colour.setter
    def title_colour(self, colour):
        """ Set the title colour """
        self.__title_colour = colour

    @property
    def border_colour(self):
        """ Get the border colour """
        return self.__border_colour

    @border_colour.setter
    def border_colour(self, colour):
        """ Set the border colour """
        self.__border_colour = colour
        
    @property
    def x_scale(self):
        return self.__x_scale

    @x_scale.setter
    def x_scale(self, value):
        self.__x_scale = value

    @property
    def y_scale(self):
        return self.__y_scale

    @y_scale.setter
    def y_scale(self, value): 
        self.__y_scale = value

    @property
    def x_offset(self):
        return self.__x_offset

    @x_offset.setter        
    def x_offset(self, value):
        self.__x_offset = value

    def set_y_offset(self, value):
        self.__y_offset = value

    def set_x_range(self, value):
        self.__x_range = value

    def set_y_range(self, value):
        self.__y_range = value

    def set_x_axis_colour(self, red, green, blue):
        self.x_axis_colour = {'red': red, 'green': green, 'blue': blue}

    @property
    def title(self):
        """ Get the title """
        return self.__title
    
    @title.setter
    def title(self, title):
        """ Set the title """
        self.__title = title
        
    def draw_border(self):
        display.set_pen(self.__border_colour['red'], self.__border_colour['green'], self.__border_colour['blue'])
        x = self.__x
        y = self.__y 
        w = self.__width
        h = self.__height
        display.rectangle(x, y, w, h)
        display.set_pen(self.__background_colour['red'], self.__background_colour['green'], self.__background_colour['blue'])

        x = self.__x + self.border_width
        y = self.__y + self.border_width
        w = self.__width - (self.__border_width * 2)
        h = self.__height - (self.__border_width * 2)
        display.rectangle(x, y, w, h)
        
        # Draw the border
        display.update()

    def update(self):
        # Draw border
        self.draw_border()

        display.set_pen(self.__title_colour['red'], self.__title_colour['green'], self.__title_colour['blue'])
        display.text(self.title, self.x+self.__border_width+1, self.y + self.__border_width+1,self.__width)

        # Update the display
        # display.update()

        # Scale the data
        min_val = min(self.__x_values)  # get the minimum value
        max_val = max(self.__x_values)  # get the maximum value

        # Calculate the scale
        self.__y_scale = (((self.__height - self.__text_height) - self.__border_width * 2)) / (max_val - min_val)
        
        # print(f'Min: {min_val} Max: {max_val}, Scale: {self.__y_scale}')

        display.set_pen(self.__data_colour['red'], self.__data_colour['green'], self.__data_colour['blue'])

        self.__x_offset = self.__x+self.__border_width+1
        self.__y_offset = (self.__height-self.__border_width)-1

        x_pos = self.x + self.__x_offset
        y_pos = self.y + self.__y_offset 
        for item in self.__x_values:
            item = int(item * self.__y_scale) # scale the data
            data_height = int(item)
            display.rectangle(x_pos, y_pos-item, self.__data_point_width, data_height)
            print(item)
            x_pos += self.__data_point_width + 1
            print(f'x_pos: {x_pos}, y_pos: {y_pos}')

        display.update()
