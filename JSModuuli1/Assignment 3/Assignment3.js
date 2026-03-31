const number1 = Number(prompt('Enter the fist number.'))
const number2 = Number(prompt('Enter the second number.'))
const number3 = Number(prompt('Enter the third number.'))

const sum = number1 + number2 + number3
const product = number1 * number2 * number3
const average = (number1 + number2 + number3)/3
document.querySelector('sum').innerHTML = 'The sum of the numbers is: ' + sum + '.';
document.querySelector('#product').innerHTML = 'The product of the numbers is: ' + product + '.';
document.querySelector('#average').innerHTML = 'The average of the numbers is: ' + average + '.';