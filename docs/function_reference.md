# PiChart Function Reference

PiChart has 4 classes:

- [Chart](#Chart)
- [Container](#Container)
- [Card](#Card)
- [Image_tile](#Image_tile)

# Chart
Create a chart by creating a new Chart object. You'll need to provide a display object, from the picographics library. PicoGraphics is built into the [Pimoroni MicroPython](https://) build.

``` python
# Import a graphics driver
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

# Create a display
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)

# Create a new Chart and pass it the display
my_chart = Chart(display)
```

---

## Properties

### `data_point_radius`
The data point is the small circle that represents the data value. The data point radius is the size of the point drawn on the chart.

### `show_labels`

## Methods
### `draw_border`

### `draw_grid`
### `map`
### `scale_data`
### `update()`



# Container
## Properties
### `display`
### `charts`
### `cols`

## Methods
### `add_chart`


# Card

## Properties
### `text_scale`
### `margin`

## Methods
### `scale_text`
### `update`

# Image_tile
## Properties
### `x`
### `y`
### `width`
### `height`
### `border_colour`
### `border_width`
### `filename`

## Methods
### `draw_border`
### `update`
