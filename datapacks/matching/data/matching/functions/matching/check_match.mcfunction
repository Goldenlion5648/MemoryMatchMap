scoreboard players set global matching_count 0
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=bee,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=allay,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=strider,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=cow,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=creeper,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=panda,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=turtle,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=axolotl,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=evoker,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=vindicator,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=fox,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=witch,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=vex,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=parrot,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=frog,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=llama,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=cod,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=skeleton_horse,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=pufferfish,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=rabbit,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=ravager,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=salmon,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=sheep,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=silverfish,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=wither_skeleton,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=iron_golem,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=snow_golem,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=polar_bear,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=mooshroom,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=guardian,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=wolf,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=zombified_piglin,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=piglin_brute,tag=selected_mob]
execute if score global matching_count matches ..1 run execute store result score global matching_count run execute if entity @e[type=piglin,tag=selected_mob]
execute if score global matching_count matches 2 run execute unless entity @e[type=area_effect_cloud,tag=spin_delay] run function matching:matching/found_match
execute unless score global matching_count matches 2 run execute if score global selected_count matches 2 run function matching:matching/put_card_back_down
