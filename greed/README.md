# Greed
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 greed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.
```

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- greed               (source code for game)
  +-- data              (data files for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```


```mermaid
classDiagram
Actor <|-- Artifact
class __main__{
  +String beakColor
  +swim()
  +quack()
  }
class Actor{
  -int sizeInFeet
  -_text
  -_font_size
  -_color
  -_position
  -_velocity
  +get_color()Color
  +get_font_size()int
  +get_position()Point
  +get_text()str
  +get_velocity()Point
  +move_next(int, int)void
  +set_solor(Color)void
  +set_position(Point)void
  +set_font_size(int)void
  +set_text(str)void
  +set_velocity(Point)void
  }
class Artifact{
  +calculate_points()int
  }
class Color{
  -_red
  -_green
  -_blue
  -_alpha
  +to_tuple()Color
}
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Spencer Sowby (sow22003@byui.edu)
