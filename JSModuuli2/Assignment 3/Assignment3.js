const koirat = [];

for (let i = 0; i < 6; i++) {
    const koira = prompt('Give the name of the dog')
    koirat.push(koira)
}
koirat.sort()
koirat.reverse()

const lista = document.querySelector('#lista')
for (let koira of koirat) {
    lista.innerHTML += `<li>${koira}</li>`
}