tellraw @a [{"text":"Make it, take it! It is "},{"selector":"@a[scores={is_my_turn_score=1}]","color":"dark_aqua","bold":true},{"text":"'s turn again!"}]
scoreboard players operation global total_turns_taken += const1 const
