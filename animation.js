"use strict";

var SCREEN_WIDTH = window.innerWidth;
var SCREEN_HEIGHT = window.innerHeight;

const RADIUS = 100;
var RADIUS_SCALE = 1;
const RADIUS_SCALE_MIN = 1;
const RADIUS_SCALE_MAX = 2;

const PARTICLES_QTY = 20;
const ROTATION_SPEED = 15;

var canvas = null;
var context = null;
var particles = [];

var mouseX = SCREEN_WIDTH * .5;
var mouseY = SCREEN_HEIGHT * .5;
var mouseIsDown = false;

window.onload = init;

function init() {
	canvas = document.getElementById("loadingParticlesCanvas");

	if (canvas && canvas.getContext) {
		context = canvas.getContext("2d");

		document.addEventListener("touchstart", documentTouchHandler, false);
		document.addEventListener("touchmove", documentTouchHandler, false);
		window.addEventListener("mousemove", documentMouseMoveHandler, false);
		window.addEventListener("mousedown", documentMouseClickHandler, false);
		window.addEventListener("mouseup", documentMouseClickHandler, false);
		window.addEventListener("resize", windowResizeHandler, false);

		createParticles();
		windowResizeHandler();
		setInterval(loop, ROTATION_SPEED);
	}
}

function createParticles() {
	for (let i=0; i<PARTICLES_QTY; i++) {
		particles.push({
			size: 1,
			position: {x: mouseX, y: mouseY},
			offset: {x: 0, y: 0},
			shift: {x: mouseX, y: mouseY},
			speed: .01 + Math.random() * .04,
			targetSize: 1,
			fillColor: "#" + (Math.random() * 0x404040 + 0xaaaaaa | 0).toString(16),
			orbit: RADIUS * .5 + (RADIUS * .5 * Math.random())
		});
	}
}

function documentTouchHandler(event) {
	if (event.touches.length == 1) {
		mouseX = Math.max(Math.min(event.touches[0].pageX - (window.innerWidth - SCREEN_WIDTH) * .5, SCREEN_WIDTH), 0);
		mouseY = Math.max(Math.min(event.touches[0].pageY - (window.innerHeight - SCREEN_HEIGHT) * .5, SCREEN_HEIGHT), 0);
	}
}

function documentMouseMoveHandler(event) {
	if (mouseIsDown) {
		mouseX = Math.max(Math.min(event.clientX - (window.innerWidth - SCREEN_WIDTH) * .5, SCREEN_WIDTH), 0);
		mouseY = Math.max(Math.min(event.clientY - (window.innerHeight - SCREEN_HEIGHT) * .5, SCREEN_HEIGHT), 0);
	}
}

function documentMouseClickHandler(event) {
	mouseIsDown = !mouseIsDown;
	mouseX = Math.max(Math.min(event.clientX - (window.innerWidth - SCREEN_WIDTH) * .5, SCREEN_WIDTH), 0);
	mouseY = Math.max(Math.min(event.clientY - (window.innerHeight - SCREEN_HEIGHT) * .5, SCREEN_HEIGHT), 0);
}

function windowResizeHandler() {
	canvas.width = SCREEN_WIDTH = window.innerWidth;
	canvas.height = SCREEN_HEIGHT = window.innerHeight;

	mouseX = SCREEN_WIDTH * .5;
	mouseY = SCREEN_HEIGHT * .5;
}

function loop() {
	if (mouseIsDown) {
		RADIUS_SCALE += (RADIUS_SCALE_MAX - RADIUS_SCALE) * .02;
	} else {
		RADIUS_SCALE -= (RADIUS_SCALE - RADIUS_SCALE_MIN) * .02;
	}

	RADIUS_SCALE = Math.min(RADIUS_SCALE, RADIUS_SCALE_MAX);

	context.fillStyle = "rgba(0,0,0,.05)";
	context.fillRect(0, 0, context.canvas.width, context.canvas.height);

	for (let i=0; i<particles.length; i++) {
		let initialPos = {x: particles[i].position.x, y: particles[i].position.y};

		// Rotation
		particles[i].offset.x += particles[i].speed;
		particles[i].offset.y += particles[i].speed;

		// Follow mouse with lag
		particles[i].shift.x += (mouseX - particles[i].shift.x) * particles[i].speed;
		particles[i].shift.y += (mouseY - particles[i].shift.y) * particles[i].speed;

		// Apply position
		particles[i].position.x = particles[i].shift.x + Math.cos(i + particles[i].offset.x) * particles[i].orbit * RADIUS_SCALE;
		particles[i].position.y = particles[i].shift.y + Math.sin(i + particles[i].offset.y) * particles[i].orbit * RADIUS_SCALE;

		// Modify paticles size
		particles[i].size += (particles[i].targetSize - particles[i].size) * .05;

		if (Math.round(particles[i].size) == Math.round(particles[i].targetSize)) {
			particles[i].targetSize = 1 + Math.random() * 7;
		}

		context.beginPath();
		context.fillStyle = particles[i].fillColor;
		context.strokeStyle = particles[i].fillColor;
		context.lineWidth = particles[i].size;
		context.moveTo(initialPos.x, initialPos.y);
		context.lineTo(particles[i].position.x, particles[i].position.y);
		context.stroke();
		context.arc(particles[i].position.x, particles[i].position.y, particles[i].size / 2, 0, Math.PI * 2, true);
		context.fill();
	}
}