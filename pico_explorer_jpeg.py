from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
import jpegdec 

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, rotate=0)

# Create a new JPEG decoder for our PicoGraphics
j = jpegdec.JPEG(display)

# Open the JPEG file
j.open_file("kev.jpg")

# Decode the JPEG
j.decode(0, 0, jpegdec.JPEG_SCALE_FULL)

# Display the result
display.update()