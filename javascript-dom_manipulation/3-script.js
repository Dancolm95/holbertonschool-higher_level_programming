document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('toggle_header');
    const header = document.querySelector('header');

    toggleBtn.addEventListener('click', function () {
        // Toggle entre las clases 'red' y 'green'
        header.classList.toggle('red');
        header.classList.toggle('green');
    });
});
