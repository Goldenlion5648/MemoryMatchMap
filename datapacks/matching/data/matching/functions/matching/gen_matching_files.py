import itertools as it
import os
import sys
import json
import math
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
invisibility_effect = "invisibility"
lobby_center = (63.00, 4.00, -28.000)

create_scoreboard(game_clock_score, 0)
increment_each_tick(game_clock_score)
helper_update.append(f"team join passable {selector_entity(selector='@a',team='!passable')}")
helper_update.extend(
    effect_give(at_a(), "minecraft:saturation"),
    execute_at(lobby_center, 
        execute_as(at_a(distance='..20'),
            clear(at_s(gamemode='adventure'))
        )
    ),
    kill(at_e(type="item"))
    #TODO before release, uncomment
    # raw('gamemode adventure @a')

)

turn_player_score = "turn_player"
player_turn_id_score = "player_turn_id"
total_player_count_score = "total_player_count"
current_player_id_being_assigned = "current_player_id_being_assigned"
times_left_to_run = "times_left_to_run"
player_matches_found_count = "player_matches_found_count"
highest_score = "highest_score"
facedown_card_block = "blue_wool"
faceup_card_block = "red_wool"
complete_card_block = "green_wool"
selected_difficulty_score = "selected_difficulty"
is_make_it_take_it_mode_score = create_scoreboard("is_make_it_take_it_mode")


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
    "fox",
    "witch",
    "vex",
    "parrot",
    "frog",
    "llama",
    "cod",
    "skeleton_horse",
    "pufferfish",
    "rabbit",
    "ravager",
    "salmon",
    "sheep",
    "silverfish",
    "wither_skeleton",
    "iron_golem",
    "snow_golem",
    "polar_bear",
    "mooshroom",
    "guardian",
    "wolf",
    "zombified_piglin",
    "piglin_brute",
    "piglin",
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
place_card_blocks_holder = OutputFile("place_card_blocks_difficulty")
summon_animals_holder = OutputFile("summon_animals_difficulty")
place_slimes_holder = OutputFile("place_slimes_difficulty")
shuffle_mobs_holder = OutputFile("shuffle_mobs_difficulty")
difficulty_high_corners = []
for difficulty in range(NUMBER_OF_DIFFICULTIES):
    board_dim = SMALLEST_BOARD_DIM + difficulty*2
    place_card_blocks_holder.add_variant(difficulty)
    place_card_blocks = place_card_blocks_holder.get_variant(-1)
    summon_animals_holder.add_variant(difficulty)
    summon_animals = summon_animals_holder.get_variant(-1)
    place_slimes_holder.add_variant(difficulty)
    place_slimes = place_slimes_holder.get_variant(-1)
    shuffle_mobs_holder.add_variant(difficulty)
    shuffle_mobs = shuffle_mobs_holder.get_variant(-1)

    tile_lower_corners = []
    temp_card_tile_commands = []
    for x_counter in range(board_dim):
        for z_counter in range(board_dim):
            x = game_corner[0] + x_counter * (tile_dim + 1)
            z = game_corner[2] + z_counter * (tile_dim + 1)
            corner_x = x + 1
            corner_z = z + 1
            tile_lower_corners.append((corner_x, game_corner[1], corner_z))
            highest_corner = (x + tile_dim, game_corner[1], z + tile_dim)

            temp_card_tile_commands.append(
                f"fill {corner_x} {game_corner[1]} {corner_z} {tuple_to_string(highest_corner)} {facedown_card_block}"
            )

    
    highest_board_dim = SMALLEST_BOARD_DIM + (NUMBER_OF_DIFFICULTIES-1) * 2
    high_corners = [
        (   
            game_corner[0] + highest_board_dim**2, 
            game_corner[1], 
            game_corner[2] + highest_board_dim**2
        ), 
        highest_corner
    ]
    difficulty_high_corners.append(highest_corner)

    # first clears the largest possible area (if last difficulty played was
    # the hardest).
    for high_corner, block, mode in zip(high_corners, [AIR, "stone_bricks"], ["replace", "hollow"]):
        upper_shield_pos1 = tuple_to_string(element_wise(game_corner, [-1, 0, -1]))
        upper_shield_pos2 = tuple_to_string(element_wise(high_corner, [2, 6, 2]))
        if block == AIR:
            place_card_blocks.append(f"fill {upper_shield_pos1} {upper_shield_pos2} air")
        else:
            place_card_blocks.append(f"fill {upper_shield_pos1} {upper_shield_pos2} barrier outline")
        place_card_blocks.append(f"fill {tuple_to_string(game_corner)} {tuple_to_string(element_wise(high_corner, [1, -6, 1]))} {block} {mode}")
    # place_card_blocks.append(f"fill {tuple_to_string(game_corner)} {tuple_to_string(element_wise(high_corner, [1, -6, 1]))} barrier outline")

    outline_block = "yellow_glazed_terracotta"
    high_game_corner = element_wise(high_corner, [1, 0, 1])
    facing_order = ["north", "east", "west", "south"]
    # place border rows
    for x, facing in zip(range(game_corner[0], high_game_corner[0] + 1), it.cycle(facing_order)):
        for main_z in [game_corner[2], high_game_corner[2]]:
            place_card_blocks.append(f"setblock {x} {game_corner[1]} {main_z} yellow_glazed_terracotta[facing={facing}] replace")

    facing_order = ["north", "west", "east", "south"]
    # place border columns
    for z, facing in zip(range(game_corner[2], high_game_corner[2] + 1), it.cycle(facing_order)):
        for main_x in [game_corner[0], high_game_corner[0]]:
            place_card_blocks.append(f"setblock {main_x} {game_corner[1]} {z} {outline_block}[facing={facing}] replace")
    # place_card_blocks.append(f"fill {tuple_to_string(game_corner)} {tuple_to_string()} {outline_block} outline")

    place_card_blocks.extend(temp_card_tile_commands)
    summon_animals.extend(smooth_remove(entity_selector(tag=Tags.ANIMAL_CARD.value)))
    create_scoreboard("mob_id", 0)

    current_difficulty_animals = animals[:board_dim**2 // 2]
    
    for animal, (x, y, z) in zip(current_difficulty_animals*2, tile_lower_corners):
        summon_animals.append(
            f'summon {animal} {x + 1} {y - 3} {z + 1} ' + '{Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:' + format_tags_for_nbt([Tags.HIDDEN_CARD,Tags.ANIMAL_CARD]) + '}'
        )
    for i, animal in enumerate(current_difficulty_animals, 1):
        summon_animals.append(f"execute as @e[type={animal}] run scoreboard players set @s mob_id {i}")
    # summon_animals.append('tellraw @a "animals have been placed!"')

    place_slimes.append("tp @e[type=minecraft:slime] ~ ~-400 ~")
    for pos in tile_lower_corners:
        place_slimes.append(f"summon slime {tuple_to_string(element_wise(pos, [1, 1, 1]))} " + '{Silent:1b,Glowing:1b,Team:"passable",PersistenceRequired:1b,NoAI:1b,Size:0,Tags:["'+ f"{Tags.CARD_OUTLINE_TAG}" + '"],ActiveEffects:[{Id:11,Amplifier:55b,Duration:200000000,ShowParticles:0b},{Id:14,Amplifier:1b,Duration:200000000,ShowParticles:0b}]}')

    shuffle_mobs.extend(
        remove_tag(at_e(tag='hidden'), 'moved')
    )
    shuffle_mobs.extend(
        fisher_yates_single_pass * len(current_difficulty_animals) * 2
    )
    # execute as @e[tag=moving] run say was moved
    # shuffle_mobs.append('tellraw @a "cards have been shuffled!"')
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
                        eval_macro(f"{REVEAL_COOLDOWN_SCORE} = 50")
                    )
                )
            )
        )
    )
)
def change_card_color(block):
    return f"fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 {block} replace"
    
check_match = OutputFile("check_match")

flip_card = OutputFile("flip_card", is_update_file=True)
flip_card.extend(
    execute_as(f"@e[tag={Tags.SELECTED_SLIME_TAG},tag=!{Tags.REVEALED_TAG}] at @s",
        [change_card_color(faceup_card_block)] +
        execute_positioned("~ ~-4 ~", 
            summon_delay_cloud(4, Tags.SPIN_DELAY_TAG) +
            execute_as_at_self(entity_selector(tag=Tags.ANIMAL_CARD,distance="..3"),
                add_tag("@s", Tags.SELECTED_MOB_TAG) +
                place_marker(tags=[Tags.REVEAL_CARD_TEMP_POS_TAG])
            ) + 
            tp(entity_selector(tag=Tags.ANIMAL_CARD,distance="..3"), "@s")
        ) +
        tp(entity_selector(tag=Tags.ANIMAL_CARD,distance="..3"), "~ ~.5 ~") +\
        add_tag("@s", Tags.REVEALED_TAG)
    ) + 
    call_function(check_match)

)

MATCHING_CARDS_COUNT_SCORE = "matching_count"
check_match.extend(set_score(MATCHING_CARDS_COUNT_SCORE, 0))
# check if two cards match
for animal in animals:
    check_match.extend(
        execute_if_score(MATCHING_CARDS_COUNT_SCORE, "matches ..1",
            store_count_entity_score(MATCHING_CARDS_COUNT_SCORE, f"@e[type={animal},tag={Tags.SELECTED_MOB_TAG}]")
        )
    )

total_turns_taken = create_scoreboard("total_turns_taken")
go_to_next_player_turn = OutputFile("go_to_next_player_turn")
go_to_next_player_turn.extend(
    eval_macro(f"{total_turns_taken} += 1"),
    eval_macro(f"{turn_player_score} += 1"),
    scoreboard_operation(turn_player_score, '%=',total_player_count_score),

    execute_unless_score(total_player_count_score, 'matches 1', 
        announce("Moving to next player's turn...") +
        delay_code_block(
            raw('''/tellraw @a [{"text":"It is "},{"selector":"@a[scores={is_my_turn_score=1}]","color":"dark_aqua","bold":true},{"text":"'s turn"}]'''),
            1
        )
    )
    # announce("Make it, take it! Your move again!")
    # execute_if_score_equals(is_make_it_take_it_mode, 0,
    #     eval_macro(f"{turn_player_score} += 1"),
    #     scoreboard_operation(turn_player_score, '%=',total_player_count_score),
    # ),
    # execute_if_score_equals(is_make_it_take_it_mode, 1,
    # )
)

found_match = OutputFile("found_match")
found_match.extend(
    execute_as_at(f"@e[tag={Tags.SELECTED_MOB_TAG}]",
        (
            [change_card_color(complete_card_block)] +
            execute_if_score_equals(REVEAL_COOLDOWN_SCORE, 1,
                execute_as(
                    f"@e[tag={Tags.CARD_OUTLINE_TAG},distance=..2]",
                    smooth_remove("@s")
                ) +
                remove_tag("@s", Tags.SELECTED_MOB_TAG) + 
                remove_tag("@s", Tags.HIDDEN_CARD)
            )
        )
    ) +
    play_sound_at_pitches_based_on_score(REVEAL_COOLDOWN_SCORE, "minecraft:block.note_block.chime", [3, 11, 19, 27], [1.3, 1, .7, .4]) + 
    execute_if_score_equals(REVEAL_COOLDOWN_SCORE, 1,
        execute_as(players,
            execute_if_score_equals_score(player_turn_id_score, turn_player_score, owner1=at_s(),to_run=
                scoreboard_operation(player_matches_found_count, '+=', 1, at_s()) +
                execute_if_score_matches(is_make_it_take_it_mode_score, 0,
                    call_function(go_to_next_player_turn, 10)
                ) +
                execute_if_score_matches(is_make_it_take_it_mode_score, 1,
                    raw('''/tellraw @a [{"text":"Make it, take it! It is "},{"selector":"@a[scores={is_my_turn_score=1}]","color":"dark_aqua","bold":true},{"text":"'s turn again!"}]'''),
                )
            )
        )
    )
)

# found_match.append("say running found_match1")
# found_match.append("say running found_match2")


put_card_back_down = OutputFile("put_card_back_down")
put_card_back_down.extend(
    play_sound_at_pitches_based_on_score(REVEAL_COOLDOWN_SCORE, 
    "block.note_block.bit", [47, 39, 31, 23], [1.7, 1.2, .7, .2]) +
    execute_if_score_equals(REVEAL_COOLDOWN_SCORE, 1,
        execute_as_at_self(selector_entity(tags=Tags.SELECTED_MOB_TAG),
            tp("@s", selector_entity(type=MARKER_MOB,sort="nearest",limit=1)) +
            kill(selector_entity(tag=Tags.REVEAL_CARD_TEMP_POS_TAG,sort='nearest',limit=1)) + 
            remove_tag("@s", Tags.SELECTED_MOB_TAG)
        ) +
        execute_as_at_self(selector_entity(tag=Tags.SELECTED_SLIME_TAG), 
            [change_card_color(facedown_card_block)] +
            remove_tag("@s", Tags.REVEALED_TAG) +
            remove_tag("@s", Tags.SELECTED_SLIME_TAG)
        ) + 
        call_function(go_to_next_player_turn, 10)
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

celebration_sound = OutputFile("celebration_sound")
last_delay_mult = 6
occurrence_rate = 5 
celebration_sound.extend(
    it.chain(
        delay_code_block(
            playsound("minecraft:block.note_block.chime", .90 + .1*i), i*occurrence_rate
        )[0] for i in range(1, last_delay_mult)
    )
)
celebration_sound.extend(
    delay_code_block(
        playsound("minecraft:block.bell.use"), (last_delay_mult + 1)*occurrence_rate
    )
)

win_animation = OutputFile("win_animation")
win_animation.extend(
    it.chain.from_iterable(
        execute_if_score_matches(selected_difficulty_score, i,
            [ 
                execute_at(element_wise(pos, [0,4,0]),
                    raw(
                    '''summon firework_rocket ~ ~ ~ {FireworksItem:{id:"firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Type:2,Flicker:1b,Trail:1b,Colors:[I;15086110,5205247],FadeColors:[I;16772075]}]}}}}'''
                    )
                )[0] 
                for pos in get_four_corners(game_corner, difficulty_high_corners[i])
            ]
        )
        for i in range(NUMBER_OF_DIFFICULTIES)
    )
)
win_animation.extend(
    it.chain.from_iterable(
        delay_code_block(
            [
                execute_positioned(get_center(game_corner, difficulty_high_corners[diff]),
                    execute_if_score_matches(selected_difficulty_score, diff,
                        raw(
                            f'''fill ~-{i} ~ ~-{i} ~{i} ~ ~{i} diamond_block replace #minecraft:wool'''
                        ))
                )[0] for diff in range(NUMBER_OF_DIFFICULTIES)
            ], i*2
        ) for i in range(0, 40, 4)
    )
)

number_of_winners_score = "number_of_winners"
calculate_winner = OutputFile("calculate_winner")
calculate_winner.extend(
    # announce("calculating winner"),
    set_score(highest_score, 0),
    scoreboard_operation(highest_score, '>', player_matches_found_count, owner2=players),
    set_score(number_of_winners_score, 0),
    execute_as(players, 
        execute_if_score_equals_score(player_matches_found_count, highest_score, owner1=at_s(), to_run=
            scoreboard_operation(number_of_winners_score, '+=', 1)
        )
    ),
    execute_if_score_matches(number_of_winners_score, '1', 
        execute_as(players,
            execute_if_score_equals_score(
                player_matches_found_count, highest_score, 
                owner1=at_s(),
                to_run=raw(
                    '''
                    title @a title [{"selector":"@s","separator":" and ","color":"green","bold":true}]
                    title @a subtitle {"text":"Wins!","color":"green"}
                    '''
                )
            )
        )
    ),
    execute_if_score_matches(number_of_winners_score, '2..', 
        raw(
            '''
            title @a title [{"selector":"__players__","separator":" and ","color":"#FF822E","bold":true}]
            title @a subtitle {"text":"Tied!","color":"#FF822E"}
            '''.replace("__players__", players)
        ) + raw(
            '''
            tellraw @a [{"selector":"__players__","separator":" and ","color":"#FF822E","bold":true}]
            tellraw @a {"text":"Tied!","color":"#FF822E"}
            '''.replace("__players__", players)
        )
    ),
    execute_if_score_matches(number_of_winners_score, '1..',
        call_function(celebration_sound) + 
        call_function(win_animation) +
        delay_code_block(
            raw('''tellraw @a [{"text":"The game took "},{"score":{"name":"global","objective":"total_turns_taken"}},{"text":" turns!"}]'''),
            40
        )
    )

)
check_game_complete = OutputFile("check_game_complete", is_update_file=True)
remaining_cards_score = "remaining_cards"
has_winner_been_found_score = "has_winner_been_found" 
check_game_complete.extend(
    set_score_to_count_of(remaining_cards_score, entity_selector(tag=Tags.CARD_OUTLINE_TAG)),
    execute_if_score_matches(has_winner_been_found_score, 0,
        execute_if_score_equals(remaining_cards_score, 0,
            call_function(calculate_winner) +
            set_score(has_winner_been_found_score, 1)
        )
    )
)

send_player_to_lobby = OutputFile("send_player_to_lobby")
send_player_to_lobby.extend(
    tp(at_s(), lobby_center + (0,0)),
    raw('clear @s')
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

apply_invis = OutputFile("apply_invis", is_update_file=True)
edge_distance = abs(game_corner[0] - difficulty_high_corners[-1][0])
apply_invis.extend(
    execute_positioned(game_corner,
        effect_give(at_e(dy=-10,dx=edge_distance,dz=edge_distance,tag=Tags.ANIMAL_CARD), invisibility_effect) + 
        effect_clear(at_e(dy=10,dx=edge_distance,dz=edge_distance,tag=Tags.ANIMAL_CARD), invisibility_effect)
    )
    # effect(at_e(tags=[Tags.ANIMAL_CARD,f"!{Tags.REVEALED_TAG}",f"!{Tags.SELECTED_MOB_TAG}"],type="!player"), invisibility_effect) + 
    # effect_clear(at_e(tags=[Tags.ANIMAL_CARD],type="!player"), invisibility_effect)
)

run_correct_difficulty = OutputFile("run_correct_difficulty")
for i in range(NUMBER_OF_DIFFICULTIES):
    run_correct_difficulty.extend(
        execute_if_score_matches(selected_difficulty_score, i,
            call_function(f"setup_game_difficulty{i}")
        )
    )

assign_player_turn_order = OutputFile("assign_player_turn_order")

assign_player_turn_order.extend(
    set_score(turn_player_score, 0),
    set_score(current_player_id_being_assigned, 0),
    set_score(player_turn_id_score, -1, players),

    set_score_to_count_of(total_player_count_score, at_a())
)
for i in range(16):
    assign_player_turn_order.extend(execute_as(unassigned_players, 
        set_score_from_other_score(player_turn_id_score, current_player_id_being_assigned, at_s()),
    ))
    assign_player_turn_order.extend(scoreboard_operation(current_player_id_being_assigned, '+=', 1))
# assign_player_turn_order.extend(announce("order has been assigned"))

is_my_turn_score = create_scoreboard("is_my_turn_score")
diagonal_board_dist = int(math.dist(high_corners[-1], game_corner)) + 3
turn_player_code = OutputFile("turn_player_code", is_update_file=True, data=
    execute_at(high_corners[-1], 
        execute_as(at_a(distance=diagonal_board_dist),
            execute_if_score_equals_score(player_turn_id_score, turn_player_score, owner1=at_s(), to_run=
                raw('title @s actionbar {"text":"It is your turn","color":"dark_aqua","bold":true,"underlined":true}') +
                set_score(is_my_turn_score, 1, at_s()) +
                list_chain(
                    raw_formatted('''item replace entity @s hotbar._r1 with iron_sword{display:{Name:'{"text":"Card Flipper","color":"gray","bold":true,"italic":false}',Lore:['{"text":"Shows an indicator"}','{"text":"when a card"}','{"text":"is in range"}']},Unbreakable:1b}''', i)
                    for i in range(9)
                )
            ) +
            execute_unless_score_equals_score(player_turn_id_score, turn_player_score, owner1=at_s(), to_run=
                raw('title @s actionbar {"text":"Wait for your turn...","color":"red","bold":true,"underlined":true}') +
                set_score(is_my_turn_score, 0, at_s()) + 
                clear(at_s())
            )
        )   
    )
)

reset_scores = OutputFile("reset_scores")
reset_scores.extend(
    remove_scoreboard(player_matches_found_count),
    set_score(total_turns_taken, 0),
    add_scoreboard(player_matches_found_count, "Matches Found"),
    set_score(player_matches_found_count, 0, players),
    set_score(has_winner_been_found_score, 0),
    set_score(current_player_id_being_assigned, 0),
    raw(f'''scoreboard objectives setdisplay sidebar player_matches_found_count''')
    # set_score(selected_difficulty_score, 0)
)

give_powerups = OutputFile("give_powerups")
give_powerups.extend(

)

blind_and_freeze_others_effect = OutputFile("blind_and_freeze_others_effect")
blind_and_freeze_others_effect.extend(
    execute_as(at_a(distance='0.000001..'), 
        effect_give(at_s(), "minecraft:jump_boost", 8, 129) +
        effect_give(at_s(), "minecraft:slowness", 8, 255) +
        effect_give(at_s(), "minecraft:blindness", 8, 255) +
        tellraw("Looks like someone doesn't want you to see their moves!", at_s())
    )
)

# end_of_game_code = OutputFile("end_of_game_code")
tp_to_game_corner = OutputFile("tp_to_game_corner",
    tp(at_p(), element_wise(game_corner, [2, 2, 2]))
)

enter_existing_game_sign_logic = OutputFile("enter_existing_game_sign_logic", is_update_file=True)
enter_existing_game_sign_poses = [(62, 3, -22), (63, 3, -22)]
enter_existing_game_sign_logic.extend(
    execute_if_score_equals(has_winner_been_found_score, 0, 
        list_chain(
            raw_formatted('''setblock _r1 oak_wall_sign[facing=north]{Text2:'{"text":"Enter","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"function matching:matching/tp_to_game_corner"}}',Text3:'{"text":"Current Game","color":"green","bold":true}'}''', tuple_to_string(pos)) for pos in enter_existing_game_sign_poses
        ), 
        otherwise=
        list_chain(
            raw_formatted('''setblock _r1 air''', tuple_to_string(pos)) for pos in enter_existing_game_sign_poses
        )
    )
    # tp(at_a(), element_wise(game_corner, [2, 2, 2]))
)

start_game = OutputFile("start_game") 
start_game.extend(
    # tp(at_a(), element_wise(game_corner, [2, 2, 2])),
    call_function(run_correct_difficulty),
    announce("Starting game..."),
    delay_code_block(
        gamemode('adventure', at_a()) +
        execute_as_at(players, 
            call_function(tp_to_game_corner)
        ) + 
        delay_code_block(
            announce("During your turn, select a card by punching a small white cube outline."), 5
        ) +
        delay_code_block(
            announce("Then punch another white outline. If the revealed cards (mobs) match, they will stay revealed."), 25
        ) +
        delay_code_block(
            announce("If there is no match, both mobs will be flipped face down."), 45
        ),
        5
    )
)

difficulty_sign_pos = (69, 4, -30)
make_it_take_it_sign_pos = (69, 4, -29)
start_sign_poses = [
    (63, 4, -22),
    (62, 4, -22)
]
difficulty_sign = SettingSign(difficulty_sign_pos, 
'''oak_wall_sign[facing=west]{Text1:'{"text":"Current Difficulty","color":"white"}',Text2:'{"text":"_r1","color":"_r1","bold":true,"clickEvent":{"action":"run_command","value":"scoreboard players operation global selected_difficulty += const1 const"}}',Text4:'{"text":"_r1","color":"_r1"}'} replace''', 
selected_difficulty_score, 3)

for difficulty, color, size in ([
    ("Easy", 'green', '4 x 4'),
    ("Medium", 'gold', '6 x 6'),
    ("Hard", 'red', '8 x 8'),
]):
    difficulty_sign.append(difficulty, color, size, color)

make_it_take_it_sign = SettingSign(make_it_take_it_sign_pos, 
'''oak_wall_sign[facing=west]{Text2:'{"text":"Make It, Take It","color":"white"}',Text3:'{"text":"_r1","color":"_r1","bold":true,"clickEvent":{"action":"run_command","value":"scoreboard players operation global is_make_it_take_it_mode += const1 const"}}'} replace''', 
is_make_it_take_it_mode_score, 2)
make_it_take_it_sign.append("Disabled", 'red')
make_it_take_it_sign.append("Enabled", 'green')

sign_logic = OutputFile("sign_logic", is_update_file=True)
sign_logic.extend(
    difficulty_sign.build(),
    make_it_take_it_sign.build()
    # execute_if_score_equals(selected_difficulty_score, 0,
    #     setblock(difficulty_sign_pos, AIR) +
    #     raw_formatted('''setblock _r1 oak_wall_sign[facing=west]{Text1:'{"text":"Current Difficulty","color":"white"}',Text2:'{"text":"Easy","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"scoreboard players operation global selected_difficulty += const1 const"}}',Text4:'{"text":"4 x 4","color":"green"}'} replace''', tuple_to_string(difficulty_sign_pos)),
    # ),
    # macro(f"{selected_difficulty_score} %= {NUMBER_OF_DIFFICULTIES}"),
    # execute_if_score_equals(selected_difficulty_score, 1,
    #     setblock(difficulty_sign_pos, AIR) +
    #     raw_formatted('''setblock _r1 oak_wall_sign[facing=west]{Text1:'{"text":"Current Difficulty","color":"white"}',Text2:'{"text":"Medium","color":"gold","bold":true,"clickEvent":{"action":"run_command","value":"scoreboard players operation global selected_difficulty += const1 const"}}',Text4:'{"text":"6 x 6","color":"gold"}'} replace''', tuple_to_string(difficulty_sign_pos)),
    # ),
    # macro(f"{selected_difficulty_score} %= {NUMBER_OF_DIFFICULTIES}"),
    # execute_if_score_equals(selected_difficulty_score, 2,
    #     setblock(difficulty_sign_pos, AIR) +
    #     raw_formatted('''setblock _r1 oak_wall_sign[facing=west]{Text1:'{"text":"Current Difficulty","color":"white"}',Text2:'{"text":"Hard","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"scoreboard players operation global selected_difficulty += const1 const"}}',Text4:'{"text":"8 x 8","color":"red"}'} replace''', tuple_to_string(difficulty_sign_pos)),
    # ),
    # macro(f"{selected_difficulty_score} %= {NUMBER_OF_DIFFICULTIES}"),
    # # macro(f"{selected_difficulty_score} += 1"),


    
)


for i in range(NUMBER_OF_DIFFICULTIES):
    setup_game = OutputFile(f"setup_game_difficulty{i}")
    setup_game.extend(
        set_score(selected_difficulty_score, i),
        # announce("Shuffling cards!"),
        call_function(place_card_blocks_holder.get_variant(i)),
        call_function(summon_animals_holder.get_variant(i)),
        call_function(shuffle_mobs_holder.get_variant(i)),
        call_function(place_slimes_holder.get_variant(i)),
        call_function(reset_scores),
        call_function(assign_player_turn_order),
        smooth_remove(selector_entity(type=MARKER_MOB))
    )


end_of_tick_code = OutputFile("end_of_tick_code", is_update_file=True)
end_of_tick_code.extend(
    decrement_with_bound(REVEAL_COOLDOWN_SCORE, 0)
    # say("decremented", REVEAL_COOLDOWN_SCORE)
    # execute_if_score(REVEAL_COOLDOWN_SCORE, "matches 1..", 
    #     eval_macro(f"{REVEAL_COOLDOWN_SCORE} -= 1")
    # )
)


# print("here")
# print(highest_corner)