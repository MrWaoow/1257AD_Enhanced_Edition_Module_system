###################################################
# header_common.py
# This file contains common declarations.
# DO NOT EDIT THIS FILE!
###################################################

#client events
multiplayer_event_set_item_selection                          = 0
multiplayer_event_set_bot_selection                           = 1
multiplayer_event_admin_start_map                             = 2
multiplayer_event_admin_set_max_num_players                   = 3
multiplayer_event_admin_set_num_bots_in_team                  = 4
multiplayer_event_admin_set_friendly_fire                     = 5
multiplayer_event_admin_set_ghost_mode                        = 6
multiplayer_event_admin_set_control_block_dir                 = 7
multiplayer_event_admin_set_add_to_servers_list               = 8
multiplayer_event_admin_set_respawn_period                    = 9
multiplayer_event_admin_set_game_max_minutes                  = 10
multiplayer_event_admin_set_round_max_seconds                 = 11
multiplayer_event_admin_set_game_max_points                   = 12
multiplayer_event_admin_set_point_gained_from_flags           = 13
multiplayer_event_admin_set_point_gained_from_capturing_flag  = 14
multiplayer_event_admin_set_server_name                       = 15
multiplayer_event_admin_set_game_password                     = 16
multiplayer_event_admin_set_team_faction                      = 17
multiplayer_event_open_admin_panel                            = 18
multiplayer_event_change_team_no                              = 19
multiplayer_event_change_troop_id                             = 20
multiplayer_event_start_new_poll                              = 21
multiplayer_event_answer_to_poll                              = 22
multiplayer_event_admin_kick_player                           = 23
multiplayer_event_admin_ban_player                            = 24
multiplayer_event_admin_set_num_bots_voteable                 = 25
multiplayer_event_admin_set_factions_voteable                 = 26
multiplayer_event_admin_set_maps_voteable                     = 27
multiplayer_event_admin_set_player_respawn_as_bot             = 28
multiplayer_event_admin_set_combat_speed                      = 29
multiplayer_event_admin_set_respawn_count                     = 30
multiplayer_event_admin_set_kick_voteable                     = 31
multiplayer_event_admin_set_ban_voteable                      = 32
multiplayer_event_admin_set_valid_vote_ratio                  = 33
multiplayer_event_admin_set_auto_team_balance_limit           = 34
multiplayer_event_admin_set_welcome_message                   = 35
multiplayer_event_admin_set_initial_gold_multiplier           = 36
multiplayer_event_admin_set_battle_earnings_multiplier        = 37
multiplayer_event_admin_set_round_earnings_multiplier         = 38
multiplayer_event_admin_set_melee_friendly_fire               = 39
multiplayer_event_admin_set_friendly_fire_damage_self_ratio   = 40
multiplayer_event_admin_set_friendly_fire_damage_friend_ratio = 41
multiplayer_event_admin_set_allow_player_banners              = 42
multiplayer_event_admin_set_force_default_armor               = 43
multiplayer_event_admin_set_anti_cheat                        = 44
multiplayer_event_open_game_rules                             = 45
multiplayer_event_offer_duel                                  = 46
multiplayer_event_admin_set_disallow_ranged_weapons           = 47
#INVASION MODE START
multiplayer_event_other_events                                = 48


#other client events
multiplayer_event_other_event_set_bot_purchase                = 0
multiplayer_event_other_event_ccoop_lock_companions           = 1
multiplayer_event_coop_set_agent_team_and_group               = 2
multiplayer_event_other_event_ccoop_count_down_visible		  = 3
multiplayer_event_other_event_ccoop_count_down_invisible	  = 4
multiplayer_event_other_spawn_prison_cart					  = 5
multiplayer_event_other_destroy_prison_cart					  = 6

multiplayer_event_other_event_ccoop_update_spawn_data_1		  = 7
multiplayer_event_other_event_ccoop_update_spawn_data_2		  = 8
multiplayer_event_other_event_ccoop_update_spawn_data_3		  = 9
multiplayer_event_other_event_ccoop_update_spawn_data_4		  = 10
multiplayer_event_other_event_ccoop_update_spawn_data_5		  = 11
multiplayer_event_other_event_ccoop_update_spawn_data_6		  = 12

multiplayer_event_other_events_change_companion_level 		  = 13
multiplayer_event_admin_set_ccoop_difficulty                  = 14
multiplayer_event_other_event_unequip_item			 		  = 15
multiplayer_event_other_event_equip_item			 		  = 16
multiplayer_event_coop_send_drop_assignment_to_server         = 17
multiplayer_event_coop_set_agent_team_and_group               = 18
#INVASION MODE END

#server events
multiplayer_event_return_max_num_players                      = 50
multiplayer_event_return_num_bots_in_team                     = 51
multiplayer_event_return_friendly_fire                        = 52
multiplayer_event_return_ghost_mode                           = 53
multiplayer_event_return_control_block_dir                    = 54
multiplayer_event_return_combat_speed                         = 55
multiplayer_event_return_add_to_servers_list                  = 56
multiplayer_event_return_respawn_period                       = 57
multiplayer_event_return_game_max_minutes                     = 58
multiplayer_event_return_round_max_seconds                    = 59
multiplayer_event_return_game_max_points                      = 60
multiplayer_event_return_point_gained_from_flags              = 61
multiplayer_event_return_point_gained_from_capturing_flag     = 62
multiplayer_event_return_server_name                          = 63
multiplayer_event_return_game_password                        = 64
multiplayer_event_return_game_type                            = 65
multiplayer_event_return_confirmation                         = 66
multiplayer_event_return_rejection                            = 67
multiplayer_event_show_multiplayer_message                    = 68
multiplayer_event_draw_this_round                             = 69
multiplayer_event_set_attached_scene_prop                     = 70
multiplayer_event_set_team_flag_situation                     = 71
multiplayer_event_set_team_score                              = 72
multiplayer_event_set_num_agents_around_flag                  = 73
multiplayer_event_ask_for_poll                                = 74
multiplayer_event_change_flag_owner                           = 75
multiplayer_event_use_item                                    = 76
multiplayer_event_set_scene_prop_open_or_close                = 77
multiplayer_event_set_round_start_time                        = 78
multiplayer_event_force_start_team_selection                  = 79
multiplayer_event_start_death_mode                            = 80
multiplayer_event_return_num_bots_voteable                    = 81
multiplayer_event_return_factions_voteable                    = 82
multiplayer_event_return_maps_voteable                        = 83
multiplayer_event_return_next_team_faction                    = 84
multiplayer_event_return_player_respawn_as_bot                = 85
multiplayer_event_set_player_score_kill_death                 = 86
multiplayer_event_set_day_time                                = 87
multiplayer_event_return_respawn_count                        = 88
multiplayer_event_return_player_respawn_spent                 = 89
multiplayer_event_return_kick_voteable                        = 90
multiplayer_event_return_ban_voteable                         = 91
multiplayer_event_return_valid_vote_ratio                     = 92
multiplayer_event_return_auto_team_balance_limit              = 93
multiplayer_event_return_initial_gold_multiplier              = 94
multiplayer_event_return_battle_earnings_multiplier           = 95
multiplayer_event_return_round_earnings_multiplier            = 96
multiplayer_event_return_renaming_server_allowed              = 97
multiplayer_event_return_changing_game_type_allowed           = 98
multiplayer_event_return_melee_friendly_fire                  = 99
multiplayer_event_return_friendly_fire_damage_self_ratio      = 100
multiplayer_event_return_friendly_fire_damage_friend_ratio    = 101
multiplayer_event_return_allow_player_banners                 = 102
multiplayer_event_return_force_default_armor                  = 103
multiplayer_event_return_anti_cheat                           = 104
multiplayer_event_return_open_game_rules                      = 105
multiplayer_event_return_max_num_bots                         = 106
multiplayer_event_return_server_mission_timer_while_player_joined = 107
multiplayer_event_show_duel_request                           = 108
multiplayer_event_start_duel                                  = 109
multiplayer_event_cancel_duel                                 = 110
multiplayer_event_show_server_message                         = 111
multiplayer_event_return_disallow_ranged_weapons              = 112
#INVASION MODE START
multiplayer_event_return_set_bot_selection                    = 113 
multiplayer_event_return_team_ratio                           = 114
multiplayer_event_return_squad_size                           = 115
multiplayer_event_return_disallow_granades                    = 116
multiplayer_event_return_sound_at_pos                         = 117
multiplayer_event_return_enable_cbf_squad_ratio				  = 118
multiplayer_event_return_cbf_squad_ratio					  = 119
multiplayer_event_coop_drop_item                              = 120
multiplayer_event_coop_chest_opened                           = 121
multiplayer_event_return_ccoop_difficulty                     = 122
multiplayer_event_ccoop_victory_message                       = 123
multiplayer_event_ccoop_return_of_the_king                    = 124
#INVASION MODE END

#multiplayer message types
multiplayer_message_type_auto_team_balance_done      = 2
multiplayer_message_type_auto_team_balance_next      = 3
multiplayer_message_type_capture_the_flag_score      = 4
multiplayer_message_type_flag_returned_home          = 5
multiplayer_message_type_capture_the_flag_stole      = 6
multiplayer_message_type_poll_result                 = 7
multiplayer_message_type_flag_neutralized            = 8
multiplayer_message_type_flag_captured               = 9
multiplayer_message_type_flag_is_pulling             = 10
multiplayer_message_type_auto_team_balance_no_need   = 11
multiplayer_message_type_round_result_in_battle_mode = 12
multiplayer_message_type_round_result_in_siege_mode  = 13
multiplayer_message_type_round_draw                  = 14
multiplayer_message_type_target_destroyed            = 15
multiplayer_message_type_defenders_saved_n_targets   = 16
multiplayer_message_type_attackers_won_the_round     = 17
multiplayer_message_type_start_death_mode            = 18

#multiplayer game type indices
multiplayer_game_type_deathmatch             = 0
multiplayer_game_type_team_deathmatch        = 1
multiplayer_game_type_battle                 = 2
multiplayer_game_type_destroy                = 3
multiplayer_game_type_capture_the_flag       = 4
multiplayer_game_type_headquarters           = 5
multiplayer_game_type_siege                  = 6
multiplayer_game_type_duel                   = 7
#INVASION MODE START
multiplayer_game_type_captain_coop           = 8
multiplayer_num_game_types                   = 9
#INVASION MODE END

#admin panel value ranges
multiplayer_round_max_seconds_min            = 60
multiplayer_round_max_seconds_max            = 901
multiplayer_respawn_period_min               = 3
multiplayer_respawn_period_max               = 31 #can only be 30 seconds max (due to agent deletion after that period)

multiplayer_siege_mod_defender_team_extra_respawn_time = 27 #It was 20 in 1.113 but it is increased it to 25 in 1.121 because defenders were mostly defeating enemy.
multiplayer_new_agents_finish_spawning_time = 30
multiplayer_max_possible_player_id = 1000

#team 1 and team 2 are 0 and 1 respectively
multi_team_spectator = 2
multi_team_unassigned = multi_team_spectator + 1

multi_data_maps_for_game_type_begin = 0
multi_data_maps_for_game_type_end = multi_data_maps_for_game_type_begin + 30
multi_data_troop_button_indices_begin = multi_data_maps_for_game_type_end
multi_data_troop_button_indices_end = multi_data_troop_button_indices_begin + 16 #maximum 16 troops per faction
multi_data_item_button_indices_begin = multi_data_troop_button_indices_end
multi_data_item_button_indices_end = multi_data_item_button_indices_begin + 100 #maximum 100 items per troop
multi_data_flag_owner_begin = multi_data_item_button_indices_end
multi_data_flag_owner_end = multi_data_flag_owner_begin + 10 #maximum of 10 flags per scene
multi_data_flag_players_around_begin = multi_data_flag_owner_end 
multi_data_flag_players_around_end = multi_data_flag_players_around_begin + 10 #maximum of 10 flags per scene
multi_data_flag_owned_seconds_begin = multi_data_flag_players_around_end
multi_data_flag_owned_seconds_end = multi_data_flag_owned_seconds_begin + 10 #maximum of 10 flags per scene
multi_data_flag_pull_code_begin = multi_data_flag_owned_seconds_end
multi_data_flag_pull_code_end = multi_data_flag_pull_code_begin + 10 #maximum of 10 flags per scene
#INVASION MODE START
multi_data_ccoop_wave_spawn_data_begin = multi_data_flag_pull_code_end
multi_data_ccoop_wave_spawn_data_end = multi_data_ccoop_wave_spawn_data_begin + 16 #maximum of 5 different troop types, amounts and entry points (+ 1 for count)
multi_data_equipment_holder_begin = multi_data_ccoop_wave_spawn_data_end
multi_data_equipment_holder_end = multi_data_equipment_holder_begin + 9
multi_data_player_index_list_begin = multi_data_equipment_holder_end
#INVASION MODE END

#Entry points 100..109 is used for showing initial points for moveable and usable scene props like siege ladder.
multi_entry_points_for_usable_items_start = 100
multi_entry_points_for_usable_items_end = multi_entry_points_for_usable_items_start + 10


#multi_item_class_type_other = 0
multi_item_class_type_sword = 1
multi_item_class_type_axe = 2
multi_item_class_type_blunt = 3
multi_item_class_type_war_picks = 4
multi_item_class_type_cleavers = 5
multi_item_class_type_two_handed_sword = 6
multi_item_class_type_two_handed_axe = 7
multi_item_class_type_spear = 8
multi_item_class_type_lance = 9
multi_item_class_type_small_shield = 10
multi_item_class_type_large_shield = 11
multi_item_class_type_bow = 12
multi_item_class_type_crossbow = 13
multi_item_class_type_arrow = 14
multi_item_class_type_bolt = 15
multi_item_class_type_throwing = 16
multi_item_class_type_throwing_axe = 17
multi_item_class_type_horse = 18
multi_item_class_type_light_armor = 19
multi_item_class_type_medium_armor = 20
multi_item_class_type_heavy_armor = 21
multi_item_class_type_light_helm = 22
multi_item_class_type_heavy_helm = 23
multi_item_class_type_light_foot = 24
multi_item_class_type_heavy_foot = 25
multi_item_class_type_glove = 26

multi_item_class_type_melee_weapons_begin = multi_item_class_type_sword
multi_item_class_type_melee_weapons_end = multi_item_class_type_small_shield
multi_item_class_type_ranged_weapons_begin = multi_item_class_type_bow
multi_item_class_type_ranged_weapons_end = multi_item_class_type_horse
multi_item_class_type_shields_begin = multi_item_class_type_melee_weapons_end
multi_item_class_type_shields_end = multi_item_class_type_bow

multi_item_class_type_weapons_begin = multi_item_class_type_sword
multi_item_class_type_weapons_end = multi_item_class_type_horse
multi_item_class_type_horses_begin = multi_item_class_type_weapons_end
multi_item_class_type_horses_end = multi_item_class_type_light_armor
multi_item_class_type_bodies_begin = multi_item_class_type_horses_end
multi_item_class_type_bodies_end = multi_item_class_type_light_helm
multi_item_class_type_heads_begin = multi_item_class_type_bodies_end
multi_item_class_type_heads_end = multi_item_class_type_light_foot
multi_item_class_type_feet_begin = multi_item_class_type_heads_end
multi_item_class_type_feet_end = multi_item_class_type_glove
multi_item_class_type_gloves_begin = multi_item_class_type_feet_end
multi_item_class_type_gloves_end = multi_item_class_type_glove + 1

multi_troop_class_other = 0
multi_troop_class_infantry = 1
multi_troop_class_spearman = 2
multi_troop_class_cavalry = 3
multi_troop_class_archer = 4
multi_troop_class_crossbowman = 5
multi_troop_class_mounted_archer = 6
multi_troop_class_mounted_crossbowman = 7

multi_num_valid_entry_points = 64
multi_num_valid_entry_points_div_2 = 32

#normal money management system
multi_battle_round_team_money_add = 500
multi_destroy_save_or_destroy_target_money_add = 100
multi_destroy_target_money_add = 1500
multi_initial_gold_value = 1000
multi_max_gold_that_can_be_stored = 15000

multi_killer_agent_standard_money_add = 150 #(2/3 = 100 for battle & destroy, 3/3 = 150 for siege, 4/3 = 200 for deathmatch/team deathmatch/capture the flag/headquarters)
multi_killer_agent_loot_percentage_share = 12 #(2/3 = 8% for battle & destroy, 3/3 = 12% for siege, 4/3 = 16% for deathmatch/team deathmatch/capture the flag/headquarters)
multi_dead_agent_loot_percentage_share = 48 #(2/3 = 32% for battle & destroy, 3/3 = 48% for siege, 4/3 = 64% for deathmatch/team deathmatch/capture the flag/headquarters)
multi_minimum_gold = 1000 #(same in all modes)

multi_minimum_target_health = 1200

multi_max_seconds_flag_can_stay_in_ground = 60

multi_capture_the_flag_score_flag_returning = 1

multi_initial_spawn_point_team_1 = 0
multi_initial_spawn_point_team_2 = 32
multi_base_point_team_1 = 64
multi_base_point_team_2 = 65
multi_siege_flag_point = 66
multi_death_mode_point = 67

multi_headquarters_pole_height = 900
multi_headquarters_flag_height_to_win = 800 #used in sd death mode
multi_headquarters_flag_initial_height = 100 #used in sd death mode
multi_headquarters_max_distance_sq_to_raise_flags = 1600 #4m * 4m * 100 = 1600
multi_headquarters_distance_sq_to_set_flag = 8100 #9m * 9m * 100 = 8100 
multi_headquarters_distance_sq_to_change_flag = 400 #2m * 2m * 100 = 400 
multi_headquarters_distance_to_change_flag = 200 #2m * 100 = 200 
multi_distance_sq_to_use_belfry = 36 #6m * 6m = 36 (there is no * 100 for this one because it uses get_sq_distance_between_positions_in_meters instead of get_sq_distance_between_positions)
multi_max_sq_dist_between_agents_to_longer_mof_time = 49 #7m * 7m = 49m
min_allowed_flag_height_difference_to_make_score = 50

#these two values are about when master of field will be kicked
multiplayer_battle_formula_value_a = 15
multiplayer_battle_formula_value_b = 18000 #think about 18000-20000 if death mod very much happens.

multiplayer_spawn_above_opt_enemy_dist_point = 32 #while finding most suitable spawn point if nearest enemy is further than 32 meters give negative points to that spawn point
multiplayer_spawn_min_enemy_dist_limit = 45 #while finding most suitable spawn point if nearest enemy is closer than 45 meters give negative points to that spawn point, (squared increase)

multiplayer_poll_disable_period = 900 #15 minutes

#INVASION MODE START
multi_distance_to_captain_spaw_point = 15*100
multi_killer_captain_add = 60
multi_captain_recomended_players_max = 16
multi_killer_captain_coop_add = 200
#multi_captain_coop_round_duration_in_sec = 600 # 10 minutes
#INVASION MODE END

#menu variables
escape_menu_item_height = 40



bignum = 0x40000000000000000000000000000000

op_num_value_bits = 24 + 32

tag_register        =  1
tag_variable        =  2
tag_string          =  3
tag_item            =  4
tag_troop           =  5
tag_faction         =  6
tag_quest           =  7
tag_party_tpl       =  8
tag_party           =  9
tag_scene           = 10
tag_mission_tpl     = 11
tag_menu            = 12
tag_script          = 13
tag_particle_sys    = 14
tag_scene_prop      = 15
tag_sound           = 16
tag_local_variable  = 17
tag_map_icon        = 18
tag_skill           = 19
tag_mesh            = 20
tag_presentation    = 21
tag_quick_string    = 22
tag_track	    = 23
tag_tableau         = 24
tag_animation       = 25
tags_end            = 26


opmask_register             =  tag_register       << op_num_value_bits
opmask_variable             =  tag_variable       << op_num_value_bits
##opmask_string             =  tag_string         << op_num_value_bits
##opmask_item_index         =  tag_item           << op_num_value_bits
##opmask_troop_index        =  tag_troop          << op_num_value_bits
##opmask_faction_index      =  tag_faction        << op_num_value_bits
opmask_quest_index          =  tag_quest          << op_num_value_bits
##opmask_p_template_index   =  tag_party_tpl      << op_num_value_bits
##opmask_party_index        =  tag_party          << op_num_value_bits
##opmask_scene_index        =  tag_scene          << op_num_value_bits
##opmask_mission_tpl_index  =  tag_mission_tpl    << op_num_value_bits
##opmask_menu_index         =  tag_menu           << op_num_value_bits
##opmask_script             =  tag_script         << op_num_value_bits
##opmask_particle_sys       =  tag_particle_sys   << op_num_value_bits
##opmask_scene_prop         =  tag_scene_prop     << op_num_value_bits
##opmask_sound              =  tag_sound          << op_num_value_bits
##opmask_map_icon           =  tag_map_icon       << op_num_value_bits
opmask_local_variable       =  tag_local_variable << op_num_value_bits
opmask_quick_string         =  tag_quick_string   << op_num_value_bits


def reg(reg_no):
  if (reg_no < 0):
    print ("Error register_no negative")
    cause_error()
  return opmask_register | reg_no

def find_object(objects,object_id):
  result = -1
  num_objects = len(objects)
  i_object = 0
  object_id_lowercase = object_id.lower()
  while (i_object < num_objects) and (result == -1):
    object = objects[i_object]
    if (object[0].lower() == object_id_lowercase):
      result = i_object
    i_object += 1
  return result

s0  =  0
s1  =  1
s2  =  2
s3  =  3
s4  =  4
s5  =  5
s6  =  6
s7  =  7
s8  =  8
s9  =  9
s10 = 10
s11 = 11
s12 = 12
s13 = 13
s14 = 14
s15 = 15
s16 = 16
s17 = 17
s18 = 18
s19 = 19
s20 = 20
s21 = 21
s22 = 22
s23 = 23
s24 = 24
s25 = 25
s26 = 26
s27 = 27
s28 = 28
s29 = 29
s30 = 30
s31 = 31
s32 = 32
s33 = 33
s34 = 34
s35 = 35
s36 = 36
s37 = 37
s38 = 38
s39 = 39
s40 = 40
s41 = 41
s42 = 42
s43 = 43
s44 = 44
s45 = 45
s46 = 46
s47 = 47
s48 = 48
s49 = 49
s50 = 50
s51 = 51
s52 = 52
s53 = 53
s54 = 54
s55 = 55
s56 = 56
s57 = 57
s58 = 58
s59 = 59
s60 = 60
s61 = 61
s62 = 62
s63 = 63

s64 = 64
s65 = 65
s66 = 66
s67 = 67
s68 = 68
s69 = 69
s70 = 70
s71 = 71
s72 = 72
s73 = 73
s74 = 74
s75 = 75
s76 = 76
s77 = 77
s78 = 78


pos0 = 0
pos1 = 1
pos2 = 2
pos3 = 3
pos4 = 4
pos5 = 5
pos6 = 6
pos7 = 7
pos8 = 8
pos9 = 9
pos10 = 10
pos11 = 11
pos12 = 12
pos13 = 13
pos14 = 14
pos15 = 15
pos16 = 16
pos17 = 17
pos18 = 18
pos19 = 19
pos20 = 20
pos21 = 21
pos22 = 22
pos23 = 23
pos24 = 24
pos25 = 25
pos26 = 26
pos27 = 27
pos28 = 28
pos29 = 29
pos30 = 30
pos31 = 31
pos32 = 32
pos33 = 33
pos34 = 34
pos35 = 35
pos36 = 36
pos37 = 37
pos38 = 38
pos39 = 39
pos40 = 40
pos41 = 41
pos42 = 42
pos43 = 43
pos44 = 44
pos45 = 45
pos46 = 46
pos47 = 47
pos48 = 48
pos49 = 49
pos50 = 50
pos51 = 51
pos52 = 52
pos53 = 53
pos54 = 54
pos55 = 55
pos56 = 56
pos57 = 57
pos58 = 58
pos59 = 59
pos60 = 60
pos61 = 61
pos62 = 62
pos63 = 63
pos64 = 64
pos65 = 65
pos66 = 66
pos67 = 67
pos68 = 68
pos69 = 69
pos70 = 70
pos71 = 71
pos72 = 72
pos73 = 73
pos74 = 74
pos75 = 75
pos76 = 76
pos77 = 77
pos78 = 78
pos79 = 79
pos80 = 80
pos81 = 81
pos82 = 82
pos83 = 83
pos84 = 84
pos85 = 85
pos86 = 86
pos87 = 87
pos88 = 88
pos89 = 89
pos90 = 90
pos91 = 91
pos92 = 92
pos93 = 93
pos94 = 94
pos95 = 95
pos96 = 96
pos97 = 97
pos98 = 98
pos99 = 99
pos100 = 100
pos101 = 101
pos102 = 102
pos103 = 103
pos104 = 104
pos105 = 105
pos106 = 106
pos107 = 107
pos108 = 108
pos109 = 109
pos110 = 110
pos111 = 111
pos112 = 112
pos113 = 113
pos114 = 114
pos115 = 115
pos116 = 116
pos117 = 117
pos118 = 118
pos119 = 119
pos120 = 120
pos121 = 121
pos122 = 122
pos123 = 123
pos124 = 124
pos125 = 125
pos126 = 126
pos127 = 127
pos128 = 128
pos129 = 129
pos130 = 130
pos131 = 131
pos132 = 132
pos133 = 133
pos134 = 134
pos135 = 135
pos136 = 136
pos137 = 137
pos138 = 138
pos139 = 139
pos140 = 140
pos141 = 141
pos142 = 142
pos143 = 143
pos144 = 144
pos145 = 145
pos146 = 146
pos147 = 147
pos148 = 148
pos149 = 149
pos150 = 150
pos151 = 151
pos152 = 152
pos153 = 153
pos154 = 154
pos155 = 155
pos156 = 156
pos157 = 157
pos158 = 158
pos159 = 159
pos160 = 160
pos161 = 161
pos162 = 162
pos163 = 163
pos164 = 164
pos165 = 165
pos166 = 166
pos167 = 167
pos168 = 168
pos169 = 169
pos170 = 170
pos171 = 171
pos172 = 172
pos173 = 173
pos174 = 174
pos175 = 175
pos176 = 176
pos177 = 177
pos178 = 178
pos179 = 179
pos180 = 180
pos181 = 181
pos182 = 182
pos183 = 183
pos184 = 184
pos185 = 185
pos186 = 186
pos187 = 187
pos188 = 188
pos189 = 189
pos190 = 190
pos191 = 191
pos192 = 192
pos193 = 193
pos194 = 194
pos195 = 195
pos196 = 196
pos197 = 197
pos198 = 198
pos199 = 199
pos200 = 200
pos201 = 201
pos202 = 202
pos203 = 203
pos204 = 204
pos205 = 205
pos206 = 206
pos207 = 207
pos208 = 208
pos209 = 209
pos210 = 210
pos211 = 211
pos212 = 212
pos213 = 213
pos214 = 214
pos215 = 215
pos216 = 216
pos217 = 217
pos218 = 218
pos219 = 219
pos220 = 220
pos221 = 221
pos222 = 222
pos223 = 223
pos224 = 224
pos225 = 225
pos226 = 226
pos227 = 227
pos228 = 228
pos229 = 229
pos230 = 230
pos231 = 231
pos232 = 232
pos233 = 233
pos234 = 234
pos235 = 235
pos236 = 236
pos237 = 237
pos238 = 238
pos239 = 239
pos240 = 240
pos241 = 241
pos242 = 242
pos243 = 243
pos244 = 244
pos245 = 245
pos246 = 246
pos247 = 247
pos248 = 248
pos249 = 249
pos250 = 250
pos251 = 251
pos252 = 252
pos253 = 253
pos254 = 254
pos255 = 255
pos256 = 256
pos257 = 257
pos258 = 258
pos259 = 259
pos260 = 260
pos261 = 261
pos262 = 262
pos263 = 263
pos264 = 264
pos265 = 265
pos266 = 266
pos267 = 267
pos268 = 268
pos269 = 269
pos270 = 270
pos271 = 271
pos272 = 272
pos273 = 273
pos274 = 274
pos275 = 275
pos276 = 276
pos277 = 277
pos278 = 278
pos279 = 279
pos280 = 280
pos281 = 281
pos282 = 282
pos283 = 283
pos284 = 284
pos285 = 285
pos286 = 286
pos287 = 287
pos288 = 288
pos289 = 289
pos290 = 290
pos291 = 291
pos292 = 292
pos293 = 293
pos294 = 294
pos295 = 295
pos296 = 296
pos297 = 297
pos298 = 298
pos299 = 299
pos300 = 300
pos301 = 301
pos302 = 302
pos303 = 303
pos304 = 304
pos305 = 305
pos306 = 306
pos307 = 307
pos308 = 308
pos309 = 309
pos310 = 310
pos311 = 311
pos312 = 312
pos313 = 313
pos314 = 314
pos315 = 315
pos316 = 316
pos317 = 317
pos318 = 318
pos319 = 319
pos320 = 320
pos321 = 321
pos322 = 322
pos323 = 323
pos324 = 324
pos325 = 325
pos326 = 326
pos327 = 327
pos328 = 328
pos329 = 329
pos330 = 330
pos331 = 331
pos332 = 332
pos333 = 333
pos334 = 334
pos335 = 335
pos336 = 336
pos337 = 337
pos338 = 338
pos339 = 339
pos340 = 340
pos341 = 341
pos342 = 342
pos343 = 343
pos344 = 344
pos345 = 345
pos346 = 346
pos347 = 347
pos348 = 348
pos349 = 349
pos350 = 350
pos351 = 351
pos352 = 352
pos353 = 353
pos354 = 354
pos355 = 355
pos356 = 356
pos357 = 357
pos358 = 358
pos359 = 359
pos360 = 360
pos361 = 361
pos362 = 362
pos363 = 363
pos364 = 364
pos365 = 365
pos366 = 366
pos367 = 367
pos368 = 368
pos369 = 369
pos370 = 370
pos371 = 371
pos372 = 372
pos373 = 373
pos374 = 374
pos375 = 375
pos376 = 376
pos377 = 377
pos378 = 378
pos379 = 379
pos380 = 380
pos381 = 381
pos382 = 382
pos383 = 383
pos384 = 384
pos385 = 385
pos386 = 386
pos387 = 387
pos388 = 388
pos389 = 389
pos390 = 390
pos391 = 391
pos392 = 392
pos393 = 393
pos394 = 394
pos395 = 395
pos396 = 396
pos397 = 397
pos398 = 398
pos399 = 399
pos400 = 400
pos401 = 401
pos402 = 402
pos403 = 403
pos404 = 404
pos405 = 405
pos406 = 406
pos407 = 407
pos408 = 408
pos409 = 409
pos410 = 410
pos411 = 411
pos412 = 412
pos413 = 413
pos414 = 414
pos415 = 415
pos416 = 416
pos417 = 417
pos418 = 418
pos419 = 419
pos420 = 420
pos421 = 421
pos422 = 422
pos423 = 423
pos424 = 424
pos425 = 425
pos426 = 426
pos427 = 427
pos428 = 428
pos429 = 429
pos430 = 430
pos431 = 431
pos432 = 432
pos433 = 433
pos434 = 434
pos435 = 435
pos436 = 436
pos437 = 437
pos438 = 438
pos439 = 439
pos440 = 440
pos441 = 441
pos442 = 442
pos443 = 443
pos444 = 444
pos445 = 445
pos446 = 446
pos447 = 447
pos448 = 448
pos449 = 449
pos450 = 450
pos451 = 451
pos452 = 452
pos453 = 453
pos454 = 454
pos455 = 455
pos456 = 456
pos457 = 457
pos458 = 458
pos459 = 459
pos460 = 460
pos461 = 461
pos462 = 462
pos463 = 463
pos464 = 464
pos465 = 465
pos466 = 466
pos467 = 467
pos468 = 468
pos469 = 469
pos470 = 470
pos471 = 471
pos472 = 472
pos473 = 473
pos474 = 474
pos475 = 475
pos476 = 476
pos477 = 477
pos478 = 478
pos479 = 479
pos480 = 480
pos481 = 481
pos482 = 482
pos483 = 483
pos484 = 484
pos485 = 485
pos486 = 486
pos487 = 487
pos488 = 488
pos489 = 489
pos490 = 490
pos491 = 491
pos492 = 492
pos493 = 493
pos494 = 494
pos495 = 495
pos496 = 496
pos497 = 497
pos498 = 498
pos499 = 499
pos500 = 500
pos501 = 501
pos502 = 502
pos503 = 503
pos504 = 504
pos505 = 505
pos506 = 506
pos507 = 507
pos508 = 508
pos509 = 509
pos510 = 510
pos511 = 511
pos512 = 512
pos513 = 513
pos514 = 514
pos515 = 515
pos516 = 516
pos517 = 517
pos518 = 518
pos519 = 519
pos520 = 520
pos521 = 521
pos522 = 522
pos523 = 523
pos524 = 524
pos525 = 525
pos526 = 526
pos527 = 527
pos528 = 528
pos529 = 529
pos530 = 530
pos531 = 531
pos532 = 532
pos533 = 533
pos534 = 534
pos535 = 535
pos536 = 536
pos537 = 537
pos538 = 538
pos539 = 539
pos540 = 540
pos541 = 541
pos542 = 542
pos543 = 543
pos544 = 544
pos545 = 545
pos546 = 546
pos547 = 547
pos548 = 548
pos549 = 549
pos550 = 550
pos551 = 551
pos552 = 552
pos553 = 553
pos554 = 554
pos555 = 555
pos556 = 556
pos557 = 557
pos558 = 558
pos559 = 559
pos560 = 560
pos561 = 561
pos562 = 562
pos563 = 563
pos564 = 564
pos565 = 565
pos566 = 566
pos567 = 567
pos568 = 568
pos569 = 569
pos570 = 570
pos571 = 571
pos572 = 572
pos573 = 573
pos574 = 574
pos575 = 575
pos576 = 576
pos577 = 577
pos578 = 578
pos579 = 579
pos580 = 580
pos581 = 581
pos582 = 582
pos583 = 583
pos584 = 584
pos585 = 585
pos586 = 586
pos587 = 587
pos588 = 588
pos589 = 589
pos590 = 590
pos591 = 591
pos592 = 592
pos593 = 593
pos594 = 594
pos595 = 595
pos596 = 596
pos597 = 597
pos598 = 598
pos599 = 599
pos600 = 600
pos601 = 601
pos602 = 602
pos603 = 603
pos604 = 604
pos605 = 605
pos606 = 606
pos607 = 607
pos608 = 608
pos609 = 609
pos610 = 610
pos611 = 611
pos612 = 612
pos613 = 613
pos614 = 614
pos615 = 615
pos616 = 616
pos617 = 617
pos618 = 618
pos619 = 619
pos620 = 620
pos621 = 621
pos622 = 622
pos623 = 623
pos624 = 624
pos625 = 625
pos626 = 626
pos627 = 627
pos628 = 628
pos629 = 629
pos630 = 630
pos631 = 631
pos632 = 632
pos633 = 633
pos634 = 634
pos635 = 635
pos636 = 636
pos637 = 637
pos638 = 638
pos639 = 639
pos640 = 640
pos641 = 641
pos642 = 642
pos643 = 643
pos644 = 644
pos645 = 645
pos646 = 646
pos647 = 647
pos648 = 648
pos649 = 649
pos650 = 650
pos_belfry_begin = 651

reg0   = opmask_register| 0
reg1   = opmask_register| 1
reg2   = opmask_register| 2
reg3   = opmask_register| 3
reg4   = opmask_register| 4
reg5   = opmask_register| 5
reg6   = opmask_register| 6
reg7   = opmask_register| 7
reg8   = opmask_register| 8
reg9   = opmask_register| 9
reg10  = opmask_register|10
reg11  = opmask_register|11
reg12  = opmask_register|12
reg13  = opmask_register|13
reg14  = opmask_register|14
reg15  = opmask_register|15
reg16  = opmask_register|16
reg17  = opmask_register|17
reg18  = opmask_register|18
reg19  = opmask_register|19
reg20  = opmask_register|20
reg21  = opmask_register|21
reg22  = opmask_register|22
reg23  = opmask_register|23
reg24  = opmask_register|24
reg25  = opmask_register|25
reg26  = opmask_register|26
reg27  = opmask_register|27
reg28  = opmask_register|28
reg29  = opmask_register|29
reg30  = opmask_register|30
reg31  = opmask_register|31
reg32  = opmask_register|32
reg33  = opmask_register|33
reg34  = opmask_register|34
reg35  = opmask_register|35
reg36  = opmask_register|36
reg37  = opmask_register|37
reg38  = opmask_register|38
reg39  = opmask_register|39
reg40  = opmask_register|40
reg41  = opmask_register|41
reg42  = opmask_register|42
reg43  = opmask_register|43
reg44  = opmask_register|44
reg45  = opmask_register|45
reg46  = opmask_register|46
reg47  = opmask_register|47
reg48  = opmask_register|48
reg49  = opmask_register|49
reg50  = opmask_register|50
reg51  = opmask_register|51
reg52  = opmask_register|52
reg53  = opmask_register|53
reg54  = opmask_register|54
reg55  = opmask_register|55
reg56  = opmask_register|56
reg57  = opmask_register|57
reg58  = opmask_register|58
reg59  = opmask_register|59
reg60  = opmask_register|60
reg61  = opmask_register|61
reg62  = opmask_register|62
reg63  = opmask_register|63

reg65  = opmask_register|65

spf_all_teams_are_enemy                      = 0x00000001, 
spf_is_horseman                              = 0x00000002,
spf_examine_all_spawn_points                 = 0x00000004,
spf_team_0_spawn_far_from_entry_32           = 0x00000008,
spf_team_1_spawn_far_from_entry_0            = 0x00000010,
spf_team_1_spawn_far_from_entry_66           = 0x00000020,
spf_team_0_spawn_near_entry_0                = 0x00000040,
spf_team_0_spawn_near_entry_66               = 0x00000080,
spf_team_1_spawn_near_entry_32               = 0x00000100,
spf_team_0_walkers_spawn_at_high_points      = 0x00000200,
spf_team_1_walkers_spawn_at_high_points      = 0x00000400,
spf_try_to_spawn_close_to_at_least_one_enemy = 0x00000800,
spf_care_agent_to_agent_distances_less       = 0x00001000,

#Tooltip types
tooltip_agent = 1
tooltip_horse = 2
tooltip_my_horse = 3
tooltip_container = 5
tooltip_door = 6
tooltip_item = 7
tooltip_leave_area = 8
tooltip_prop = 9
tooltip_destructible_prop = 10

#Human bones
hb_abdomen = 0
hb_thigh_l = 1
hb_calf_l = 2
hb_foot_l = 3
hb_thigh_r = 4
hb_calf_r = 5
hb_foot_r = 6
hb_spine = 7
hb_thorax = 8
hb_head = 9
hb_shoulder_l = 10
hb_upperarm_l = 11
hb_forearm_l = 12
hb_hand_l = 13
hb_item_l = 14
hb_shoulder_r = 15
hb_upperarm_r = 16
hb_forearm_r = 17
hb_hand_r = 18
hb_item_r = 19

#Horse bones
hrsb_pelvis = 0
hrsb_spine_1 = 1
hrsb_spine_2 = 2
hrsb_spine_3 = 3
hrsb_neck_1 = 4
hrsb_neck_2 = 5
hrsb_neck_3 = 6
hrsb_head = 7
hrsb_l_clavicle = 8
hrsb_l_upper_arm = 9
hrsb_l_forearm = 10
hrsb_l_hand = 11
hrsb_l_front_hoof = 12
hrsb_r_clavicle = 13
hrsb_r_upper_arm = 14
hrsb_r_forearm = 15
hrsb_r_hand = 16
hrsb_r_front_hoof = 17
hrsb_l_thigh = 18
hrsb_l_calf = 19
hrsb_l_foot = 20
hrsb_l_back_hoof = 21
hrsb_r_thigh = 22
hrsb_r_calf = 23
hrsb_r_foot = 24
hrsb_r_back_hoof = 25
hrsb_tail_1 = 26
hrsb_tail_2 = 27

#Attack directions
atk_thrust = 0
atk_right_swing = 1
atk_left_swing = 2
atk_overhead = 3

#Game windows
window_inventory = 7
window_party = 8
window_character = 11

#Agent body meta meshes
bmm_head = 0
bmm_beard = 1
bmm_hair = 2
bmm_helmet = 3
bmm_armor = 4
bmm_trousers = 5
bmm_left_foot = 6
bmm_right_foot = 7
bmm_armature = 8
bmm_item_1 = 9
bmm_item_2 = 10
bmm_item_3 = 11
bmm_item_4 = 12
bmm_missile_1 = 13
bmm_missile_2 = 14
bmm_missile_3 = 15
bmm_missile_4 = 16
bmm_carry_1 = 17
bmm_carry_2 = 18
bmm_carry_3 = 19
bmm_carry_4 = 20
bmm_unknown_2 = 21
bmm_left_hand = 22
bmm_right_hand = 23
bmm_left_bracer = 24
bmm_right_bracer = 25
bmm_banner = 26
bmm_name = 27

#Dialog states
dlg_start              = 0
dlg_party_encounter    = 1
dlg_event_triggered    = 5
dlg_close_window       = 6
dlg_member_chat        = 13
dlg_prisoner_chat      = 14

#Floating point registers
fp0 = 0
fp1 = 1
fp2 = 2
fp3 = 3
fp4 = 4
fp5 = 5
fp6 = 6
fp7 = 7
fp8 = 8
fp9 = 9
fp10 = 10
fp11 = 11
fp12 = 12
fp13 = 13
fp14 = 14
fp15 = 15
fp16 = 16
fp17 = 17
fp18 = 18
fp19 = 19
fp20 = 20
fp21 = 21
fp22 = 22
fp23 = 23
fp24 = 24
fp25 = 25
fp26 = 26
fp27 = 27
fp28 = 28
fp29 = 29
fp30 = 30
fp31 = 31
fp32 = 32
fp33 = 33
fp34 = 34
fp35 = 35
fp36 = 36
fp37 = 37
fp38 = 38
fp39 = 39
fp40 = 40
fp41 = 41
fp42 = 42
fp43 = 43
fp44 = 44
fp45 = 45
fp46 = 46
fp47 = 47
fp48 = 48
fp49 = 49
fp50 = 50
fp51 = 51
fp52 = 52
fp53 = 53
fp54 = 54
fp55 = 55
fp56 = 56
fp57 = 57
fp58 = 58
fp59 = 59
fp60 = 60
fp61 = 61
fp62 = 62
fp63 = 63
fp64 = 64
fp65 = 65
fp66 = 66
fp67 = 67
fp68 = 68
fp69 = 69
fp70 = 70
fp71 = 71
fp72 = 72
fp73 = 73
fp74 = 74
fp75 = 75
fp76 = 76
fp77 = 77
fp78 = 78
fp79 = 79
fp80 = 80
fp81 = 81
fp82 = 82
fp83 = 83
fp84 = 84
fp85 = 85
fp86 = 86
fp87 = 87
fp88 = 88
fp89 = 89
fp90 = 90
fp91 = 91
fp92 = 92
fp93 = 93
fp94 = 94
fp95 = 95
fp96 = 96
fp97 = 97
fp98 = 98
fp99 = 99
fp100 = 100
fp101 = 101
fp102 = 102
fp103 = 103
fp104 = 104
fp105 = 105
fp106 = 106
fp107 = 107
fp108 = 108
fp109 = 109
fp110 = 110
fp111 = 111
fp112 = 112
fp113 = 113
fp114 = 114
fp115 = 115
fp116 = 116
fp117 = 117
fp118 = 118
fp119 = 119
fp120 = 120
fp121 = 121
fp122 = 122
fp123 = 123
fp124 = 124
fp125 = 125
fp126 = 126
fp127 = 127

sort_f_desc = 1
sort_f_ci	= 2

sort_m_int_asc = 0
sort_m_int_desc = sort_f_desc

sort_m_str_cs_asc  = 0
sort_m_str_cs_desc = sort_f_desc
sort_m_str_ci_asc  = sort_f_ci
sort_m_str_ci_desc = sort_f_ci | sort_f_desc

LUA_TNONE			= -1
LUA_TNIL			= 0
LUA_TBOOLEAN		= 1
LUA_TLIGHTUSERDATA	= 2
LUA_TNUMBER			= 3
LUA_TSTRING			= 4
LUA_TTABLE			= 5
LUA_TFUNCTION		= 6
LUA_TUSERDATA		= 7
LUA_TTHREAD			= 8