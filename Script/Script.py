# -*- coding: utf-8 -*-
import re
import os
import html
import csv
import catDict
import tkinter as tk
from tkinter import filedialog


def categorytranslate(category, game):
    try:
        return catDict.nexus_dictionaries[game][category]
    except:
        print("Failed to find a match in nexus_dictionaries")
        return category


def trimlist(x, type):
    x[0] = x[0].replace('        "name": "', "")[:-3]
    x[1] = x[1].replace('        "version": "', "")[:-3]
    x[2] = x[2].replace('        "category": ', "")[:-2]
    x[3] = html.unescape(x[3].replace('        "shortDescription": ', "")[:-2])
    x[3] = re.sub("(\[[^\]]*\])", "", x[3])[1:-1]
    x[4] = x[4].replace('        "modId": ', "")[:-2].replace('"',"")
    x[5] = x[5].replace('        "fileId": ', "")[:-2]
    x[6] = x[6].replace('        "fileName": "', "")[:-3]
    x[7] = x[7].replace('        "author": "', "")[:-3]
    if type == 1:  # No endorsed section
        x[8] = x[8].replace('        "game": "', "")[:-2]
    if type == 2:  # Has endorsed section
        x[8] = x[8].replace('        "game": "', "")[:-3]
        x[9] = x[9].replace('        "endorsed": "', "")[:-2]
    x[2] = categorytranslate(x[2], x[8])

    # Add link
    x.insert(4,"https://www.nexusmods.com/oblivion/mods/" + x[4])

    return x


while True:
    modList = []
    root = tk.Tk()
    root.withdraw()


    file_path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title="Select Preset to Inherit",
                                           filetypes=[("Modlist Export File", "*.*")])
    if len(file_path) < 1: continue

    with open(file_path, "r", encoding='utf-8') as modfile:
        lines = modfile.readlines()
        modList = []

        i = 0
        startMod = 0
        endMod = 0
        for line in lines:
            if line == "    {\n":
                startMod = i + 1
            elif (line == "    },\n") or (line == "    }\n"):
                endMod = i

                if lines[endMod - 1][9] == 'g':
                    tempList = lines[startMod:endMod]
                    tempList = trimlist(tempList, 1)
                    tempList.append("Undecided")
                    modList.append(tempList)
                else:
                    modList.append(trimlist(lines[startMod:endMod], 2))
            i += 1


        spacer = " "
        buffer = 21
        vbuffer = 11
        with open("modFile.csv", "w", newline='\n') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(["Name", "Version", "Category", "Description", "Link", "ModID","FileID", "FileName", "Author", "Game", "Endorsed"])
            print("Name                 | Version    | Category             | Description          " +
                  "| Link                 | ModID      | FileID     | FileName   | Author     | Game       | Endorsed")
            print("-"*179)
            for mod in modList:
                csvwriter.writerow(mod)
                print(mod[0][:buffer]   + spacer * (buffer-len(mod[0][:buffer]))   + "| " +
                      mod[1][:vbuffer]  + spacer * (vbuffer-len(mod[1][:buffer]))  + "| " +
                      mod[2][:buffer]   + spacer * (buffer-len(mod[2][:buffer]))   + "| " +
                      mod[3][:buffer]   + spacer * (buffer-len(mod[3][:buffer]))   + "| " +
                      mod[4][:buffer]   + spacer * (buffer-len(mod[4][:buffer]))   + "| " +
                      mod[5][:vbuffer]  + spacer * (vbuffer-len(mod[5][:vbuffer])) + "| " +
                      mod[6][:vbuffer]  + spacer * (vbuffer-len(mod[6][:vbuffer])) + "| " +
                      mod[7][:vbuffer]  + spacer * (vbuffer-len(mod[7][:vbuffer])) + "| " +
                      mod[8][:vbuffer]  + spacer * (vbuffer-len(mod[8][:vbuffer])) + "| " +
                      mod[9][:vbuffer]  + spacer * (vbuffer-len(mod[9][:vbuffer])) + "| " +
                      mod[10][:vbuffer] + spacer * (vbuffer-len(mod[10][:buffer])))

    input("\n\n\nFinished, press ENTER to restart.")
    os.system('cls')

# https://www.nexusmods.com/skyrimspecialedition/mods/  MOD_ID ?tab=files&file_id= FILE_ID &nmm=1
# Vortex Mod Attributes:
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
