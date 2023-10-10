# -*- coding: UTF-8 -*-
####################################################################################################################
# Generated by Warband Module Decompiler
# All rights of the module belong to their respective owners
####################################################################################################################

from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction", "No_Faction", 0, 0.0, [("no_faction", 0.9)], []),
  ("commoners", "Commoners", 0, 0.0, [("commoners", 0.1),("outlaws", -0.6),("player_faction", 0.1),("mountain_bandits", -0.2),("forest_bandits", -0.2),("undeads", -0.7)], [], 0xFFFFFF),
  ("outlaws", "Outlaws", max_player_rating(-30), 0.0, [("commoners", -0.6),("outlaws", 0.5),("innocents", -0.05),("merchants", -0.5),("player_faction", -0.15),("player_supporters_faction", -0.05),("kingdom_1", -0.05),("kingdom_2", -0.05),("kingdom_3", -0.05),("kingdom_4", -0.05),("kingdom_5", -0.05),("kingdom_6", -0.05),("kingdom_7", -0.05),("kingdom_8", -0.05),("kingdom_9", -0.05),("kingdom_10", -0.05),("kingdom_11", -0.05),("kingdom_12", -0.05),("kingdom_13", -0.05),("kingdom_14", -0.05),("kingdom_15", -0.05),("kingdom_16", -0.05),("kingdom_17", -0.05),("kingdom_18", -0.05),("kingdom_19", -0.05),("kingdom_20", -0.05),("papacy", -0.05),("kingdom_22", -0.05),("kingdom_23", -0.05),("kingdom_24", -0.05),("kingdom_25", -0.05),("kingdom_26", -0.05),("kingdom_27", -0.05),("kingdom_28", -0.05),("kingdom_29", -0.05),("kingdom_30", -0.05),("kingdom_31", -0.05),("kingdom_32", -0.05),("kingdom_33", -0.05),("kingdom_34", -0.05),("kingdom_35", -0.05),("kingdom_36", -0.05),("kingdom_37", -0.05),("kingdom_38", -0.05),("kingdom_39", -0.05),("kingdom_40", -0.05),("kingdom_41", -0.05),("kingdom_42", -0.05),("manhunters", -0.6),("peasant_rebels", -0.1),("crusade", -0.05),("escaped_prisoners_faction", -0.2)], [], 0xFF00FF),
  ("neutral", "Neutral_Parties", 0, 0.0, [("neutral", 0.1)], [], 0xFFFFFF),
  ("innocents", "Innocents", ff_always_hide_label, 0.0, [("outlaws", -0.05),("innocents", 0.5)], [], 0xFFFFFF),
  ("merchants", "Merchants", ff_always_hide_label, 0.0, [("outlaws", -0.5),("merchants", 0.5),("deserters", -0.5),("mountain_bandits", -0.5),("forest_bandits", -0.5)], [], 0xFFFFFF),
  ("culture_finnish", "Finnish", 0, 0.0, [("culture_finnish", 0.9)], []),
  ("culture_mazovian", "Mazovian", 0, 0.0, [("culture_mazovian", 0.9)], []),
  ("culture_serbian", "Serbian", 0, 0.0, [("culture_serbian", 0.9)], []),
  ("culture_welsh", "Welsh", 0, 0.0, [("culture_welsh", 0.9)], []),
  ("culture_teutonic", "Teutonic", 0, 0.0, [("culture_teutonic", 0.9)], []),
  ("culture_balkan", "Balkan", 0, 0.0, [("culture_balkan", 0.9)], []),
  ("culture_rus", "Rus", 0, 0.0, [("culture_rus", 0.9)], []),
  ("culture_nordic", "Nordic", 0, 0.0, [("culture_nordic", 0.9)], []),
  ("culture_baltic", "Baltic", 0, 0.0, [("culture_baltic", 0.9)], []),
  ("culture_marinid", "Marinid", 0, 0.0, [("culture_marinid", 0.9)], []),
  ("culture_mamluke", "Mamluke", 0, 0.0, [("culture_mamluke", 0.9)], []),
  ("culture_byzantium", "Byzantium", 0, 0.0, [("culture_byzantium", 0.9)], []),
  ("culture_iberian", "Iberian", 0, 0.0, [("culture_iberian", 0.9)], []),
  ("culture_italian", "Italian", 0, 0.0, [("culture_italian", 0.9)], []),
  ("culture_andalus", "Andalus", 0, 0.0, [("culture_andalus", 0.9)], []),
  ("culture_gaelic", "Gaelic", 0, 0.0, [("culture_gaelic", 0.9)], []),
  ("culture_anatolian_christian", "Armenia", 0, 0.0, [("culture_anatolian_christian", 0.9)], []),
  ("culture_anatolian", "Anatolia", 0, 0.0, [("culture_anatolian", 0.9)], []),
  ("culture_scotish", "Scottish", 0, 0.0, [("culture_scotish", 0.9)], []),
  ("culture_western", "Western_Europe", 0, 0.0, [("culture_western", 0.9)], []),
  ("culture_mongol", "Mongol", 0, 0.0, [("culture_mongol", 0.9)], []),
  ("culture_templar", "Templar", 0, 0.0, [("culture_templar", 0.9)], []),
  ("culture_hospitaller", "Hospitaller", 0, 0.0, [("culture_hospitaller", 0.9)], []),
  ("culture_antioch", "Antioch", 0, 0.0, [("culture_antioch", 0.9)], []),
  ("culture_tripoli", "Tripoli", 0, 0.0, [("culture_tripoli", 0.9)], []),
  ("culture_ibelin", "Ibelin", 0, 0.0, [("culture_ibelin", 0.9)], []),
  ("culture_jerusalem", "Jerusalem", 0, 0.0, [("culture_jerusalem", 0.9)], []),
  ("culture_crusader", "Crusader", 0, 0.0, [("culture_crusader", 0.9)], []),
  ("culture_cuman", "Cuman", 0, 0.0, [("culture_cuman", 0.9)], []),
  ("culture_english", "English", 0, 0.0, [("culture_english", 0.9)], []),
  ("culture_french", "French", 0, 0.0, [("culture_french", 0.9)], []),
  ("culture_hungarian", "Hungarian", 0, 0.0, [("culture_hungarian", 0.9)], []),
  ("culture_polish", "Polish", 0, 0.0, [("culture_polish", 0.9)], []),
  ("culture_player", "Custom", 0, 0.0, [("culture_player", 0.9)], []),
  ("player_faction", "Player", 0, 0.0, [("commoners", 0.1),("outlaws", -0.15),("player_faction", 0.9),("player_supporters_faction", 1),("manhunters", 0.1),("deserters", -0.1),("mountain_bandits", -0.15),("forest_bandits", -0.15),("undeads", -0.5),("escaped_prisoners_faction", -0.2)], [], 0xFFFF),
  ("player_supporters_faction", "Player's_Kingdom", 0, 0.0, [("outlaws", -0.05),("player_faction", 1),("player_supporters_faction", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xFFFF),
  ("kingdom_1", "Ordo_Teutonicus", 0, 0.0, [("outlaws", -0.05),("kingdom_1", 0.9),("kingdom_4", 0.1),("kingdom_6", 0.5),("kingdom_8", -0.2),("kingdom_14", 0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xE9E9E9),
  ("kingdom_2", "Regnum_Litus", 0, 0.0, [("outlaws", -0.05),("kingdom_2", 0.9),("kingdom_3", 0.1),("kingdom_33", 0.5),("kingdom_34", 0.5),("kingdom_35", 0.5),("kingdom_36", 0.5),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0xBADEB2),
  ("kingdom_3", "Altan_Ordyn_Uls", 0, 0.0, [("outlaws", -0.05),("kingdom_2", 0.1),("kingdom_3", 0.9),("kingdom_5", -1),("kingdom_7", -1),("kingdom_8", 0.2),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0xA33E32),
  ("kingdom_4", "Regnum_Daniae", 0, 0.0, [("outlaws", -0.05),("kingdom_1", 0.1),("kingdom_4", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x9B1A1A),
  ("kingdom_5", "Regnum_Poloniae", 0, 0.0, [("outlaws", -0.05),("kingdom_3", -1),("kingdom_5", 0.9),("kingdom_7", 0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xFF0000),
  ("kingdom_6", "Sacrum_Imperium_Romanum", 0, 0.0, [("outlaws", -0.05),("kingdom_1", 0.5),("kingdom_6", 0.9),("kingdom_38", 0.5),("kingdom_41", 1),("kingdom_42", 1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xFFCC00),
  ("kingdom_7", "Regnum_Hungariae", 0, 0.0, [("outlaws", -0.05),("kingdom_3", -1),("kingdom_5", 0.1),("kingdom_7", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x289327),
  ("kingdom_8", "Novgorod_Weliki", 0, 0.0, [("outlaws", -0.05),("kingdom_1", -0.2),("kingdom_3", 0.2),("kingdom_8", 0.9),("kingdom_14", -0.2),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x9E0B6F),
  ("kingdom_9", "Regnum_Angliae", 0, 0.0, [("outlaws", -0.05),("kingdom_9", 0.9),("kingdom_37", -1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x931124),
  ("kingdom_10", "Regnum_Franciae", 0, 0.0, [("outlaws", -0.05),("kingdom_10", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x6DE2),
  ("kingdom_11", "Kongeriket_Norge", 0, 0.0, [("outlaws", -0.05),("kingdom_11", 0.9),("kingdom_12", -0.2),("kingdom_13", -0.2),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x6669D6),
  ("kingdom_12", "Regnum_Scotiae", 0, 0.0, [("outlaws", -0.05),("kingdom_11", -0.2),("kingdom_12", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x22D8A7),
  ("kingdom_13", "Scotia_Maior", 0, 0.0, [("outlaws", -0.05),("kingdom_11", -0.2),("kingdom_13", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x77B322),
  ("kingdom_14", "Konungariket_Sverige", 0, 0.0, [("outlaws", -0.05),("kingdom_1", 0.1),("kingdom_8", -0.2),("kingdom_14", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x3254B5),
  ("kingdom_15", "Regnum_Galiciae_et_Lodomeriae", 0, 0.0, [("outlaws", -0.05),("kingdom_15", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xECE874),
  ("kingdom_16", "Regnum_Portugaliae", 0, 0.0, [("outlaws", -0.05),("kingdom_16", 0.9),("kingdom_20", -40),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x27837A),
  ("kingdom_17", "Corona_Aragonae", 0, 0.0, [("outlaws", -0.05),("kingdom_17", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x7B233),
  ("kingdom_18", "Corona_Castiliae", 0, 0.0, [("outlaws", -0.05),("kingdom_18", 0.9),("kingdom_20", -40),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xD85AC4),
  ("kingdom_19", "Regnum_Navarrae", 0, 0.0, [("outlaws", -0.05),("kingdom_19", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xF7F497),
  ("kingdom_20", "Imarat_al_Nasri", 0, 0.0, [("outlaws", -0.05),("kingdom_16", -40),("kingdom_18", -40),("kingdom_20", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0xABC904),
  ("papacy", "Patrimonium_Sancti_Petri", 0, 0.0, [("outlaws", -0.05),("papacy", 0.9),("kingdom_40", 1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0xFFF17A),
  ("kingdom_22", "Basileia_ton_Rhomaion", 0, 0.0, [("outlaws", -0.05),("kingdom_22", 0.9),("kingdom_26", -1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x760D0D),
  ("kingdom_23", "Regnum_Hierosolymitanum", 0, 0.0, [("outlaws", -0.05),("kingdom_23", 0.9),("kingdom_25", -1),("kingdom_27", 0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xF3EFB8),
  ("kingdom_24", "Regnum_Siciliae", 0, 0.0, [("outlaws", -0.05),("kingdom_24", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x799CB5),
  ("kingdom_25", "Sultanat_al_Mamalik", 0, 0.0, [("outlaws", -0.05),("kingdom_23", -1),("kingdom_25", 0.9),("kingdom_27", -1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0xEBE800),
  ("kingdom_26", "Imperium_Romaniae", 0, 0.0, [("outlaws", -0.05),("kingdom_22", -1),("kingdom_26", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xB26248),
  ("kingdom_27", "Ilkhanate", 0, 0.0, [("outlaws", -0.05),("kingdom_23", 0.1),("kingdom_25", -1),("kingdom_27", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0xE19004),
  ("kingdom_28", "Sultanat_al_Hafsi", 0, 0.0, [("outlaws", -0.05),("kingdom_28", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0xA48460),
  ("kingdom_29", "Kraljevstvo_Srbsko", 0, 0.0, [("outlaws", -0.05),("kingdom_29", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xB38263),
  ("kingdom_30", "Balgarsko_Tsarstvo", 0, 0.0, [("outlaws", -0.05),("kingdom_30", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x76A296),
  ("kingdom_31", "Sultanat_al_Marini", 0, 0.0, [("outlaws", -0.05),("kingdom_31", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0xC1272D),
  ("kingdom_32", "Repubblica_di_Venezia", 0, 0.0, [("outlaws", -0.05),("kingdom_32", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xC1172D),
  ("kingdom_33", "Jotvingiai", 0, 0.0, [("outlaws", -0.05),("kingdom_2", 0.5),("kingdom_33", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0x3E7583),
  ("kingdom_34", "Pruteni", 0, 0.0, [("outlaws", -0.05),("kingdom_2", 0.5),("kingdom_34", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0x65C0D7),
  ("kingdom_35", "Kursi", 0, 0.0, [("outlaws", -0.05),("kingdom_2", 0.5),("kingdom_35", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0x3E7583),
  ("kingdom_36", "Zemaiciai", 0, 0.0, [("outlaws", -0.05),("kingdom_2", 0.5),("kingdom_36", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0x529CAE),
  ("kingdom_37", "Cymry", 0, 0.0, [("outlaws", -0.05),("kingdom_9", -1),("kingdom_37", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xDC00),
  ("kingdom_38", "Respublica_Ianuensis", 0, 0.0, [("outlaws", -0.05),("kingdom_6", 0.5),("kingdom_38", 0.9),("kingdom_39", -0.5),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", -0.5)], [], 0xE1900A),
  ("kingdom_39", "Respublica_Pisarum", 0, 0.0, [("outlaws", -0.05),("kingdom_38", -0.5),("kingdom_39", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xEBE800),
  ("kingdom_40", "Comuni_Guelfi", 0, 0.0, [("outlaws", -0.05),("papacy", 1),("kingdom_40", 0.9),("kingdom_41", -0.8),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x3254E5),
  ("kingdom_41", "Comuni_Ghibellini", 0, 0.0, [("outlaws", -0.05),("kingdom_6", 1),("kingdom_40", -0.8),("kingdom_41", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0x9E026A),
  ("kingdom_42", "České_Království", 0, 0.0, [("outlaws", -0.05),("kingdom_6", 1),("kingdom_42", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1)], [], 0xE8E8E8),
  ("enhanced_kingdom_1", "Random_Faction", 0, 0.0, [("enhanced_kingdom_1", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_2", "Random_Faction", 0, 0.0, [("enhanced_kingdom_2", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_3", "Random_Faction", 0, 0.0, [("enhanced_kingdom_3", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_4", "Random_Faction", 0, 0.0, [("enhanced_kingdom_4", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_5", "Random_Faction", 0, 0.0, [("enhanced_kingdom_5", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_6", "Random_Faction", 0, 0.0, [("enhanced_kingdom_6", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_7", "Random_Faction", 0, 0.0, [("enhanced_kingdom_7", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_8", "Random_Faction", 0, 0.0, [("enhanced_kingdom_8", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_9", "Random_Faction", 0, 0.0, [("enhanced_kingdom_9", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_10", "Random_Faction", 0, 0.0, [("enhanced_kingdom_10", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_11", "Random_Faction", 0, 0.0, [("enhanced_kingdom_11", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_12", "Random_Faction", 0, 0.0, [("enhanced_kingdom_12", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_13", "Random_Faction", 0, 0.0, [("enhanced_kingdom_13", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_14", "Random_Faction", 0, 0.0, [("enhanced_kingdom_14", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_15", "Random_Faction", 0, 0.0, [("enhanced_kingdom_15", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_16", "Random_Faction", 0, 0.0, [("enhanced_kingdom_16", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_17", "Random_Faction", 0, 0.0, [("enhanced_kingdom_17", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_18", "Random_Faction", 0, 0.0, [("enhanced_kingdom_18", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_19", "Random_Faction", 0, 0.0, [("enhanced_kingdom_19", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_20", "Random_Faction", 0, 0.0, [("enhanced_kingdom_20", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_21", "Random_Faction", 0, 0.0, [("enhanced_kingdom_21", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_22", "Random_Faction", 0, 0.0, [("enhanced_kingdom_22", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_23", "Random_Faction", 0, 0.0, [("enhanced_kingdom_23", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_24", "Random_Faction", 0, 0.0, [("enhanced_kingdom_24", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_25", "Random_Faction", 0, 0.0, [("enhanced_kingdom_25", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_26", "Random_Faction", 0, 0.0, [("enhanced_kingdom_26", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_27", "Random_Faction", 0, 0.0, [("enhanced_kingdom_27", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_28", "Random_Faction", 0, 0.0, [("enhanced_kingdom_28", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_29", "Random_Faction", 0, 0.0, [("enhanced_kingdom_29", 0.9)], [], 0xE8E8E8),
  ("enhanced_kingdom_30", "Random_Faction", 0, 0.0, [("enhanced_kingdom_30", 0.9)], [], 0xE8E8E8),
  ("kingdoms_end", "{!}kingdoms_end", 0, 0.0, [], []),
  ("robber_knights", "{!}robber_knights", 0, 0.0, [("robber_knights", 0.1)], []),
  ("manhunters", "Manhunters", 0, 0.0, [("outlaws", -0.6),("player_faction", 0.1),("manhunters", 0.5),("deserters", -0.6),("mountain_bandits", -0.6),("forest_bandits", -0.6)], [], 0xFFFFFF),
  ("deserters", "Deserters", 0, 0.0, [("merchants", -0.5),("player_faction", -0.1),("player_supporters_faction", -0.02),("kingdom_1", -0.02),("kingdom_2", -0.02),("kingdom_3", -0.02),("kingdom_4", -0.02),("kingdom_5", -0.02),("kingdom_6", -0.02),("kingdom_7", -0.02),("kingdom_8", -0.02),("kingdom_9", -0.02),("kingdom_10", -0.02),("kingdom_11", -0.02),("kingdom_12", -0.02),("kingdom_13", -0.02),("kingdom_14", -0.02),("kingdom_15", -0.02),("kingdom_16", -0.02),("kingdom_17", -0.02),("kingdom_18", -0.02),("kingdom_19", -0.02),("kingdom_20", -0.02),("papacy", -0.02),("kingdom_22", -0.02),("kingdom_23", -0.02),("kingdom_24", -0.02),("kingdom_25", -0.02),("kingdom_26", -0.02),("kingdom_27", -0.02),("kingdom_28", -0.02),("kingdom_29", -0.02),("kingdom_30", -0.02),("kingdom_31", -0.02),("kingdom_32", -0.02),("kingdom_33", -0.02),("kingdom_34", -0.02),("kingdom_35", -0.02),("kingdom_36", -0.02),("kingdom_37", -0.02),("kingdom_38", -0.02),("kingdom_39", -0.02),("kingdom_40", -0.02),("kingdom_41", -0.02),("kingdom_42", -0.02),("manhunters", -0.6),("deserters", 0.5),("peasant_rebels", -0.05),("crusade", -0.02),("escaped_prisoners_faction", -0.1)], [], 0xFF00FF),
  ("mountain_bandits", "Allied_Factions", 0, 0.0, [("commoners", -0.2),("merchants", -0.5),("player_faction", -0.15),("player_supporters_faction", -0.05),("kingdom_1", -0.05),("kingdom_2", -0.05),("kingdom_3", -0.05),("kingdom_4", -0.05),("kingdom_5", -0.05),("kingdom_6", -0.05),("kingdom_7", -0.05),("kingdom_8", -0.05),("kingdom_9", -0.05),("kingdom_10", -0.05),("kingdom_11", -0.05),("kingdom_12", -0.05),("kingdom_13", -0.05),("kingdom_14", -0.05),("kingdom_15", -0.05),("kingdom_16", -0.05),("kingdom_17", -0.05),("kingdom_18", -0.05),("kingdom_19", -0.05),("kingdom_20", -0.05),("papacy", -0.05),("kingdom_22", -0.05),("kingdom_23", -0.05),("kingdom_24", -0.05),("kingdom_25", -0.05),("kingdom_26", -0.05),("kingdom_27", -0.05),("kingdom_28", -0.05),("kingdom_29", -0.05),("kingdom_30", -0.05),("kingdom_31", -0.05),("kingdom_32", -0.05),("kingdom_33", -0.05),("kingdom_34", -0.05),("kingdom_35", -0.05),("kingdom_36", -0.05),("kingdom_37", -0.05),("kingdom_38", -0.05),("kingdom_39", -0.05),("kingdom_40", -0.05),("kingdom_41", -0.05),("kingdom_42", -0.05),("manhunters", -0.6),("mountain_bandits", 0.5),("peasant_rebels", -0.1),("crusade", -0.05),("escaped_prisoners_faction", -0.2)], [], 0x6DE2),
  ("forest_bandits", "Friendly_Factions", 0, 0.0, [("commoners", -0.2),("merchants", -0.5),("player_faction", -0.15),("player_supporters_faction", -0.05),("kingdom_1", -0.05),("kingdom_2", -0.05),("kingdom_3", -0.05),("kingdom_4", -0.05),("kingdom_5", -0.05),("kingdom_6", -0.05),("kingdom_7", -0.05),("kingdom_8", -0.05),("kingdom_9", -0.05),("kingdom_10", -0.05),("kingdom_11", -0.05),("kingdom_12", -0.05),("kingdom_13", -0.05),("kingdom_14", -0.05),("kingdom_15", -0.05),("kingdom_16", -0.05),("kingdom_17", -0.05),("kingdom_18", -0.05),("kingdom_19", -0.05),("kingdom_20", -0.05),("papacy", -0.05),("kingdom_22", -0.05),("kingdom_23", -0.05),("kingdom_24", -0.05),("kingdom_25", -0.05),("kingdom_26", -0.05),("kingdom_27", -0.05),("kingdom_28", -0.05),("kingdom_29", -0.05),("kingdom_30", -0.05),("kingdom_31", -0.05),("kingdom_32", -0.05),("kingdom_33", -0.05),("kingdom_34", -0.05),("kingdom_35", -0.05),("kingdom_36", -0.05),("kingdom_37", -0.05),("kingdom_38", -0.05),("kingdom_39", -0.05),("kingdom_40", -0.05),("kingdom_41", -0.05),("kingdom_42", -0.05),("manhunters", -0.6),("forest_bandits", 0.5),("peasant_rebels", -0.1),("crusade", -0.05),("escaped_prisoners_faction", -0.2)], [], 0xFF00),
  ("undeads", "Enemy_Factions", max_player_rating(-30), 0.0, [("commoners", -0.7),("player_faction", -0.5),("undeads", 0.5)], [], 0xFF0000),
  ("peasant_rebels", "Peasant_Rebels", 0, 0.0, [("outlaws", -0.1),("player_supporters_faction", -0.1),("kingdom_1", -0.1),("kingdom_2", -0.1),("kingdom_3", -0.1),("kingdom_4", -0.1),("kingdom_5", -0.1),("kingdom_6", -0.1),("kingdom_7", -0.1),("kingdom_8", -0.1),("kingdom_9", -0.1),("kingdom_10", -0.1),("kingdom_11", -0.1),("kingdom_12", -0.1),("kingdom_13", -0.1),("kingdom_14", -0.1),("kingdom_15", -0.1),("kingdom_16", -0.1),("kingdom_17", -0.1),("kingdom_18", -0.1),("kingdom_19", -0.1),("kingdom_20", -0.1),("papacy", -0.1),("kingdom_22", -0.1),("kingdom_23", -0.1),("kingdom_24", -0.1),("kingdom_25", -0.1),("kingdom_26", -0.1),("kingdom_27", -0.1),("kingdom_28", -0.1),("kingdom_29", -0.1),("kingdom_30", -0.1),("kingdom_31", -0.1),("kingdom_32", -0.1),("kingdom_33", -0.1),("kingdom_34", -0.1),("kingdom_35", -0.1),("kingdom_36", -0.1),("kingdom_37", -0.1),("kingdom_38", -0.1),("kingdom_39", -0.1),("kingdom_40", -0.1),("kingdom_41", -0.1),("kingdom_42", -0.1),("deserters", -0.05),("mountain_bandits", -0.1),("forest_bandits", -0.1),("peasant_rebels", 1),("crusade", -0.1),("escaped_prisoners_faction", -0.1)], [], 0xFF00FF),
  ("crusade", "Crusaders", 0, 0.0, [("outlaws", -0.05),("kingdom_2", -0.5),("kingdom_3", -0.5),("kingdom_20", -0.5),("papacy", -0.5),("kingdom_25", -0.5),("kingdom_27", -0.5),("kingdom_28", -0.5),("kingdom_31", -0.5),("kingdom_33", -0.5),("kingdom_34", -0.5),("kingdom_35", -0.5),("kingdom_36", -0.5),("kingdom_38", -0.5),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("peasant_rebels", -0.1),("crusade", 0.9)], [], 0xE5E5E5),
  ("escaped_prisoners_faction", "Escaped_Prisoners", 0, 0.0, [("outlaws", -0.2),("player_faction", -0.2),("deserters", -0.1),("mountain_bandits", -0.2),("forest_bandits", -0.2),("peasant_rebels", -0.1),("escaped_prisoners_faction", 1)], [], 0xFFFF),
  ("end_minor_faction", "Village_Idiots", 0, 0.0, [("end_minor_faction", 0.9)], [], 0xFFF17A),
  ("culture_player2", "{!}culture_player2", 0, 0.0, [("culture_player2", 0.9)], []),
]