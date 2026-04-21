'use strict'

const form = document.querySelector('form')

form.addEventListener('submit', function(evt){
    evt.preventDefault()
    const value = document.getElementById('query').value
    asynchronousFunction(value)
})

async function asynchronousFunction(value) {
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${value}`)
        const jsonData = await response.json()
        console.log(jsonData)
    } catch (error) {
        console.log(error.message)
    } finally {
        console.log('Done')
    }
}