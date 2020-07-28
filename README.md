# NexusMods Vortex Modlist Backup Sorter

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
#NexusGetCategories
Python script to create a category dictionary for every nexus link provided in links.txt in the same directory.

Requires:
- requests 
- time
- re
- ast
- bs4
- urllib.request
- lxml
