let agrc1 = document.querySelector('.agrc');
let agrs1 = document.querySelector('.agrs');

agrc1.onchange = function() {
	if (agrc1.checked) {
		agrs1.disabled = false;
	} else {
		agrs1.disabled = true;
	}
};