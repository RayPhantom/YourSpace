//switch theme

let page = document.querySelector('.page');
let thbut = document.querySelector('.thbut');
let thimg = document.querySelector('.thimg');
let thimg2 = document.querySelector('.thimg2');

const currentTheme = localStorage.getItem("theme");
if (currentTheme == "light") {
  document.body.classList.add("light");
}

thbut.onclick = function() {
	page.classList.toggle('light');
	thimg.classList.toggle('nc');
	thimg2.classList.toggle('nc');
	let theme = "dark";

	if (document.body.classList.contains("light")) {
    	theme = "light";
    }

    localStorage.setItem("theme", theme);
};

//lang menu

let form = document.forms.lang;
let sel = form.language;

sel.onchange = function() {
	form.submit();
};
