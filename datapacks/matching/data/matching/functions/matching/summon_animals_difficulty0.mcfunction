tp @e[tag=card] ~ ~-200 ~
kill @e[tag=card]
summon bee 52 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon allay 52 -3 57 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon strider 52 -3 62 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon cow 52 -3 67 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon creeper 57 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon panda 57 -3 57 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon turtle 57 -3 62 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon axolotl 57 -3 67 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon bee 62 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon allay 62 -3 57 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon strider 62 -3 62 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon cow 62 -3 67 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon creeper 67 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon panda 67 -3 57 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon turtle 67 -3 62 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon axolotl 67 -3 67 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
execute as @e[type=bee] run scoreboard players set @s mob_id 1
execute as @e[type=allay] run scoreboard players set @s mob_id 2
execute as @e[type=strider] run scoreboard players set @s mob_id 3
execute as @e[type=cow] run scoreboard players set @s mob_id 4
execute as @e[type=creeper] run scoreboard players set @s mob_id 5
execute as @e[type=panda] run scoreboard players set @s mob_id 6
execute as @e[type=turtle] run scoreboard players set @s mob_id 7
execute as @e[type=axolotl] run scoreboard players set @s mob_id 8
tellraw @a "animals have been placed!"
