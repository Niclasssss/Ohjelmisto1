'use strict';
const names = ['John', 'Paul', 'Jones'];

const div = document.getElementById('target')

for (let name of names) {
    div.innerHTML += `<li>${name}</li>`
}