execute store result score global remaining_cards if entity @e[tag=card_outline]
execute if score global has_winner_been_found matches 0 run execute if score global remaining_cards matches 0 run function matching:matching/calculate_winner
execute if score global has_winner_been_found matches 0 run execute if score global remaining_cards matches 0 run scoreboard players set global has_winner_been_found 1
