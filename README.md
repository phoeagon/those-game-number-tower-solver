# those-game-number-tower-solver
A solver script for "Number tower" in "Those game"

Those game, or "YEAH! YOU WANT "THOSE GAMES," RIGHT? SO HERE YOU GO! NOW, LET'S SEE YOU CLEAR THEM!"(https://store.steampowered.com/app/2348100/YEAH_YOU_WANT_THOSE_GAMES_RIGHT_SO_HERE_YOU_GO_NOW_LETS_SEE_YOU_CLEAR_THEM/) [wikipedia](https://en.wikipedia.org/wiki/Those_Games) is a collection of games.

Notably this is a solver for the "Number tower" game: a game of arithmetic where the player has a starting number. The player must then add, subtract, multiply, or divide the starting number based on the tower they select in order to have a greater number than the last tower in the puzzle.

Sample play video is [here](https://www.youtube.com/watch?v=xlA381JOKaI).

## Usage:

First input the starting strength of the protagonist.

```
input all vars:35
```

Then, in each line, input the values from each level of the tower. Separate each item with a space.

```
input all var
-3 *2 /2 +100
[prints optimal answer resulting in maximal resulting strength without going into negative]
```
