document.getElementsByClassName("btn js-expand-games")[0].click();
var x = document.getElementsByClassName("mod-image");
var arrayLength = x.length;
var err = [];

for (var i = 0; i < arrayLength; i++) {
    err.push(x[i].href.toString() + "/mods");
}
err.sort()

var err_final = "";
for (var i = 0; i < arrayLength; i++) {
	err_final += err[i];
	if (i < arrayLength - 1) {
		err_final += "\n"
	}
}
console.log(err_final);