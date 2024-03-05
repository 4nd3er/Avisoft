const search = document.getElementById('search');
const inputSearch = document.getElementById('inputSearch');
const dateSearch = document.getElementById('dateSearch');

const searchSelect = (value) => {
    if (value === 'input') {
        search.style.marginBottom = '1.3rem';
        setTimeout(() => {
            inputSearch.style.display = 'flex';
            inputSearch.style.opacity = '100';
        }, 250);
        dateSearch.style.display = 'none';
        dateSearch.style.opacity = '0';
    } else if (value === 'date') {
        search.style.marginBottom = '1.3rem';
        setTimeout(() => {
            dateSearch.style.display = 'flex';
            dateSearch.style.opacity = '100';
        }, 250);
        inputSearch.style.display = 'none';
        inputSearch.style.opacity = '0';
    } else {
        search.style.marginBottom = '0';
        dateSearch.style.display = 'none';
        dateSearch.style.opacity = '0';
        inputSearch.style.display = 'none';
        inputSearch.style.opacity = '0';
    }
}

setTimeout(async () => {
    searchSelect(search.value);
}, 100);