import jpegdec 

class Chart:
    title = ''
    x_values = []
    __x_offset = 0
    __y_offset = 0
    background_colour = {'red': 0, 'green': 0, 'blue': 0}
    border_colour = {'red': 0, 'green': 0, 'blue': 0}
    grid_colour = {'red':border_colour['red']//4, 'green':border_colour['green']//4,'blue':border_colour['blue']//4}
    title_colour = {'red': 0, 'green': 0, 'blue': 0}
    data_colour = {'red': 0, 'green': 0, 'blue': 0}
    __data_point_radius = 2
    data_point_radius2 = __data_point_radius * 4
    __data_point_width = 10
    x = 0
    y = 0
    width = 100
    height = 100
    border_width = 2
    __text_height = 16
    show_datapoints = False
    show_lines = False
    show_bars = True
    __show_labels = False
    grid = True
    grid_spacing = 10

    def __init__(self, display, title=None, x_label=None, y_label=None, x_values=None, y_values=None):
        self.display = display
        if title: self.title = title
        if x_label: self.__x_label = x_label
        if y_label: self.__y_label = y_label
        if x_values:
            # Scale the data
            self.x_values = x_values
            self.min_val = min(self.x_values)  # get the minimum value
            self.max_val = max(self.x_values)  # get the maximum value
        if y_values: self.__y_values = y_values

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
    
    def draw_border(self):
        border_colour = self.display.create_pen(self.border_colour['red'], self.border_colour['green'], self.border_colour['blue'])
        background_colour = self.display.create_pen(self.background_colour['red'], self.background_colour['green'], self.background_colour['blue'])
        self.display.set_pen(border_colour)
        x = self.x
        y = self.y 
        w = self.width 
        h = self.height
        x1 = x+w
        y1 = y+h
        self.display.set_clip(x,y,x1,y1)

        # Draw the 4 border lines
        for i in range(0,self.border_width,1):
            self.display.line(x+i, y+i, x+i, y1-i) # left
            self.display.line(x+i, y+i, x1-i, y+i) # top
            self.display.line(x+i, y1-i-1, x1-i, y1-i-1) # bottom
            self.display.line(x1-i-1, y+i, x1-i-1, y1) # right
        
        self.display.set_pen(background_colour)
        self.display.remove_clip()
        
#         self.display.update()
        

    def draw_grid(self):
        """ Draw the grid behind the chart """
        
        # Set the colour of the grid
        grid_colour = self.display.create_pen(self.grid_colour['red'], self.grid_colour['green'], self.grid_colour['blue'])
        self.display.set_pen(grid_colour)
        
        # Create values
        x = self.x
        y = self.y 
        w = self.width
        h = self.height

        # Calculate columns
        cols = w // self.grid_spacing
        row = h // self.grid_spacing
    
        # Draw Grid
        for i in range(cols):
            self.display.line(x+self.grid_spacing*i, y, x+self.grid_spacing*i, y+h)   
        
        for j in range(row):
            self.display.line(x, y+self.grid_spacing*j, x+w, y+self.grid_spacing*j)
        
        # Update display
#         self.display.update()

    def map(self, x, in_min, in_max, out_min, out_max):
        """ Map a value from one range to another """
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def scale_data(self):
        """ Scale the data to fit the chart """

        self.min_val = min(self.x_values)  # get the minimum value
        self.max_val = max(self.x_values)  # get the maximum value
        
        # Calculate the scale
        if self.max_val - self.min_val == 0:
            self.max_val = 2
            self.min_val = 1
        self.__y_scale = (((self.height - self.__text_height) - self.border_width * 2)) // (self.max_val - self.min_val)

    def update(self):
        """ Update the chart """
        
        self.display.set_clip(self.x, self.y, self.x+self.width, self.y+self.height)
        background_colour = self.display.create_pen(self.background_colour['red'], self.background_colour['green'], self.background_colour['blue'])
        self.display.set_pen(background_colour)
        self.display.rectangle(self.x, self.y, self.width, self.height)
        
        self.display.remove_clip()
        
        # Draw the Grid
        if self.grid:
            self.draw_grid()
        
        gap = 3
        
        # display the Title
        title_colour = self.display.create_pen(self.title_colour['red'], self.title_colour['green'], self.title_colour['blue'])
        data_colour = self.display.create_pen(self.data_colour['red'], self.data_colour['green'], self.data_colour['blue'])
        data_colour2 = self.display.create_pen(self.data_colour['red']//4, self.data_colour['green']//4, self.data_colour['blue']//4)

        self.display.set_clip(self.x+gap, self.y+gap, (self.x+self.width)-gap, (self.y+self.height)-gap)
        self.display.set_pen(title_colour)
        self.display.text(self.title, self.x+self.border_width+1, self.y + self.border_width+1,self.width)
        self.display.set_pen(data_colour)
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

        for item in self.x_values:
            val = item
            item = int(self.map(item, self.min_val, self.max_val,0,plot_area)) # scale the data

            # calculate data visual height
            data_height = int(item)

            if self.show_bars:
                self.display.rectangle(x_pos, y_pos-item, self.__data_point_width, data_height)
            
            if self.show_datapoints:
                self.display.set_pen(data_colour2)
                self.display.circle(x_pos, y_pos-item, self.data_point_radius2)
                self.display.set_pen(data_colour)
                self.display.circle(x_pos, y_pos-item, self.__data_point_radius)
                
            if self.show_lines:
                self.display.line(x_pos, y_pos-item, prev_x, prev_y)
            
            if self.show_labels:                
                self.display.text(str(val), x_pos-4, y_pos-item -10, self.width - y_pos, 1)

            prev_x = x_pos
            prev_y = y_pos-item
            x_pos += self.__data_point_width+1

        self.display.remove_clip()
        
        # Draw the border
        self.draw_border()

        self.display.update()
        

class Card(Chart):
    """ A card class """

#     display = None
#     x = 0
#     y = 0
#     width = 0
#     height = 0
#     title = ''
#     background_colour = {'red':0, 'green':0, 'blue':0}
#     title_colour = {'red':0, 'green':0, 'blue':0}
    text_scale = 20
    margin = 2

    def __init__(self, display, x=None, y=None, width=None, height=None, title=None):
        """ Initialise the card """
        self.display = display
        if x: self.x = x
        if y: self.y = y
        if width: self.width = width
        if height: self.height = height
        if title: self.title = title

    def scale_text(self):
        """ Scale the text """
       
        self.text_scale = 20

        while True:
            self.display.set_font("bitmap8")
            name_length = self.display.measure_text(self.title, self.text_scale)
            if name_length >= self.width - self.margin*2:
                self.text_scale -= 1
            else:
                break
        
        if self.text_scale * 8 > self.height:
            self.text_scale = self.height // 8 

    def update(self):
        """ Update the card """

        # Set the colours
        background_color = self.display.create_pen(self.background_colour['red'], self.background_colour['green'], self.background_colour['blue'])
        title_color = self.display.create_pen(self.title_colour['red'], self.title_colour['green'], self.title_colour['blue'])
        self.display.set_pen(background_color)

        # Clear the display, without flickering
        self.display.rectangle(self.x, self.y, self.width, self.height)
        
        # Draw the Grid, if its enabled
        if self.grid:
            self.draw_grid()

        # Draw the border 
        self.draw_border()
        
        self.display.set_pen(title_color)
                
        # Centered title
        self.scale_text()
        text_length = self.display.measure_text(self.title, self.text_scale)
        

        # title_x = ((text_length - self.width) //2)                        
        title_y = (self.y + self.height // 2) - (self.text_scale * 8) // 2
        
        # Draw the title
        self.display.text(self.title, self.x + ((self.width //2) - (text_length //2)), title_y, text_length, self.text_scale)

        # Update the display
        self.display.update()

class Image_tile:
    __image_file = None
    x = 0
    w = 0
    width = 0
    height = 0
    border_colour = {'red':0, 'green':0, 'blue':0}
    border_width = 2
    
    def __init__(self, display, filename=None):
        """ Initialise the image tile """
        self.display = display
        if filename:
            self.__image_file = filename

    @property
    def filename(self):
        return self.__image_file

    @filename.setter
    def filename(self, file:str):
        self.__image_file = file

    def draw_border(self):
        border_colour = self.display.create_pen(self.border_colour['red'], self.border_colour['green'], self.border_colour['blue'])
        # background_colour = self.display.create_pen(self.background_colour['red'], self.background_colour['green'], self.background_colour['blue'])
        self.display.set_pen(border_colour)
        x = self.x
        y = self.y 
        w = self.width 
        h = self.height
        x1 = x+w
        y1 = y+h
        self.display.set_clip(x,y,x1,y1)

        # Draw the 4 border lines
        for i in range(0,self.border_width,1):
            self.display.line(x+i, y+i, x+i, y1-i) # left
            self.display.line(x+i, y+i, x1-i, y+i) # top
            self.display.line(x+i, y1-i-1, x1-i, y1-i-1) # bottom
            self.display.line(x1-i-1, y+i, x1-i-1, y1) # right
        
        # self.display.set_pen(background_colour)
        self.display.remove_clip()

    def update(self):
        """ Display the image tile"""
        
        j = jpegdec.JPEG(self.display)

        # Open the JPEG file
        j.open_file(self.filename)

        self.display.set_clip(self.x, self.y, self.width, self.height)

        # Decode the JPEG
        j.decode(self.x, self.y, jpegdec.JPEG_SCALE_HALF)

        self.display.remove_clip()
        # Draw the border 
        self.draw_border()

class Container:
    """ A container class """

    display = None
    
    charts = []
    cols = 1
    __background_colour = {'red':0, 'green':0, 'blue':0}
    __title_colour = {'red':0, 'green':0, 'blue':0}
    __data_colour = {'red':0, 'green':0, 'blue':0}
    __grid_colour = {'red':0, 'green':0, 'blue':0}

    def __init__(self, display, width=None, height=None):
        if width: 
            self.width = width
        if height:
             self.height = height
        else:
            self.width, self.height = display.get_bounds()

    def add_chart(self, item):
        """ Add an item to the container """
        self.charts.append(item)

    def update(self):
        """ Update the container """
    
        rows = len(self.charts) // self.cols
        
        print(f'rows: {rows}, cols: {self.cols}')
        
        item_count = rows // self.cols
    
        count = 1
        for col in range(1,self.cols+1,1):
            for row in range(1, rows+1, 1):
                item_index = count
                print(f'index_item: {item_index}')
                
                item = self.charts[item_index-1]
                item.height = self.height // rows
                item.y = self.height - (row * item.height)
                item.width = self.width // self.cols
                item.x = self.width - (self.width // col)
                count +=1 
                if count > 4:
                    count = 1
            for item in self.charts:
                item.update()

    @property
    def background_colour(self):
        return self.__background_colour

    @background_colour.setter
    def background_colour(self, value):
        
        self.__background_colour = value
        for item in self.charts:
            item.background_colour = value
    
    @property
    def grid_colour(self):
        return self.__grid_colour

    @grid_colour.setter
    def grid_colour(self, value):
        
        self.__grid_colour = value
        for item in self.charts:
            item.grid_colour = value
    
    @property
    def data_colour(self):
        return self.__data_colour

    @data_colour.setter
    def data_colour(self, value):
        
        self.__data_colour = value
        for item in self.charts:
            item.data_colour = value
            
    @property
    def title_colour(self):
        return self.__title_colour

    @title_colour.setter
    def title_colour(self, value):
        
        self.__title_colour = value
        for item in self.charts:
            item.title_colour = value
    
    @property
    def border_colour(self):
        return self.__border_colour

    @border_colour.setter
    def border_colour(self, value):
        
        self.__border_colour = value
        for item in self.charts:
            item.border_colour = value
    @property
    def border_width(self):
        return self.__border_width

    @border_width.setter
    def border_width(self, value):
        
        self.__border_width = value
        for item in self.charts:
            item.border_width = value