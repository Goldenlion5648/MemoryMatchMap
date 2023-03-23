execute if entity @a[scores={is_my_turn_score=1}] run tellraw @a [{"text":"It is "},{"selector":"@a[scores={is_my_turn_score=1}]","color":"dark_aqua","bold":true},{"text":"'s turn"}]
execute unless entity @a[scores={is_my_turn_score=1}] run function matching:matching/nested_functions/nested_function3
