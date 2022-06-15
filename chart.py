class Chart:
    __title = ''
    __x_label = ''
    __y_label = ''
    __x_values = []
    __x_scale = 1
    __y_scale = 1
    __x_offset = 0
    __y_offset = 0
    background_colour = {'red': 0, 'green': 0, 'blue': 0}
    border_colour = {'red': 0, 'green': 0, 'blue': 0}
    grid_colour = {'red':border_colour['red']//4, 'green':border_colour['green']//4,'blue':border_colour['blue']//4}
    __title_colour = {'red': 0, 'green': 0, 'blue': 0}
    __data_colour = {'red': 0, 'green': 0, 'blue': 0}
    __data_point_radius = 2
    __data_point_radius2 = __data_point_radius * 4
    __data_point_width = 10
    __data_point_height = 1
    __data_point_x_offset = 0
    __data_point_y_offset = 0
    x = 0
    y = 0
    __width = 100
    __height = 100
    border_width = 2
    __text_height = 16
    __show_datapoints = False
    __show_lines = False
    __show_bars = True
    __show_labels = False
    grid = True
    grid_spacing = 10

    def __init__(self, display, title=None, x_label=None, y_label=None, x_values=None, y_values=None):
        self.display = display
        if title: self.__title = title
        if x_label: self.__x_label = x_label
        if y_label: self.__y_label = y_label
        if x_values:
            # Scale the data
            self.__x_values = x_values
            self.min_val = min(self.__x_values)  # get the minimum value
            self.max_val = max(self.__x_values)  # get the maximum value
        if y_values: self.__y_values = y_values

    @property
    def show_bars(self):
        """ Get the show_bars value """
        return self.__show_bars

    @show_bars.setter
    def show_bars(self, value):
        """ Set the show_bars value """
        self.__show_bars = value

    @property
    def show_datapoints(self):
        """ Get Show the data points status """
        return self.__show_datapoints

    @show_datapoints.setter
    def show_datapoints(self, value):
        """ Set Show the data points status"""
        self.__show_datapoints = value

    @property
    def show_lines(self):
        """ Get Show the lines status """
        return self.__show_lines

    @show_lines.setter
    def show_lines(self, value):
        """ Set Show the lines status"""
        self.__show_lines = value

    @property
    def data_point_radius(self):
        """ Get the radius of the data points """
        return self.__data_point_radius

    @data_point_radius.setter
    def data_point_radius(self, value):
        """ Set the radius of the data points """
        self.__data_point_radius = value

    @property
    def show_labels(self):
        """ Get the show_labels value """
        return self.__show_labels

    @show_labels.setter
    def show_labels(self, value):
        """ Set the show_labels value """
        self.__show_labels = value
        self.data_point_radius2 = self.data_point_radius

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
    def x_offset(self):
        return self.__x_offset

    @x_offset.setter        
    def x_offset(self, value):
        self.__x_offset = value

    @property
    def y_offset(self, value):
        self.__y_offset = value
    
    @y_offset.setter
    def y_offset(self, value):
        self.__y_offset = value
    
    @property
    def x_values(self):
        return self.__x_values

    @x_values.setter
    def x_values(self, value):
        """ Set the x values """
        self.__x_values = value

    def set_x_axis_colour(self, red, green, blue):
        """ Set the x axis colour """
        self.x_axis_colour = {'red': red, 'green': green, 'blue': blue}

    @property
    def title(self):
        """ Get the title """
        return self.__title
    
    @title.setter
    def title(self, title):
        """ Set the title """
        self.__title = title

    @property
    def data_point_radius2(self):
        """ Get the radius of the data points """
        return self.__data_point_radius2

    @data_point_radius2.setter
    def data_point_radius2(self, value):
        """ Set the radius of the data points """
        self.__data_point_radius2 = value
        
    def draw_border(self):
        self.display.set_pen(self.border_colour['red'], self.border_colour['green'], self.border_colour['blue'])
        x = self.x
        y = self.y 
        w = self.__width 
        h = self.__height
        x1 = x+w
        y1 = y+h
        self.display.set_clip(x,y,x1,y1)

        # Draw the 4 border lines
        for i in range(0,self.border_width,1):
            self.display.line(x+i, y+i, x+i, y1-i) # left
            self.display.line(x+i, y+i, x1-i, y+i) # top
            self.display.line(x+i, y1-i-1, x1-i, y1-i-1) # bottom
            self.display.line(x1-i-1, y+i, x1-i-1, y1) # right
        
        self.display.set_pen(self.background_colour['red'], self.background_colour['green'], self.background_colour['blue'])
        self.display.remove_clip()
        
        self.display.update()
        

    def draw_grid(self):
        # self.display.set_pen(self.border_colour['red']//4, self.border_colour['green']//4, self.border_colour['blue']//4)
        self.display.set_pen(self.grid_colour['red'], self.grid_colour['green'], self.grid_colour['blue'])
        x = self.x
        y = self.y 
        w = self.width
        h = self.height

        cols = w // self.grid_spacing
        row = h // self.grid_spacing

#         print(f'cols: {cols}, row: {row}')

        for i in range(cols):
            self.display.line(x+self.grid_spacing*i, y, x+self.grid_spacing*i, y+h)
            # print(f'drawing cols: {i}')    
        
        for j in range(row):
            self.display.line(x, y+self.grid_spacing*j, x+w, y+self.grid_spacing*j)
            # print(f'drawing row: {j}')  
        
        # Update display
        self.display.update()

    def map(self, x, in_min, in_max, out_min, out_max):
        """ Map a value from one range to another """
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def scale_data(self):

        self.min_val = min(self.__x_values)  # get the minimum value
        self.max_val = max(self.__x_values)  # get the maximum value
        
        # Calculate the scale
        if self.max_val - self.min_val == 0:
            self.max_val = 2
            self.min_val = 1
        self.__y_scale = (((self.__height - self.__text_height) - self.border_width * 2)) // (self.max_val - self.min_val)
#         print(f'Min: {self.min_val} Max: {self.max_val}, Y Scale: {self.__y_scale}')

    def update(self):
        """ Update the chart """
        
        self.display.set_clip(self.x, self.y, self.x+self.width, self.y+self.height)
        self.display.clear()
        self.display.remove_clip()
        
        # Draw the Grid
        if self.grid: self.draw_grid()
        
        gap = 3
        
        # display the Title
        self.display.set_clip(self.x+gap, self.y+gap, (self.x+self.width)-gap, (self.y+self.height)-gap)
        self.display.set_pen(self.__title_colour['red'], self.__title_colour['green'], self.__title_colour['blue'])
        self.display.text(self.title, self.x+self.border_width+1, self.y + self.border_width+1,self.__width)
        self.display.set_pen(self.__data_colour['red'], self.__data_colour['green'], self.__data_colour['blue'])
        self.display.remove_clip()
    
        # Work out the area offset
        self.__x_offset = self.border_width+2
        self.__y_offset = (self.height-self.border_width)-2

        x_pos = self.x + self.__x_offset
        y_pos = self.y + self.__y_offset 

        prev_x = x_pos
        prev_y = y_pos
        
    
        # The area within the chart
        plot_area = (self.height - self.__text_height) - self.border_width*2
        self.display.set_clip(self.x+self.border_width, self.y+self.border_width+self.__text_height, self.x+self.width, (self.y+self.height)-self.border_width)
#         self.display.line(self.x, self.y+self.height - plot_area, self.width, self.y+self.height-plot_area)
        # print(f'plot area: {plot_area}, height: {self.height}')
        for item in self.__x_values:
            val = item
            item = int(self.map(item, self.min_val, self.max_val,0,plot_area)) # scale the data

            # calculate data visual height
            data_height = int(item)

            if self.show_bars:
                self.display.rectangle(x_pos, y_pos-item, self.__data_point_width, data_height)
            
            if self.show_datapoints:
                self.display.set_pen(self.__data_colour['red']//4, self.__data_colour['green']//4, self.__data_colour['blue']//4)
                self.display.circle(x_pos, y_pos-item, self.__data_point_radius2)
                self.display.set_pen(self.__data_colour['red'], self.__data_colour['green'], self.__data_colour['blue'])
                self.display.circle(x_pos, y_pos-item, self.__data_point_radius)
                
            if self.show_lines:
                self.display.line(x_pos, y_pos-item, prev_x, prev_y)
            
            if self.show_labels:
#                 self.display.set_pen(self.data_colour['red']//2,self.__data_colour['green']//2, self.__data_colour['blue']//2)
                self.display.text(str(val), x_pos-4, y_pos-item -10, self.width - y_pos, 1)

            prev_x = x_pos
            prev_y = y_pos-item
            x_pos += self.__data_point_width+1

        self.display.remove_clip()
        
        # Draw the border
        self.draw_border()

        self.display.update()
        