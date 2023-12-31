# -*- coding: UTF-8 -*-
####################################################################################################################
# Generated by Warband Module Decompiler
# All rights of the module belong to their respective owners
####################################################################################################################

from header_skins import *
from ID_particle_systems import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

comp_less_than = -1;
comp_greater_than = 1;

skins = [
  (
    "man", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head",
    [
      (240, 0, -0.4, 0.3, "Chin Size"),
      (230, 0, -0.4, 0.8, "Chin Shape"),
      (250, 0, -0.25, 0.55, "Chin Forward"),
      (130, 0, -0.5, 1, "Jaw Width"),
      (120, 0, -0.5, 0.6, "Lower Lip"),
      (110, 0, -0.2, 0.6, "Upper Lip"),
      (100, 0, 0.2, -0.2, "Mouth-Nose Distance"),
      (90, 0, 0.55, -0.55, "Mouth Width"),
      (30, 0, -0.3, 0.3, "Nostril Size"),
      (60, 0, 0.25, -0.25, "Nose Height"),
      (40, 0, -0.2, 0.3, "Nose Width"),
      (70, 0, -0.3, 0.4, "Nose Size"),
      (50, 0, 0.2, -0.3, "Nose Shape"),
      (80, 0, -0.3, 0.65, "Nose Bridge"),
      (160, 0, -0.2, 0.25, "Eye Width"),
      (190, 0, -0.25, 0.15, "Eye to Eye Dist"),
      (170, 0, -0.85, 0.85, "Eye Shape"),
      (200, 0, -0.3, 0.7, "Eye Depth"),
      (180, 0, -1.5, 1.5, "Eyelids"),
      (20, 0, 0.6, -0.25, "Cheeks"),
      (260, 0, -0.6, 0.5, "Cheek Bones"),
      (220, 0, 0.8, -0.8, "Eyebrow Height"),
      (210, 0, -0.75, 0.75, "Eyebrow Shape"),
      (10, 0, -0.6, 0.5, "Temple Width"),
      (270, 0, -0.3, 1, "Face Depth"),
      (150, 0, -0.25, 0.45, "Face Ratio"),
      (140, 0, -0.4, 0.5, "Face Width"),
      (280, 0, 1, 1, "Post-Edit"),
    ],
    ["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4"],
    ["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_young_2", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
      ("manface_midage", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
      ("manface_young", 0xFFD0E0E0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_young_3", 0xFFDCEDED, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
      ("manface_7", 0xFFC0C8C8, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_midage_2", 0xFDE4C8D8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_rugged", 0xFFB0AAB5, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_african", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_asian2", 0xFFE3E8E1, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_asian1", 0xFFE3E8E1, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_asian3", 0xFFBBB6AE, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_mideast1", 0xFFAEB0A6, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_mideast2", 0xFFD0C8C1, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_mideast3", 0xFFE0E8E8, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_black1", 0xFF87655C, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_black2", 0xFF5A342D, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_black3", 0xFF634D3E, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_white1", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
      ("manface_white2", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_white3", 0xFFE0E8E8, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ],
    [(voice_die, "snd_man_die"),(voice_hit, "snd_man_hit"),(voice_grunt, "snd_man_grunt"),(voice_grunt_long, "snd_man_grunt_long"),(voice_yell, "snd_man_yell"),(voice_stun, "snd_man_stun"),(voice_victory, "snd_man_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
      [1.6, comp_greater_than, (1, 15),(1, 23)],
      [0.6, comp_less_than, (1, 15),(1, 23)],
      [1.5, comp_greater_than, (1, 25),(1, 6)],
      [0.6, comp_greater_than, (-1, 9),(1, 6)],
      [-1, comp_less_than, (-1, 9),(1, 6)],
  ]),

  (
    "woman", 1,
    "woman_body", "woman_calf_l", "f_handL",
    "female_head",
    [
      (230, 0, 0.7, -0.7, "Chin Size"),
      (220, 0, -0.6, 0.6, "Chin Shape"),
      (10, 0, -0.5, 0.5, "Chin Forward"),
      (20, 0, -0.5, 0.6, "Jaw Width"),
      (40, 0, -0.7, 0.7, "Jaw Position"),
      (90, 0, -1.2, 1.2, "Jaw Neck"),
      (50, 0, -0.8, 0.8, "Cheeks 2"),
      (210, 0, -0.5, 0.5, "Cheeks 1"),
      (100, 0, -0.8, 0.8, "Cheek Bones"),
      (270, 0, 0.8, -0.8, "Mouth-Nose Distance"),
      (30, 0, -0.6, 1, "Mouth Width"),
      (160, 0, 0.4, -0.4, "Lips Position"),
      (60, 0, -0.5, 0.5, "Nose Height"),
      (70, 0, -0.7, 0.7, "Nose Width"),
      (80, 0, 0.5, -1, "Nose Size"),
      (240, 0, -0.5, 0.5, "Nose Shape"),
      (150, 0, -0.8, 0.8, "Eye Width"),
      (110, 0, 0.5, -0.5, "Eye to Eye Dist"),
      (120, 0, -0.7, 0.8, "Eye Shape"),
      (130, 0, -1, 0.7, "Eye Position"),
      (140, 0, -1, 1, "Eyelids"),
      (170, 0, -0.7, 0.7, "Eyebrow Height"),
      (180, 0, -1, 0.7, "Eyebrow Shape"),
      (260, 0, 0.8, -0.8, "Temple Width"),
      (200, 0, 0.7, -0.7, "Face tall-short"),
      (250, 0, 0.8, -0.8, "Face up-down"),
      (190, 0, -0.6, 1, "Face Width"),
      (280, 0, 0, 0.7, "Post-Edit"),
    ],
    ["woman_hair_01", "woman_hair_02", "woman_hair_03", "woman_hair_04", "woman_hair_05", "woman_hair_06", "woman_hair_07", "woman_hair_08", "woman_hair_09", "woman_hair_10", "woman_hair_11", "woman_hair_12", "woman_hair_13", "woman_hair_14", "woman_hair_15", "woman_hair_16", "woman_hair_17", "woman_hair_18", "woman_hair_19", "woman_hair_20", "woman_hair_21", "woman_hair_22", "woman_hair_23", "woman_hair_24", "woman_hair_25", "woman_hair_26"],
    ["lucheyelashes", "lucheyelashes_mascara"],
    ["hair_blonde02", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["lucheyelashes_blonde"],
    [
      ("womanface_01", 0xFFF2F9F7, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_02", 0xFFEAF7FF, ["hair_blonde02"], [0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_03", 0xFFE4EDED, ["hair_blonde02"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_04", 0xFFD5D3B8, ["hair_blonde02"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
      ("womanface_05", 0xFF7E7C85, ["hair_blonde02"], [0xff120808, 0xff007080c]),
      ("womanface_06", 0xFFEAF0F5, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_07", 0xFFF4FFFF, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_08", 0xFFE7E7D1, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_09", 0xFFF6F7F5, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_10", 0xFFF6FFFF, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_11", 0xFFEDFDFF, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_12", 0xFFEAF7FF, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_13", 0xFFE1E9F0, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_14", 0xFFEAF7FF, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_15", 0xFFEAF7FF, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_16", 0xFFF9FAFF, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_17", 0xFFFBFFFF, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_18", 0xFFF3FBFF, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
    ],
    [(voice_die, "snd_woman_die"),(voice_hit, "snd_woman_hit"),(voice_yell, "snd_woman_yell")],
    "skel_human_female", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
  ]),

]