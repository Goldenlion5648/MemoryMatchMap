tellraw @a "DEBUG"
tellraw @a "calculating winner"
scoreboard players operation global highest_score > @a player_matches_found_count
scoreboard players set global number_of_winners 0
execute as @a run execute if score @s player_matches_found_count = global highest_score run scoreboard players operation global number_of_winners += const1 const
execute if score global number_of_winners matches 1 run title @a subtitle {"text":"Wins!","color":"green"}
execute if score global number_of_winners matches 1 run title @a title [{"selector":"@a","separator":" and ","color":"green","bold":true}]
execute if score global number_of_winners matches 2.. run title @a subtitle {"text":"Tied!","color":"green"}
execute if score global number_of_winners matches 2.. run title @a title [{"selector":"@a","separator":" and ","color":"green","bold":true}]
