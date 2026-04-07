function concat(array) {
    let tulos = '';
    for (let item of array) {
        tulos += item
    }
    return tulos;
}

const nimet = ['Jhonny', 'DeeDee', 'Joey', 'Marky']

document.querySelector('#tulos').innerHTML = concat(nimet)