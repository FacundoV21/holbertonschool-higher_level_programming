const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
const hello = document.querySelector('#hello');

window.addEventListener('DOMContentLoaded',() => {
  fetch(URL)
  .then((data) => data.json())
  .then((data) => {
    hello.textContent = data.hello
  })
})