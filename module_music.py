# -*- coding: UTF-8 -*-
####################################################################################################################
# Generated by Warband Module Decompiler
# All rights of the module belong to their respective owners
####################################################################################################################

from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
  ("cant_find_this", "cant_find_this.ogg", 0, 0),
  ("mount_and_blade_title_screen", "mount_and_blade_title_screen.ogg", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 0),
  ("capture", "capture.ogg", mtf_module_track, 0),
  ("empty_village", "empty_village.ogg", mtf_persist_until_finished|mtf_module_track, 0),
  ("escape", "escape.ogg", mtf_persist_until_finished|mtf_module_track, 0),
  ("retreat", "retreat.ogg", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
  ("euro_1", "euro_1.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_2", "euro_2.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_3", "euro_3.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_4", "euro_4.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_5", "euro_5.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_6", "euro_6.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_7", "euro_7.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_8", "euro_8.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_9", "euro_9.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_10", "euro_10.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_11", "euro_11.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_12", "euro_12.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("euro_13", "euro_13.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, 0),
  ("baltic_1", "baltic_1.ogg", mtf_culture_2|mtf_sit_travel|mtf_module_track, 0),
  ("baltic_2", "baltic_2.ogg", mtf_culture_2|mtf_sit_travel|mtf_module_track, 0),
  ("baltic_3", "baltic_3.ogg", mtf_culture_2|mtf_sit_travel|mtf_module_track, 0),
  ("baltic_4", "baltic_4.ogg", mtf_culture_2|mtf_sit_travel|mtf_module_track, 0),
  ("baltic_5", "baltic_5.ogg", mtf_culture_2|mtf_sit_travel|mtf_module_track, 0),
  ("rus_1", "rus_1.ogg", mtf_culture_5|mtf_sit_travel|mtf_module_track, 0),
  ("rus_2", "rus_2.ogg", mtf_culture_5|mtf_sit_travel|mtf_module_track, 0),
  ("rus_3", "rus_3.ogg", mtf_culture_5|mtf_sit_travel|mtf_module_track, 0),
  ("rus_4", "rus_4.ogg", mtf_culture_5|mtf_sit_travel|mtf_module_track, 0),
  ("saracen_1", "saracen_1.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, 0),
  ("saracen_2", "saracen_2.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, 0),
  ("saracen_3", "saracen_3.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, 0),
  ("saracen_4", "saracen_4.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, 0),
  ("saracen_5", "saracen_5.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, 0),
  ("saracen_6", "saracen_6.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, 0),
  ("saracen_7", "saracen_7.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, 0),
  ("mong_1", "mong_1.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, 0),
  ("mong_2", "mong_2.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, 0),
  ("mong_3", "mong_3.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, 0),
  ("mong_4", "mong_4.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, 0),
  ("mong_5", "mong_5.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, 0),
  ("mong_6", "mong_6.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, 0),
  ("mong_7", "mong_7.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, 0),
  ("mong_8", "mong_8.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, 0),
  ("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished|mtf_module_track, 0),
  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),
  ("coronation", "coronation.ogg", mtf_persist_until_finished, 0),
  ("ambient_1", "ambient_1.ogg", mtf_culture_all|mtf_module_track, 0),
  ("ambient_2", "ambient_2.ogg", mtf_culture_all|mtf_module_track, 0),
  ("ambient_3", "ambient_3.ogg", mtf_culture_all|mtf_module_track, 0),
  ("ambient_4", "ambient_4.ogg", mtf_culture_all|mtf_module_track, 0),
  ("ambient_5", "ambient_5.ogg", mtf_culture_all|mtf_module_track, 0),
  ("ambient_6", "ambient_6.ogg", mtf_culture_all|mtf_module_track, 0),
  ("ambient_7", "ambient_7.ogg", mtf_culture_all|mtf_module_track, 0),
  ("ambient_8", "ambient_8.ogg", mtf_culture_all|mtf_module_track, 0),
  ("ambient_9", "ambient_9.ogg", mtf_culture_all|mtf_module_track, 0),
  ("ambient_10", "ambient_10.ogg", mtf_module_track, 0),
  ("silence", "silence.ogg", mtf_module_track, 0),
  ("Arabic_Battle_1_Crack_your_head_with_a_Tabla", "Arabic_Battle_1_Crack_your_head_with_a_Tabla.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("Crusades_Battle_Valley_Of_Death", "Crusades_Battle_Valley_Of_Death.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("Euro_Battle_1_Duke_of_Death", "Euro_Battle_1_Duke_of_Death.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, 0),
  ("Teutonic_Battle_Darker_Skies_Ahead", "Teutonic_Battle_Darker_Skies_Ahead.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("06_melee_cafe", "06_melee_cafe.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("12_mayhem", "12_mayhem.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("13_imperial_conflict", "13_imperial_conflict.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("16_the_enemy_is_near", "16_the_enemy_is_near.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("17_warrior_march", "17_warrior_march.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("30_soldiers_chant", "30_soldiers_chant.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("31_mobilize", "31_mobilize.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("new_battle_3", "new_battle_3.ogg", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("new_battle_4", "new_battle_4.ogg", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("new_battle_5", "new_battle_5.ogg", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, 0),
  ("new_battle_6", "new_battle_6.ogg", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("siege_4", "siege_4.mp3", mtf_sit_siege|mtf_module_track, 0),
  ("10_time_2_kill", "10_time_2_kill.mp3", mtf_culture_all|mtf_sit_ambushed|mtf_sit_encounter_hostile|mtf_module_track, 0),
  ("Medieval_II_total_war_Time_And_Again", "Medieval_II_total_war_Time_And_Again.mp3", mtf_culture_all|mtf_sit_travel|mtf_module_track, 0),
  ("Euro_Mobilize_4_New_Arc_Ascending", "Euro_Mobilize_4_New_Arc_Ascending.mp3", mtf_culture_all|mtf_sit_travel|mtf_module_track, 0),
]