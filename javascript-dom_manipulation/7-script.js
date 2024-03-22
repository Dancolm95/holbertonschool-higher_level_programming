document.addEventListener('DOMContentLoaded', function () {
    // Realizar la solicitud GET a la URL del API
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then(response => {
            // Verificar si la respuesta fue exitosa

            return response.json();
        })
        .then(data => {
            // Obtener la lista de películas del objeto JSON
            const movies = data.results;
            // Seleccionar el elemento <ul> con el id 'list_movies'
            const moviesList = document.getElementById('list_movies');
            // Iterar sobre la lista de películas y agregar cada título a la lista
            movies.forEach(movie => {
                const listItem = document.createElement('li');
                listItem.textContent = movie.title;
                moviesList.appendChild(listItem);
            });
        });
});
