tp @e[tag=card] ~ ~-200 ~
kill @e[tag=card]
summon bee 52 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon allay 52 -3 58 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon strider 52 -3 64 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon cow 52 -3 70 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon creeper 52 -3 76 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon panda 52 -3 82 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon turtle 58 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon axolotl 58 -3 58 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon evoker 58 -3 64 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon vindicator 58 -3 70 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon illusioner 58 -3 76 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon vex 58 -3 82 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon parrot 64 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon frog 64 -3 58 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon bee 64 -3 64 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon allay 64 -3 70 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon strider 64 -3 76 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon cow 64 -3 82 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon creeper 70 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon panda 70 -3 58 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon turtle 70 -3 64 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon axolotl 70 -3 70 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon evoker 70 -3 76 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon vindicator 70 -3 82 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon illusioner 76 -3 52 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon vex 76 -3 58 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon parrot 76 -3 64 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
summon frog 76 -3 70 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["hidden", "card"]}
execute as @e[type=bee] run scoreboard players set @s mob_id 1
execute as @e[type=allay] run scoreboard players set @s mob_id 2
execute as @e[type=strider] run scoreboard players set @s mob_id 3
execute as @e[type=cow] run scoreboard players set @s mob_id 4
execute as @e[type=creeper] run scoreboard players set @s mob_id 5
execute as @e[type=panda] run scoreboard players set @s mob_id 6
execute as @e[type=turtle] run scoreboard players set @s mob_id 7
execute as @e[type=axolotl] run scoreboard players set @s mob_id 8
execute as @e[type=evoker] run scoreboard players set @s mob_id 9
execute as @e[type=vindicator] run scoreboard players set @s mob_id 10
execute as @e[type=illusioner] run scoreboard players set @s mob_id 11
execute as @e[type=vex] run scoreboard players set @s mob_id 12
execute as @e[type=parrot] run scoreboard players set @s mob_id 13
execute as @e[type=frog] run scoreboard players set @s mob_id 14
tellraw @a "animals have been placed!"
