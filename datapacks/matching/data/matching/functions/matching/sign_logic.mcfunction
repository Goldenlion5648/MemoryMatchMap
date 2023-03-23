execute if score global selected_difficulty matches 0 run function matching:matching/nested_functions/nested_function31
execute if score global selected_difficulty matches 1 run function matching:matching/nested_functions/nested_function32
execute if score global selected_difficulty matches 2 run function matching:matching/nested_functions/nested_function33
scoreboard players operation global selected_difficulty %= const3 const
execute if score global is_make_it_take_it_mode matches 0 run function matching:matching/nested_functions/nested_function34
execute if score global is_make_it_take_it_mode matches 1 run function matching:matching/nested_functions/nested_function35
scoreboard players operation global is_make_it_take_it_mode %= const2 const
