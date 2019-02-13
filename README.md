# Flappy Bird Game
An implementation of the popular game Flappy Bird
![screenshot](./resources/readme/1.png)

## Usage
Dependency: pygame, numpy
Install requirement `pip install -r requirements.txt` <br> 
Just run `python Flappy_bird.py` to run the game

Press 'R' to reset the game <br>
Press 'P' to pause/resume the game<br>
Press '1','2','3' to change background music<br>

## Description
This game includes 3 modules `Flappy_Bird,bird and pipe`<br>
`Flappy_bird` is used to draw the game board, display the score and listen to keyboard event <br>
`Bird` manages the birds motion and update its coordinates <br>
`Pipe` including `pipe_head` and `pipe_body`, and it is used to update pipe coordinates