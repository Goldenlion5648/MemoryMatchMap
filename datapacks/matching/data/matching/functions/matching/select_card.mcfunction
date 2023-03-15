execute store result score global selected_count if entity @e[tag=selected_slime]
execute if score global selected_count matches 0..1 run execute as @e[tag=card_outline,nbt={HurtTime:10s}] run execute on attacker run execute if score @s player_turn_id = global turn_player run execute as @e[tag=card_outline,nbt={HurtTime:10s}] run function matching:matching/nested_functions/nested_function0
