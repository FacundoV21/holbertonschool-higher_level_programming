const headerElement = document.querySelector('header');
const toggleHeaderButton = document.querySelector('#toggle_header');


toggleHeaderButton.addEventListener('click',() => {
  headerElement.classList.contains('green')
  ?
  (
    headerElement.classList.remove('green'),
    headerElement.classList.add('red')
  )
  :
  (
    headerElement.classList.add('green'),
    headerElement.classList.remove('red')
  )
});
