let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');

// Event Listener
searchBtn.addEventListener('click', () => {
    searchBtn.classList.toggle('fa-times');
    searchBar.classList.toggle('active');
});