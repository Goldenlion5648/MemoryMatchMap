tp @e[tag=card] ~ ~-200 ~
kill @e[tag=card]
summon bee 52 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon allay 52 -3 56 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon strider 52 -3 60 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon cow 52 -3 64 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon creeper 56 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon panda 56 -3 56 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon turtle 56 -3 60 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon axolotl 56 -3 64 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon bee 60 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon allay 60 -3 56 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon strider 60 -3 60 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon cow 60 -3 64 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon creeper 64 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon panda 64 -3 56 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon turtle 64 -3 60 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon axolotl 64 -3 64 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
execute as @e[type=bee] run scoreboard players set @s mob_id 1
execute as @e[type=allay] run scoreboard players set @s mob_id 2
execute as @e[type=strider] run scoreboard players set @s mob_id 3
execute as @e[type=cow] run scoreboard players set @s mob_id 4
execute as @e[type=creeper] run scoreboard players set @s mob_id 5
execute as @e[type=panda] run scoreboard players set @s mob_id 6
execute as @e[type=turtle] run scoreboard players set @s mob_id 7
execute as @e[type=axolotl] run scoreboard players set @s mob_id 8
tellraw @a "animals have been placed!"
