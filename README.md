## Minecraft Memory Matching Minigame

This is a minecraft minigame map that runs on mcfunction files generated using [a python script](datapacks/matching/data/matching/functions/matching/gen_matching_files.py) which makes use of my [PythonToMcfunctionTranspiler](https://github.com/Goldenlion5648/PythonToMcfunctionTranspiler/blob/master/python_helpers/helper_functions.py)

The gameplay is the classic memory matching game where a player selects a "card," then chooses a second card, and if they match, the cards stay facing up. If the cards do not match, both are flipped face down again.

The board looks like this by default:
![Empty board](explanation_images/empty_board.png)

Once the game is over, it looks like this:
![Completed board](explanation_images/completed_map.png)

This game can be played in single player or multiplayer. If played in multiplayer, the game enforces players taking turns in a round robin ordering, or optionally a "make it, take it" mode where a player can go again after a correct match.

These are the game settings: (the grid size, and whether or not "make it, take it" mode is enabled)
![game settings](explanation_images/game_settings.png)

An example of "Make it, Take it:"
![make it take it](explanation_images/make_it_take_it.png)

In the following image, a player has made their first pick (which had an Evoker), and is about to make their second choice (by hitting the white cube).
![the player is about to make their second move](explanation_images/before_picking2.png)

![the second pick was a cod](explanation_images/after_picking_second.png)

In this case, the Cod does not match the Evoker so both cards go back face down.

![both cards went back face down](explanation_images/before_picking.png)
