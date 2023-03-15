fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 red_wool replace
execute positioned ~ ~-4 ~ run summon area_effect_cloud ~ ~ ~ {Tags:["spin_delay"],Age:-4}
execute positioned ~ ~-4 ~ run execute as @e[tag=card,distance=..3] at @s run function matching:matching/nested_functions/nested_function1
execute positioned ~ ~-4 ~ run tp @e[tag=card,distance=..3] @s
tp @e[tag=card,distance=..3] ~ ~.5 ~
tag @s add revealed
