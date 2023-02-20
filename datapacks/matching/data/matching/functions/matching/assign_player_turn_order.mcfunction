scoreboard players set global turn_player 0
scoreboard players set global current_player_id_being_assigned 0
scoreboard players set @a player_turn_id -1
execute store result score global total_player_count if entity @a
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
execute as @e[limit=1,type=player,sort=random,scores={player_turn_id=-1}] run execute store result score @s player_turn_id run scoreboard players get global current_player_id_being_assigned
scoreboard players operation global current_player_id_being_assigned += const1 const
tellraw @a "order has been assigned"
