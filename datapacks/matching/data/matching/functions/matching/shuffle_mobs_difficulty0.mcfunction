tag @e[tag=hidden] remove moved
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
tag @e[tag=hidden,tag=!moved,tag=!selected_mob,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {Tags:["shuffle_temp_pos"]}
tag @e[tag=hidden,tag=!selected_mob,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag=shuffle_temp_pos,limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag @e[tag=dest,limit=1] remove dest
kill @e[type=marker,tag=shuffle_temp_pos]
