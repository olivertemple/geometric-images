# geometric-images
Creates Various Geomentric images using for loops
There are currently 3 different images that can be generated both in 2D and 3D. Colours can be changes and up to two images of the same dimensions can be overlayed.

# Motovation
I did this project because i was bored during the 3rd UK Covid-19 lockdown, and it was something that i had wanted to try for a few months, just hadnt found the time.

# Examples
Here are two examples of 2, 2D images overlayed in different colours.
<img src='/outputs/example1.png'>
<img src='/outputs/example2.png'>

# Instilation
To install requirements, run:

`pip3 install -r requirements.txt`

This will install matplotlib and argparse
# Usage
```
main.py [-h] [-dimensions DIMENSIONS] [-i I] [-w W] [-num NUM] [-shape SHAPE] [-shape2 SHAPE2] [-colour COLOUR] [-colour2 COLOUR2]

Draw geometric Images.

optional arguments:
  -h, --help            show this help message and exit
  -dimensions DIMENSIONS
                        2D/3D output image (2 for 2D, 3 for 3D).
  -i I                  Size of output image.
  -w W                  Width of line, recommended less than 1.
  -num NUM              How many quadrants to be filled, 1-4.
  -shape SHAPE          Shape 1 number (1-3).
  -shape2 SHAPE2        Shape 2 number (optional)(1-3).
  -colour COLOUR        Colour of shape 1, either as a word, hex or RGB.
  -colour2 COLOUR2      Colour of shape 2, either as a word, hex or RGB.
  ```
  
  # Example Code
  ```python .\main.py -dimensions 2 -i 30 -w 0.4 -num 4 -shape 1 -shape2 2 -colour darkorange -colour2 pink```
  <img src='/outputs/examplecodeoutput.png'>
