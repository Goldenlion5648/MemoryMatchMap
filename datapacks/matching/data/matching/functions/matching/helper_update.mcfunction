scoreboard players add global game_clock 1
team join passable @a[team=!passable]
effect give @a minecraft:saturation infinite 0 true
execute positioned 63.0 4.0 -28.0 run execute as @a[distance=..20] run clear @s[gamemode=adventure] 
kill @e[type=item]
