scoreboard players set global turn_switch_cooldown 10
scoreboard players operation global total_turns_taken += const1 const
scoreboard players operation global turn_player += const1 const
scoreboard players operation global turn_player %= global total_player_count
execute unless score global total_player_count matches 1 run function matching:matching/nested_functions/nested_function4
