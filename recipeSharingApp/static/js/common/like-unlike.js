window.addEventListener('load', setEvents);

function setEvents(e) {
    const recipeCardElements = document.querySelectorAll('.recipe-card');

    recipeCardElements.forEach(element => {
        const likeAElement = element.querySelector('.likes a');
        likeAElement.addEventListener('click', (e) => likeUnlike(e, element, likeAElement))
    });
}

function likeUnlike(e, recipeCardElement, likeAElement) {
    // TODO: Change at deploy
    const baseURL = 'http://localhost:8000';

    if (likeAElement.classList.contains('liked')) {
        unlike();
    } else {
        like(recipeCardElement, likeAElement, baseURL);
    }
}

function like(recipeCardElement, likeAElement, baseURL) {
    const recipeID = recipeCardElement.id;
    const csrftoken = getCSRFToken();

    fetch(`${baseURL}/like/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        credentials: 'same-origin',
        body: JSON.stringify({ recipe: recipeID })
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}

function unlike() {

}

function getCSRFToken() {
    return document.querySelector('#logout-form input[type="hidden"]').value;
}
