scoreboard players operation remainder_of_game_clock_mod_3 remainder = global game_clock
scoreboard players operation remainder_of_game_clock_mod_3 remainder %= const3 const
execute if score remainder_of_game_clock_mod_3 remainder matches 0 run execute unless entity @e[type=area_effect_cloud,tag=spin_delay] run execute as @e[tag=selected_mob] at @s run tp @s ~ ~ ~ ~90 ~
