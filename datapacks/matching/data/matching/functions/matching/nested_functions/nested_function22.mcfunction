scoreboard players set @a is_my_turn_score 0
scoreboard players set @s is_my_turn_score 1
execute if score global turn_switch_cooldown matches 0 run function matching:matching/nested_functions/nested_function21
