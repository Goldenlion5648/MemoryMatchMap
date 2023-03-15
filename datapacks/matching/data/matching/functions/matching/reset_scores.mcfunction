scoreboard objectives remove player_matches_found_count
scoreboard players set global total_turns_taken 0
scoreboard objectives add player_matches_found_count dummy "Matches Found"
scoreboard players set @a player_matches_found_count 0
scoreboard players set global has_winner_been_found 0
scoreboard players set global current_player_id_being_assigned 0
scoreboard objectives setdisplay sidebar player_matches_found_count
