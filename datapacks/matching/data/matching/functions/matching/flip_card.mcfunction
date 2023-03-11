execute as @e[tag=selected_slime,tag=!revealed] at @s run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 red_wool replace
execute as @e[tag=selected_slime,tag=!revealed] at @s run execute positioned ~ ~-4 ~ run summon area_effect_cloud ~ ~ ~ {Tags:["spin_delay"],Age:-4}
execute as @e[tag=selected_slime,tag=!revealed] at @s run execute positioned ~ ~-4 ~ run execute as @e[tag=card,distance=..3] at @s run summon marker ~ ~ ~ {Tags:["temp_pos"]}
execute as @e[tag=selected_slime,tag=!revealed] at @s run execute positioned ~ ~-4 ~ run execute as @e[tag=card,distance=..3] at @s run tag @s add selected_mob
execute as @e[tag=selected_slime,tag=!revealed] at @s run execute positioned ~ ~-4 ~ run tp @e[tag=card,distance=..3] @s
execute as @e[tag=selected_slime,tag=!revealed] at @s run tp @e[tag=card,distance=..3] ~ ~.5 ~
execute as @e[tag=selected_slime,tag=!revealed] at @s run tag @s add revealed
