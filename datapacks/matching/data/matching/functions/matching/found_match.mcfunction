execute as @e[tag=selected_mob] at @s run function matching:matching/nested_functions/nested_function7
execute if score global reveal_cooldown matches 33 run execute as @a at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.3
execute if score global reveal_cooldown matches 41 run execute as @a at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1
execute if score global reveal_cooldown matches 49 run execute as @a at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 0.7
execute if score global reveal_cooldown matches 57 run execute as @a at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 0.4
execute if score global reveal_cooldown matches 1 run execute as @a run execute if score @s player_turn_id = global turn_player run function matching:matching/nested_functions/nested_function9
