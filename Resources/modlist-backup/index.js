module.exports =
/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/index.ts");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/getSafe.ts":
/*!************************!*\
  !*** ./src/getSafe.ts ***!
  \************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";

Object.defineProperty(exports, "__esModule", { value: true });
function getSafe(state, path, fallback) {
    let current = state;
    for (const segment of path) {
        if ((current === undefined) || (current === null) || !current.hasOwnProperty(segment)) {
            return fallback;
        }
        else {
            current = current[segment];
        }
    }
    return current;
}
exports.default = getSafe;


/***/ }),

/***/ "./src/index.ts":
/*!**********************!*\
  !*** ./src/index.ts ***!
  \**********************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";

Object.defineProperty(exports, "__esModule", { value: true });
const getSafe_1 = __webpack_require__(/*! ./getSafe */ "./src/getSafe.ts");
const path = __webpack_require__(/*! path */ "path");
const fs = __webpack_require__(/*! fs */ "fs");
const activeProfile = (state) => {
    const profileId = state.settings.profiles.activeProfileId;
    return getSafe_1.default(state, ['persistent', 'profiles', profileId], undefined);
};
const getActiveGameId = (state) => {
    const profile = activeProfile(state);
    return profile !== undefined ? profile.gameId : undefined;
};
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
const getInstalledMods = (state) => Object.values(state.persistent.mods)
    .map(game => Object.values(game).map(mod => transformModFormat(mod)))
    .reduce((result, current) => result.concat(current), []);
const init = (context) => {
    const { api } = context;
    const backupMods = (thisGameOnly = false) => () => {
        const state = api.store.getState();
        let mods = getInstalledMods(state);
        api.selectFile({ create: true, title: 'Select file to export to' })
            .then(fileName => {
            const activeGameId = getActiveGameId(state);
            mods = mods
                .filter(mod => mod.modId && mod.fileId && mod.game);
            if (thisGameOnly) {
                mods = mods.filter(mod => mod.game === activeGameId);
            }
            if (fs.existsSync(fileName)) {
                const existingMods = JSON.parse(fs.readFileSync(fileName)).filter((mod) => mod.game !== activeGameId);
                mods = mods
                    .filter((mod) => mod.game === activeGameId)
                    .concat(existingMods);
            }
            fs.writeFile(path.resolve(fileName), JSON.stringify(mods, null, 4), error => {
                if (error) {
                    api.showErrorNotification(error, error);
                    return;
                }
                api.sendNotification({
                    type: 'success',
                    title: 'Backup Complete',
                    message: `Modlist backed up to ${path.resolve(fileName)}`,
                });
            });
        });
    };
    const restoreMods = () => {
        const state = api.store.getState();
        if (!getSafe_1.default(state, ['persistent', 'nexus', 'userInfo', 'isPremium'], false)) {
            api.showErrorNotification('You need to be a premium member to restore a list of mods', 'You need to be a premium member to restore a list of mods');
            return;
        }
        api.selectFile({ create: false, title: 'Select your backup file to import' })
            .then(fileName => {
            fs.readFile(path.resolve(fileName), (error, jsonString) => {
                const activeGameId = getActiveGameId(state);
                if (error) {
                    api.showErrorNotification(error, error);
                    return;
                }
                let mods = JSON.parse(jsonString);
                mods = mods
                    .filter(mod => mod.game === activeGameId)
                    .map(mod => {
                    if (!mod.source) {
                        mod.source = "nexus";
                    }
                    return mod;
                })
                    .filter(mod => { var _a; return mod.source === "nexus" || !((_a = mod.source) === null || _a === void 0 ? void 0 : _a.length); });
                const modsFound = mods.length;
                const installedMods = getInstalledMods(state);
                mods = mods.filter(mod => !installedMods.some(installedMod => installedMod.game === mod.game && installedMod.modId === mod.modId && installedMod.fileId === mod.fileId));
                for (const mod of mods) {
                    api.events.emit('mod-update', mod.game, mod.modId, mod.fileId, mod.source);
                }
                api.sendNotification({
                    type: 'success',
                    title: `${mods.length} mods for ${activeGameId} restores`,
                    message: `${modsFound} mods found for ${activeGameId}, but only ${mods.length} mods installed`
                });
            });
        });
    };
    context.registerAction('mod-icons', 999, 'show', {}, 'Modlist Backup: Restore', restoreMods);
    context.registerAction('mod-icons', 999, 'show', {}, 'Modlist Backup All Games', backupMods());
    context.registerAction('mod-icons', 999, 'show', {}, 'Modlist Backup Only This Game', backupMods(true));
};
module.exports = { default: init };


/***/ }),

/***/ "fs":
/*!*********************!*\
  !*** external "fs" ***!
  \*********************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = require("fs");

/***/ }),

/***/ "path":
/*!***********************!*\
  !*** external "path" ***!
  \***********************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = require("path");

/***/ })

/******/ });
//# sourceMappingURL=vortex-modlist-backup.js.map