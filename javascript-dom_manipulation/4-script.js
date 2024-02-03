const add = document.querySelector('#add_item');

add.addEventListener('click', () => {
  const li = document.createElement('li')
  li.textContent = 'Item'
  document.querySelector('.my_list').appendChild(li)
})
