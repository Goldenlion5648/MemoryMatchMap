execute as @e[tag=selected_mob] at @s run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 black_concrete replace #minecraft:mineable/pickaxe
execute as @e[tag=selected_mob] at @s run execute if score global reveal_cooldown matches 1 run execute as @e[tag=card_outline,distance=..2] run tp @s ~ ~-200 ~
execute as @e[tag=selected_mob] at @s run execute if score global reveal_cooldown matches 1 run execute as @e[tag=card_outline,distance=..2] run kill @s
execute as @e[tag=selected_mob] at @s run execute if score global reveal_cooldown matches 1 run tag @s remove selected_mob
execute if score global reveal_cooldown matches 25 run execute as @a at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.3
execute if score global reveal_cooldown matches 30 run execute as @a at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1
execute if score global reveal_cooldown matches 35 run execute as @a at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 0.7
execute if score global reveal_cooldown matches 1 run execute as @a run execute if score @s player_turn_id = global turn_player run scoreboard players operation @s player_matches_found_count += const1 const
execute if score global reveal_cooldown matches 1 run execute as @a run execute if score @s player_turn_id = global turn_player run function matching:matching/go_to_next_player_turn
