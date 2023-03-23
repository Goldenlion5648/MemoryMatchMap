setblock 69 4 -29 air replace
setblock 69 4 -29 oak_wall_sign[facing=west]{Text2:'{"text":"Make It, Take It","color":"white"}',Text3:'{"text":"Disabled","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"scoreboard players operation global is_make_it_take_it_mode += const1 const"}}'} replace
scoreboard players operation global is_make_it_take_it_mode %= const2 const
