var carosol_container = document.querySelector('.carosol-container'),
	carosol_container_inner = document.querySelector('.carosol-container-inner'),
	carosol_items = document.querySelectorAll('.carosol-container .item');

carosol_container_inner.style.width = carosol_items.length * 240 + 'px';

var left_btn = document.querySelector('.left'),
	right_btn = document.querySelector('.right');

left_btn.addEventListener('click', go_left);
right_btn.addEventListener('click', go_right);

var margin_now = 0;
var left_to_go = 0;
left_btn.style.display = 'none';

function go_right(){
	left_btn.style.display = 'inline';
	margin_now -= 229;
	left_to_go += 229;
	if(margin_now - 229 * 2 < -carosol_container_inner.offsetWidth){
		right_btn.style.display = 'none';
	}
	carosol_container_inner.style.marginLeft = margin_now + 'px';
}
function go_left(){
	right_btn.style.display = 'inline';
	left_to_go -= 229;
	margin_now += 229;
	if(left_to_go <= 0){
		left_btn.style.display = 'none';
		left_to_go = 0;
	}
	carosol_container_inner.style.marginLeft = margin_now + 'px';
}

var carosol_container2 = document.querySelector('.carosol-container2'),
	carosol_container_inner2 = document.querySelector('.carosol-container-inner2'),
	carosol_items2 = document.querySelectorAll('.carosol-container2 .item');

carosol_container_inner2.style.width = carosol_items2.length * 240 + 'px';

var left_btn2 = document.querySelector('.left2'),
	right_btn2 = document.querySelector('.right2');

left_btn2.addEventListener('click', go_left2);
right_btn2.addEventListener('click', go_right2);

var margin_now2 = 0;
var left_to_go2 = 0;
left_btn2.style.display = 'none';

function go_right2(){
	left_btn2.style.display = 'inline';
	margin_now2 -= 229;
	left_to_go2 += 229;
	if(margin_now2 - 229 * 2 < -carosol_container_inner2.offsetWidth){
		right_btn2.style.display = 'none';
	}
	carosol_container_inner2.style.marginLeft = margin_now2 + 'px';
}
function go_left2(){
	right_btn2.style.display = 'inline';
	left_to_go2 -= 229;
	margin_now2 += 229;
	if(left_to_go2 <= 0){
		left_btn2.style.display = 'none';
		left_to_go2 = 0;
	}
	carosol_container_inner2.style.marginLeft = margin_now2 + 'px';
}

var carosol_container3 = document.querySelector('.carosol-container3'),
	carosol_container_inner3 = document.querySelector('.carosol-container-inner3'),
	carosol_items3 = document.querySelectorAll('.carosol-container3 .item');

carosol_container_inner3.style.width = carosol_items3.length * 240 + 'px';

var left_btn3 = document.querySelector('.left3'),
	right_btn3 = document.querySelector('.right3');

left_btn3.addEventListener('click', go_left3);
right_btn3.addEventListener('click', go_right3);

var margin_now3 = 0;
var left_to_go3 = 0;
left_btn3.style.display = 'none';

function go_right3(){
	left_btn3.style.display = 'inline';
	margin_now3 -= 229;
	left_to_go3 += 229;
	if(margin_now3 - 229 * 2 < -carosol_container_inner3.offsetWidth){
		right_btn3.style.display = 'none';
	}
	carosol_container_inner3.style.marginLeft = margin_now3 + 'px';
}
function go_left3(){
	right_btn3.style.display = 'inline';
	left_to_go3 -= 229;
	margin_now3 += 229;
	if(left_to_go3 <= 0){
		left_btn3.style.display = 'none';
		left_to_go3 = 0;
	}
	carosol_container_inner3.style.marginLeft = margin_now3 + 'px';
}

var carosol_container4 = document.querySelector('.carosol-container4'),
	carosol_container_inner4 = document.querySelector('.carosol-container-inner4'),
	carosol_items4 = document.querySelectorAll('.carosol-container4 .item');

carosol_container_inner4.style.width = carosol_items4.length * 240 + 'px';

var left_btn4 = document.querySelector('.left4'),
	right_btn4 = document.querySelector('.right4');

left_btn4.addEventListener('click', go_left4);
right_btn4.addEventListener('click', go_right4);

var margin_now4 = 0;
var left_to_go4 = 0;
left_btn4.style.display = 'none';

function go_right4(){
	left_btn4.style.display = 'inline';
	margin_now4 -= 229;
	left_to_go4 += 229;
	if(margin_now4 - 229 * 2 < -carosol_container_inner4.offsetWidth){
		right_btn4.style.display = 'none';
	}
	carosol_container_inner4.style.marginLeft = margin_now4 + 'px';
}
function go_left4(){
	right_btn4.style.display = 'inline';
	left_to_go4 -= 229;
	margin_now4 += 229;
	if(left_to_go4 <= 0){
		left_btn4.style.display = 'none';
		left_to_go4 = 0;
	}
	carosol_container_inner4.style.marginLeft = margin_now4 + 'px';
}

var carosol_container5 = document.querySelector('.carosol-container5'),
	carosol_container_inner5 = document.querySelector('.carosol-container-inner5'),
	carosol_items5 = document.querySelectorAll('.carosol-container5 .item');

carosol_container_inner5.style.width = carosol_items5.length * 240 + 'px';

var left_btn5 = document.querySelector('.left5'),
	right_btn5 = document.querySelector('.right5');

left_btn5.addEventListener('click', go_left5);
right_btn5.addEventListener('click', go_right5);

var margin_now5 = 0;
var left_to_go5 = 0;
left_btn5.style.display = 'none';

function go_right5(){
	left_btn5.style.display = 'inline';
	margin_now5 -= 229;
	left_to_go5 += 229;
	if(margin_now5 - 229 * 2 < -carosol_container_inner5.offsetWidth){
		right_btn5.style.display = 'none';
	}
	carosol_container_inner5.style.marginLeft = margin_now5 + 'px';
}
function go_left5(){
	right_btn5.style.display = 'inline';
	left_to_go5 -= 229;
	margin_now5 += 229;
	if(left_to_go5 <= 0){
		left_btn5.style.display = 'none';
		left_to_go5 = 0;
	}
	carosol_container_inner5.style.marginLeft = margin_now5 + 'px';
}
