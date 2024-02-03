const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
const character = document.querySelector('#character');

fetch(URL)
.then((data) => {
  return data.json()
})
.then((data) => {
  character.textContent = data.name
})
