scoreboard players operation @s player_matches_found_count += const1 const
execute if score global is_make_it_take_it_mode matches 0 run schedule function matching:matching/go_to_next_player_turn 10 append
execute if score global is_make_it_take_it_mode matches 1 run tellraw @a [{"text":"Make it, take it! It is "},{"selector":"@a[scores={is_my_turn_score=1}]","color":"dark_aqua","bold":true},{"text":"'s turn again!"}]
