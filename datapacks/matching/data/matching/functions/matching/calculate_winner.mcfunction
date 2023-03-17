scoreboard players set global highest_score 0
scoreboard players operation global highest_score > @a player_matches_found_count
scoreboard players set global number_of_winners 0
execute as @a run execute if score @s player_matches_found_count = global highest_score run scoreboard players operation global number_of_winners += const1 const
execute if score global number_of_winners matches 1 run execute as @a run execute if score @s player_matches_found_count = global highest_score run function matching:matching/nested_functions/nested_function14
execute if score global number_of_winners matches 2.. run function matching:matching/nested_functions/nested_function15
execute if score global number_of_winners matches 1.. run function matching:matching/nested_functions/nested_function16
