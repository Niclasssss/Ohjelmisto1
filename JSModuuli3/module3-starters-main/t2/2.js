const div = document.getElementById('target')

const list1 = document.createElement('li')
list1.innerHTML = 'First item'

const list2 = document.createElement('li')
list2.innerHTML = 'Second item'
list2.classList.add('my-list')

const list3 = document.createElement('li')
list3.innerHTML = 'Third item'

div.appendChild(list1)
div.appendChild(list2)
div.appendChild(list3)