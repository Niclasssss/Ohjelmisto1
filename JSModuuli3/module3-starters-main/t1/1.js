const target = document.getElementById ('target')
target.classList.add('my-list')

const list =
    '<li>First item</li>\n' +
    '<li>Second item</li>\n' +
    '<li>Third item</li>';
target.innerHTML = list;