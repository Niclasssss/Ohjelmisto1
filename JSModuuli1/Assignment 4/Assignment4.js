function getRandomInt(max) {
    return Math.floor(Math.random() * max)
}

const luku = getRandomInt(4)
const nimi = prompt('Type your name.')

if (luku == 0) {
    document.querySelector('#luku').innerHTML = nimi + ', you are Gryffindor';
} else if (luku == 1) {
    document.querySelector('#luku').innerHTML = nimi + ', you are Slytherin';
} else if (luku == 2) {
    document.querySelector('#luku').innerHTML = nimi + ', you are Hufflepuff';
} else if (luku == 3) {
    document.querySelector('#luku').innerHTML = nimi + ', you are Ravenclaw';
}
