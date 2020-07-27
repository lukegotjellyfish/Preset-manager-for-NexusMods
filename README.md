# NexusMods Vortex Modlist Backup Sorter
 Relies on exported file from https://github.com/Garethp/Vortex-Modlist-Backup with a small modification to export data:
 
 Line 138: 
 ```js
 const transformModFormat = (mod) => ({
    name: mod.attributes.modName,
    version: mod.attributes.version,
    category: mod.attributes.category,
    shortDescription: mod.attributes.shortDescription,
    size: mod.attributes.size,
    modId: mod.attributes.modId,
    fileId: mod.attributes.fileId,
    fileName: mod.attributes.fileName,
    author: mod.attributes.author,
    game: mod.attributes.downloadGame,
    endorsed: mod.attributes.endorsed,
});
```
