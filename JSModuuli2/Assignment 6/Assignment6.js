function rolldice() {
    return Math.floor(Math.random() * 6) + 1;
}

const rolls = [];
let roll = 0;

while (roll !== 6) {
    roll = rolldice();
    rolls.push(roll);
}

const lista = document.querySelector('#lista')
for (let roll of rolls) {
    lista.innerHTML += `<li>${roll}</li>`
}