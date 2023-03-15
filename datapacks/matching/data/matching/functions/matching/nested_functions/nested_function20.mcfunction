setblock 69 4 -30 air replace
setblock 69 4 -30 oak_wall_sign[facing=west]{Text1:'{"text":"Current Difficulty","color":"white"}',Text2:'{"text":"Easy","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"scoreboard players operation global selected_difficulty += const1 const"}}',Text4:'{"text":"4 x 4","color":"green"}'} replace
scoreboard players operation global selected_difficulty %= const3 const
