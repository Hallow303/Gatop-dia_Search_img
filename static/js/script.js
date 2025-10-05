const form = document.getElementById('searchForm');
const loader = document.getElementById('loader');
const resultCard = document.getElementById('resultCard');

form.addEventListener('submit', () => {
    loader.style.display = 'block';
    if (resultCard) resultCard.style.display = 'none';
});
