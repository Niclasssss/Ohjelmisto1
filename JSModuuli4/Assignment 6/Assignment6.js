'use strict'

const form = document.querySelector('form')

form.addEventListener('submit', function(evt){
    evt.preventDefault()
    const value = document.getElementById('query').value
    asynchronousFunction(value)
})

async function asynchronousFunction(value) {
    try {
        const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${value}`)
        const jsonData = await response.json()
        form.innerHTML = `<article><p>${jsonData}</p></article>`
    } catch (error) {
        console.log(error.message)
    }
}