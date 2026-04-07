const number = Number(prompt('Enter the number of participants.'))
const participants =  [];

for (let i = 0; i < number; i++) {
    const input = prompt('Enter the name of the participant.')
    participants.push(input)
}
participants.sort()

const lista = document.querySelector('#lista')
for (let  i = 0; i < participants.length; i++) {
    lista.innerHTML += `<ol>${participants[i]}</ol>`;
}