document.getElementsByClassName("btn js-expand-games")[0].click();
var x = document.getElementsByClassName("mod-image");
var arrayLength = x.length;
var err = "";
for (var i = 0; i < arrayLength; i++) {
    err += x[i].href.toString() + "/mods" + "\n";
}
console.log(err.replace(/\n$/, ""));