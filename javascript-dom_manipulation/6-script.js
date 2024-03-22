document.addEventListener('DOMContentLoaded', function () {
    // Realizar la solicitud GET a la URL del API
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
        .then(response => {

            // Convertir la respuesta a formato JSON
            return response.json();
        })
        .then(data => {

            const characterName = data.name;

            const characterElement = document.getElementById('character');

            characterElement.textContent = characterName;
        })

});