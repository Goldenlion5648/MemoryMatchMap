import itertools as it
import os
import sys
import json
from enum import Enum
sys.path.insert(0, r'C:\Users\cobou\Documents\Curse\Minecraft\Instances\CommandCreations1_19_2\python_helpers')
sys.path.insert(0, r'C:\Users\cobou\Desktop\MultiMC\MultiMC\instances\snapshots\.minecraft\python_1_20_helper')
from helper_functions import *
import helper_functions
from python_1_20_helper import *

helper_functions.UPDATE_JSON_FILE = f"{os.path.dirname(__file__)}\\..\\..\\..\\minecraft\\tags\\functions\\tick.json"

class Tags(Enum):
    CARD_OUTLINE_TAG = "card_outline"
    SELECTED_SLIME_TAG = "selected_slime"
    SELECTED_MOB_TAG = "selected_mob"
    REVEALED_TAG = "revealed"
    SHUFFLE_TEMP_POS = "shuffle_temp_pos"
    ANIMAL_CARD = "card"
    SHUFFLE_DESTINATION = "dest"
    SHUFFLE_CURRENT_MOVING = "moving"
    HIDDEN_CARD = "hidden"
    REVEAL_CARD_TEMP_POS_TAG = "temp_pos"
    SPIN_DELAY_TAG = "spin_delay"

    def __str__(self):
        return str(self.value)
    
game_clock_score = "game_clock"

# print(helper_functions.UPDATE_JSON_FILE)

create_scoreboard(game_clock_score, 0)
increment_each_tick(game_clock_score)
helper_update.append(f"team join passable {selector_entity(selector='@a',team='!passable')}")

turn_player_score = "turn_player"
player_turn_id_score = "player_turn_id"
total_player_count_score = "total_player_count"
current_player_id_being_assigned = "current_player_id_being_assigned"
times_left_to_run = "times_left_to_run"
player_matches_found_count = "player_matches_found_count"
highest_score = "highest_score"

unassigned_players = at_e(type='player',score=[(player_turn_id_score, -1)],limit=1,sort='random')
players = at_a()
# unassigned_players = at_e(type=['sheep'],score=[(player_turn_id_score, -1)],limit=1,sort='random')
# players = at_e(type=['sheep'])
animals = [
    "bee",
    "allay",
    "strider",
    "cow",
    "creeper",
    "panda",
    "turtle",
    "axolotl",
    "evoker",
    "vindicator",
    "illusioner",
    "vex",
    "parrot",
    "frog",
]
game_corner = (50, 0, 50)
SMALLEST_BOARD_DIM = 4
tile_dim = 3



fisher_yates_single_pass = f'''tag @e[tag=hidden,tag=!moved,limit=1] add moving
execute at @e[tag=moving] run summon marker ~ ~ ~ {{Tags:["{Tags.SHUFFLE_TEMP_POS}"]}}
tag @e[tag=hidden,sort=random,limit=1] add dest
execute as @e[tag=moving,limit=1] run tp @s @e[tag=dest,limit=1]
execute as @e[tag=dest,limit=1] run tp @s @e[type=marker,tag={Tags.SHUFFLE_TEMP_POS},limit=1]
tag @e[tag=moving,limit=1] add moved
tag @e[tag=moving,limit=1] remove moving
tag {selector_entity(tag=Tags.SHUFFLE_DESTINATION,limit=1)} remove dest
kill @e[type=marker,tag={Tags.SHUFFLE_TEMP_POS}]'''.splitlines()

NUMBER_OF_DIFFICULTIES = 3
for difficulty in range(NUMBER_OF_DIFFICULTIES):
    board_dim = SMALLEST_BOARD_DIM + difficulty*2
    place_card_blocks = OutputFile(f"place_card_blocks_difficulty{difficulty}")
    summon_animals = OutputFile(f"summon_animals_difficulty{difficulty}")
    place_slimes = OutputFile(f"place_slimes_difficulty{difficulty}")
    shuffle_mobs = OutputFile(f"shuffle_mobs_difficulty{difficulty}")
    

    place_card_blocks.append(f"fill {tuple_to_string(game_corner)} {game_corner[0] + board_dim**2} {game_corner[1]} {game_corner[2] + board_dim**2} stone_bricks")
    tile_lower_corners = []

    for x in range(game_corner[0], game_corner[0] + board_dim**2, 5):
        for z in range(game_corner[0], game_corner[0] + board_dim**2, 5):
            tile_lower_corners.append((x + 1, game_corner[1], z + 1))
            place_card_blocks.append(f"fill {x + 1} {game_corner[1]} {z + 1} {x + tile_dim} {game_corner[1]} {z + tile_dim} purple_concrete")

    summon_animals.extend(smooth_remove(entity_selector(tag=Tags.ANIMAL_CARD.value)))
    create_scoreboard("mob_id")

    current_difficulty_animals = animals[:board_dim**2 // 2]
    
    for animal, (x, y, z) in zip(current_difficulty_animals*2, tile_lower_corners):
        summon_animals.append(
            f'summon {animal} {x + 1} {y - 3} {z + 1} ' + '{Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:' + format_tags_for_nbt([Tags.HIDDEN_CARD,Tags.ANIMAL_CARD]) + '}'
        )
    for i, animal in enumerate(current_difficulty_animals, 1):
        summon_animals.append(f"execute as @e[type={animal}] run scoreboard players set @s mob_id {i}")
    summon_animals.append('tellraw @a "animals have been placed!"')

    place_slimes.append("tp @e[type=minecraft:slime] ~ ~-400 ~")
    for pos in tile_lower_corners:
        place_slimes.append(f"summon slime {tuple_to_string(element_wise(pos, [1, 1, 1]))} " + '{Silent:1b,Glowing:1b,Team:"passable",PersistenceRequired:1b,NoAI:1b,Size:0,Tags:["'+ f"{Tags.CARD_OUTLINE_TAG}" + '"],ActiveEffects:[{Id:11,Amplifier:55b,Duration:200000000,ShowParticles:0b},{Id:14,Amplifier:1b,Duration:200000000,ShowParticles:0b}]}')

    shuffle_mobs.extend(
        fisher_yates_single_pass * len(current_difficulty_animals) * 2
    )
    # execute as @e[tag=moving] run say was moved
    shuffle_mobs.append('tellraw @a "cards have been shuffled!"')
    # difficulty_setup.extend(
    #     place_card_blocks,
    #     summon_animals,
    #     place_slimes,
    #     shuffle_mobs
    # )
    


select_card_file = OutputFile("select_card", is_update_file=True)
# create_scoreboard("selected_count")
NUM_CARDS_SELECTED_COUNT_SCORE = "selected_count"
# select_card_file.append(set_score_from(NUM_CARDS_SELECTED_COUNT_SCORE, f"if entity @e[tag={Tags.SELECTED_SLIME_TAG}]"))
select_card_file.extend(set_score_to_count_of(NUM_CARDS_SELECTED_COUNT_SCORE, selector_entity(tag=Tags.SELECTED_SLIME_TAG)))

REVEAL_COOLDOWN_SCORE = 'reveal_cooldown'

hit_slime_selector = f"@e[tag={Tags.CARD_OUTLINE_TAG}," + "nbt={HurtTime:10s}]"
select_card_file.extend(
    execute_if_score(NUM_CARDS_SELECTED_COUNT_SCORE, "matches 0..1",
        execute_as(hit_slime_selector,
        # execute as @e[type=minecraft:slime,sort=nearest,limit=1] run execute on attacker run execute if score @s player_turn_id = global turn_player run say yes, it was your turn
        # execute_as(at_e(tag=Tags.SELECTED_SLIME_TAG))
            execute_on("attacker",
                execute_if_score_equals_score(player_turn_id_score, turn_player_score, owner1=at_s(), to_run=
                    execute_as(hit_slime_selector,
                        add_tag("@s", Tags.SELECTED_SLIME_TAG) +
                        eval_macro(f"{REVEAL_COOLDOWN_SCORE} = 45")
                    )
                )
            )
        )
    )
)
def change_card_color(block):
    return f"fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 {block} replace #minecraft:mineable/pickaxe"

flip_card = OutputFile("flip_card", is_update_file=True)
flip_card.extend(
    execute_as(f"@e[tag={Tags.SELECTED_SLIME_TAG},tag=!{Tags.REVEALED_TAG}] at @s",
        [change_card_color("minecraft:red_concrete")] +
        execute_positioned("~ ~-4 ~", 
            add_delay(4, Tags.SPIN_DELAY_TAG) +
            execute_as_at_self(entity_selector(tag=Tags.ANIMAL_CARD,distance="..3"),
                add_tag("@s", Tags.SELECTED_MOB_TAG) +
                place_marker(tags=[Tags.REVEAL_CARD_TEMP_POS_TAG])
            ) + 
            tp(entity_selector(tag=Tags.ANIMAL_CARD,distance="..3"), "@s")
        ) +
        tp(entity_selector(tag=Tags.ANIMAL_CARD,distance="..3"), "~ ~.5 ~") +\
        add_tag("@s", Tags.REVEALED_TAG)
    )
)

check_match = OutputFile("check_match", is_update_file=True)
MATCHING_CARDS_COUNT_SCORE = "matching_count"
check_match.extend(set_score(MATCHING_CARDS_COUNT_SCORE, 0))
# check if two cards match
for animal in animals:
    check_match.extend(
        execute_if_score(MATCHING_CARDS_COUNT_SCORE, "matches ..1",
            store_count_entity_score(MATCHING_CARDS_COUNT_SCORE, f"@e[type={animal},tag={Tags.SELECTED_MOB_TAG}]")
        )
    )

go_to_next_player_turn = OutputFile("go_to_next_player_turn")
go_to_next_player_turn.extend(
    eval_macro(f"{turn_player_score} += 1"),
    scoreboard_operation(turn_player_score, '%=',total_player_count_score),
    announce("moving to next player's turn...")
)

found_match = OutputFile("found_match")
found_match.extend(
    execute_as_at(f"@e[tag={Tags.SELECTED_MOB_TAG}]",
        (
            [change_card_color("black_concrete")] +
            execute_if_score_equals(REVEAL_COOLDOWN_SCORE, 1,
                execute_as(
                    f"@e[tag={Tags.CARD_OUTLINE_TAG},distance=..2]",
                    smooth_remove("@s")
                ) +
                remove_tag("@s", Tags.SELECTED_MOB_TAG)
            )
        )
    ) +
    play_sound_at_pitches_based_on_score(REVEAL_COOLDOWN_SCORE, "minecraft:block.note_block.chime", [20, 30, 40], [0.3, 1, 1.7]) + 
    execute_if_score_equals(REVEAL_COOLDOWN_SCORE, 1,
        execute_as(players,
            execute_if_score_equals_score(player_turn_id_score, turn_player_score, owner1=at_s(),to_run=
                scoreboard_operation(player_matches_found_count, '+=', 1, at_s()) +
                call_function(go_to_next_player_turn)
            )
        )
    )
)

# found_match.append("say running found_match1")
# found_match.append("say running found_match2")


put_card_back_down = OutputFile("put_card_back_down")
put_card_back_down.extend(
    play_sound_at_pitches_based_on_score(REVEAL_COOLDOWN_SCORE, 
    "block.note_block.bit", [40, 30, 20], [1.7, 1, .3]) +
    execute_if_score_equals(REVEAL_COOLDOWN_SCORE, 1,
        execute_as_at_self(selector_entity(tags=Tags.SELECTED_MOB_TAG),
            tp("@s", selector_entity(type=MARKER_MOB,sort="nearest",limit=1)) +
            remove_tag("@s", Tags.SELECTED_MOB_TAG) +
            kill(selector_entity(tag=Tags.REVEAL_CARD_TEMP_POS_TAG))
        ) +
        execute_as_at_self(selector_entity(tag=Tags.SELECTED_SLIME_TAG), 
            [change_card_color("purple_concrete")] +
            remove_tag("@s", Tags.REVEALED_TAG) +
            remove_tag("@s", Tags.SELECTED_SLIME_TAG)
        ) + 
        call_function(go_to_next_player_turn)
    )
)


check_match.extend(
    execute_if_score(MATCHING_CARDS_COUNT_SCORE, "matches 2",
        allow_after_delay(Tags.SPIN_DELAY_TAG,
            call_function(found_match)
        )
    ) +
    execute_unless_score(MATCHING_CARDS_COUNT_SCORE, "matches 2",
        execute_if_score_equals(NUM_CARDS_SELECTED_COUNT_SCORE, 2,
            call_function(put_card_back_down)
        )
    )
)


number_of_winners_score = "number_of_winners"
calculate_winner = OutputFile("calculate_winner")
calculate_winner.extend(
    debug("calculating winner"),
    scoreboard_operation(highest_score, '>', player_matches_found_count, owner2=players),
    set_score(number_of_winners_score, 0),
    execute_as(at_a(), 
        execute_if_score_equals_score(player_matches_found_count, highest_score, owner1=at_s(), to_run=
            scoreboard_operation(number_of_winners_score, '+=', 1)
        )
    ),
    execute_if_score_matches(number_of_winners_score, '1', 
        raw(
            '''
            title @a subtitle {"text":"Wins!","color":"green"}
            title @a title [{"selector":"__players__","separator":" and ","color":"green","bold":true}]
            '''.replace("__players__", players)
        )
    ),
    execute_if_score_matches(number_of_winners_score, '2..', 
        raw(
            '''
            title @a subtitle {"text":"Tied!","color":"green"}
            title @a title [{"selector":"__players__","separator":" and ","color":"green","bold":true}]
            '''.replace("__players__", players)
        )
    )

)
check_game_complete = OutputFile("check_game_complete", is_update_file=True)
remaining_cards_score = "remaining_cards"
has_winner_been_found_score = "has_winner_been_found_score" 
check_game_complete.extend(
    set_score_to_count_of(remaining_cards_score, entity_selector(tag=Tags.CARD_OUTLINE_TAG)),
    execute_if_score_matches(has_winner_been_found_score, 0,
        execute_if_score_equals(remaining_cards_score, 0,
            call_function(calculate_winner) +
            set_score(has_winner_been_found_score, 1)
        )
    )
)

spin_revealed = OutputFile("spin_revealed", is_update_file=True)
spin_revealed.extend(
    run_when_tag_gone(Tags.SPIN_DELAY_TAG,
        execute_as_at_self(entity_selector(tag=Tags.SELECTED_MOB_TAG),
            # execute_if_divisible(game_clock_score, 5, 0, 
                "tp @s ~ ~ ~ ~45 ~"
            # )
        )
    )
    #     "tp @s ~ ~ ~ ~30 ~"
    #     # "tp @s ~ ~.5 ~ ~ ~"
    # )
    # execute_if_divisible(game_clock_score, 20, 20,
    #     "tp @s ~ ~-.5 ~ ~ ~"
    # ) 
)

assign_player_turn_order = OutputFile("assign_player_turn_order")

assign_player_turn_order.extend(
    set_score(turn_player_score, 0),
    set_score(current_player_id_being_assigned, 0),
    set_score(player_turn_id_score, -1,players),
    set_score_to_count_of(total_player_count_score, at_a())
)
for i in range(16):
    assign_player_turn_order.extend(execute_as(unassigned_players, 
        set_score_from_other_score(player_turn_id_score, current_player_id_being_assigned, at_s()),
    ))
    assign_player_turn_order.extend(scoreboard_operation(current_player_id_being_assigned, '+=', 1))
assign_player_turn_order.extend(announce("order has been assigned"))

reset_scores = OutputFile("reset_scores")
reset_scores.extend(
    set_score(player_matches_found_count, 0, players)
)

for i in range(NUMBER_OF_DIFFICULTIES):
    setup_game = OutputFile(f"setup_game_difficulty{i}")
    setup_game.extend(
        call_function(place_card_blocks.get_variant(i)),
        call_function(summon_animals.get_variant(i)),
        call_function(shuffle_mobs.get_variant(i)),
        call_function(place_slimes.get_variant(i)),
        call_function(reset_scores),
        call_function(assign_player_turn_order),
        smooth_remove(selector_entity(type=MARKER_MOB))
    )


end_of_tick_code = OutputFile("end_of_tick_code", is_update_file=True)
end_of_tick_code.extend(
    execute_if_score(REVEAL_COOLDOWN_SCORE, "matches 1..", 
        eval_macro(f"{REVEAL_COOLDOWN_SCORE} -= 1")
    )
)


# print("here")