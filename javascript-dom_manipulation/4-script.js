document.addEventListener('DOMContentLoaded', function () {
    const addItem = document.getElementById('add_item');
    const myList = document.querySelector('.my_list');

    addItem.addEventListener('click', function () {
        // Crear un nuevo elemento de lista <li>
        const newItem = document.createElement('li');
        // Agregar texto al nuevo elemento de lista
        newItem.textContent = 'Item';
        // Agregar el nuevo elemento de lista a la lista <ul>
        myList.appendChild(newItem);
    });
});
