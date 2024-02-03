const update = document.querySelector('#update_header');
const headerElement = document.querySelector('#add_item');


update.addEventListener('click', () => {
    headerElement.textContent = 'New Header!!!'
})
