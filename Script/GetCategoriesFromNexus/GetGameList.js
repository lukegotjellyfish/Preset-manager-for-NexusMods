document.getElementsByClassName("btn js-expand-games")[0].click();
var x = document.getElementsByClassName("mod-image");
var arrayLength = x.length;
var err = [];

for (var i = 0; i < arrayLength; i++) {
    err.push(x[i].href.toString() + "/mods");
}
err.sort()

for (var i = 0; i < arrayLength; i++) {
	console.log(err[i]);
}