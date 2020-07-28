# NexusMods Vortex Modlist Backup Sorter

On run, opens a tk file dialog to open the exported file from Vortex-Modlist-Backup to parse.
CSV result is named "modFile(number if duplicate).csv"

![](Demo.png?raw=true)

Requires:
- re
- os
- html
- csv
- catDict (provided or can be created from NexusGetCategories.py)
- tkinter
---
Relies on exported file from https://github.com/Garethp/Vortex-Modlist-Backup with a small modification to export data:

 Line 138: 
 ```js
const transformModFormat = (mod) => ({
    name: mod.attributes.modName,
    version: mod.attributes.version,
    category: mod.attributes.category,
    modId: mod.attributes.modId,
    shortDescription: mod.attributes.shortDescription,
    size: mod.attributes.size,
    fileId: mod.attributes.fileId,
    fileName: mod.attributes.fileName,
    author: mod.attributes.author,
    game: mod.attributes.downloadGame,
    endorsed: mod.attributes.endorsed,
});
```
---
# NexusGetCategories
Python script to create a category dictionary for every nexus link provided in links.txt in the same directory.

Run GetGameList.js in the console of a browser while on https://www.nexusmods.com/games to get a new list, provided list has 1021 games, all as of 28/07/2020

Requires:
- requests 
- time
- re
- ast
- os
- bs4
- urllib.request
- lxml
