execute if score global reveal_cooldown matches 27 run execute as @a at @s run playsound block.note_block.bit master @s ~ ~ ~ 1 1.7
execute if score global reveal_cooldown matches 19 run execute as @a at @s run playsound block.note_block.bit master @s ~ ~ ~ 1 1.2
execute if score global reveal_cooldown matches 11 run execute as @a at @s run playsound block.note_block.bit master @s ~ ~ ~ 1 0.7
execute if score global reveal_cooldown matches 3 run execute as @a at @s run playsound block.note_block.bit master @s ~ ~ ~ 1 0.2
execute if score global reveal_cooldown matches 1 run execute as @e[tag=selected_mob] at @s run tp @s @e[limit=1,type=minecraft:marker,sort=nearest]
execute if score global reveal_cooldown matches 1 run execute as @e[tag=selected_mob] at @s run kill @e[tag=temp_pos]
execute if score global reveal_cooldown matches 1 run execute as @e[tag=selected_mob] at @s run tag @s remove selected_mob
execute if score global reveal_cooldown matches 1 run execute as @e[tag=selected_slime] at @s run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 white_wool replace
execute if score global reveal_cooldown matches 1 run execute as @e[tag=selected_slime] at @s run tag @s remove revealed
execute if score global reveal_cooldown matches 1 run execute as @e[tag=selected_slime] at @s run tag @s remove selected_slime
execute if score global reveal_cooldown matches 1 run function matching:matching/go_to_next_player_turn
