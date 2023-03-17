execute if score global selected_difficulty matches 0 run function matching:matching/nested_functions/nested_function24
execute if score global selected_difficulty matches 1 run function matching:matching/nested_functions/nested_function25
execute if score global selected_difficulty matches 2 run function matching:matching/nested_functions/nested_function26
scoreboard players operation global selected_difficulty %= const3 const
execute if score global is_make_it_take_it_mode matches 0 run function matching:matching/nested_functions/nested_function27
execute if score global is_make_it_take_it_mode matches 1 run function matching:matching/nested_functions/nested_function28
scoreboard players operation global is_make_it_take_it_mode %= const2 const
