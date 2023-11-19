let usercont = document.querySelector('.usercont');
let profwind = document.querySelector('.profwind');

usercont.onclick = function() {
	profwind.classList.toggle('profwindnvis');
	//upds.classList.toggle('updvis');
}

let seltype = document.querySelector('.seltype');
let textform = document.querySelector('.textform');
let imgform = document.querySelector('.imgform');

seltype.onchange = function() {
	if (seltype.value === "Img") {
		imgform.classList.add('show');
		textform.classList.remove('show');
	} else if (seltype.value === "Text") {
		imgform.classList.remove('show');
		textform.classList.add('show');
	} else {
		textform.classList.remove('show');
		imgform.classList.remove('show');
	}
}
