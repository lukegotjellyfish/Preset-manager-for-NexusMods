# -*- coding: utf-8 -*-
import re
import os
import html
import tkinter as tk
from tkinter import filedialog


categoryDictionary = {
	"22": "Buildings",
	"24": "Gameplay Effects and Changes",
	"25": "Guilds/Factions",
	"26": "Body, Face, and Hair",
	"27": "Items and Objects - Player",
	"28": "Miscellaneous",
	"29": "Models and Textures",
	"30": "New Lands",
	"33": "NPC",
	"34": "Races, Classes, and Birthsigns",
	"35": "Quests and Adventures",
	"36": "Weapons and Armour",
	"39": "Utilities",
	"40": "Cheats and God items",
	"42": "User Interface",
	"43": "Save Games",
	"45": "Videos and Trailers",
	"51": "Animation",
	"53": "Cities, Towns, Villages, and Hamlets",
	"54": "Armour",
	"55": "Weapons",
	"58": "Landscape Changes",
	"60": "Clothing",
	"61": "Audio - Music",
	"62": "Visuals and Graphics",
	"65": "Followers & Companions - Creatures",
	"67": "Player homes",
	"68": "Castles, Palaces, Mansions, and Estates",
	"69": "Mercantiles (shops, stores, inns, taverns, etc)",
	"70": "Forts, Ruins, and Abandoned Structures",
	"73": "Skills and Leveling",
	"74": "Environmental",
	"75": "Magic - Spells & Enchantments",
	"76": "Stealth",
	"77": "Combat",
	"78": "Immersion",
	"79": "Overhauls",
	"82": "Modders Resources and Tutorials",
	"83": "Creatures",
	"84": "Patches",
	"85": "Items and Objects - World",
	"88": "Dungeons - New",
	"89": "Locations - New",
	"90": "Locations - Vanilla",
	"91": "Dungeons - Vanilla",
	"92": "Collectables, Treasure Hunts, and Puzzles",
	"93": "Magic - Gameplay",
	"94": "Alchemy",
	"95": "Bug Fixes",
	"96": "Followers & Companions",
	"97": "Presets - ENB",
	"98": "Books and Scrolls",
	"99": "NPC - Children",
	"100": "Crafting",
	"101": "Mounts",
	"102": "Clothing - Jewelry",
	"103": "Armour - Shields",
	"104": "Shouts",
	"105": "Presets - ReShade",
	"106": "Audio - SFX",
	"107": "Audio - Voice",
	"108": "VR",
	"109": "Character Presets"
}

def trimList(x,type):
	x[0] = x[0].replace('        "name": "',"")[:-3]
	x[1] = x[1].replace('        "version": "',"")[:-3]
	x[2] = x[2].replace('        "category": ',"")[:-2]
	x[3] = html.unescape(x[3].replace('        "shortDescription": ',"")[:-2])
	x[3] = re.sub("(\[[^\]]*\])","",x[3])
	x[4] = x[4].replace('        "modId": ',"")[:-2]
	x[5] = x[5].replace('        "fileId": ',"")[:-2]
	x[6] = x[6].replace('        "fileName": "',"")[:-3]
	x[7] = x[7].replace('        "author": "',"")[:-3]
	if type == 1:  #No endorsed section
		x[8] = x[8].replace('        "game": "',"")[:-2]
	if type == 2:  #Has endorsed section
		x[8] = x[8].replace('        "game": "',"")[:-3]
		x[9] = x[9].replace('        "endorsed": "',"")[:-2]
	return x



while True:
	modList = []
	root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Preset to Inherit", filetypes=[("Modlist Export File", "*.*")])
	with open(file_path, "r", encoding='utf-8') as modfile:
		lines = modfile.readlines()
		modList = []

		i = 0
		startMod = 0
		endMod = 0
		for line in lines:
			if (line == "    {\n"):
				startMod = i + 1
			elif ((line == "    },\n") or (line == "    }\n")):
				endMod = i

				if (lines[endMod-1][9] == 'g'):
					tempList = lines[startMod:endMod]
					tempList = trimList(tempList,1)
					tempList.append("Undecided")
					modList.append(tempList)
				else:
					modList.append(trimList(lines[startMod:endMod],2))
			i += 1

		with open("modFile.csv", "w") as f:
			for mods in modList:
				for item in mods:
					f.write(item + ",")
				f.write("\n")

	input("Press ENTER to restart.")



#https://www.nexusmods.com/skyrimspecialedition/mods/  MOD_ID ?tab=files&file_id= FILE_ID &nmm=1



# Vortex Mod Atributes:
# mod.attributes.modName,
# mod.attributes.version,
# mod.attributes.category,
# mod.attributes.size,
# mod.attributes.modId,
# mod.attributes.fileId,
# mod.attributes.fileName,
# mod.attributes.author,
# mod.attributes.downloadGame,
# mod.attributes.endorsed,
# mod.attributes.variant,
# mod.attributes.modVersion,
# mod.attributes.fileMD5,
# mod.attributes.changelog,
# mod.attributes.newestChangelog,
# installTime: stat.ctime,
# mountTime: stat.mtime,
# mod.attributes.description,
# mod.attributes.shortDescription,