window.addEventListener('load', setEvents);

function setEvents(e) {
    const recipeElements = document.querySelectorAll('.recipe');

    recipeElements.forEach(element => {
        const likeAElement = element.querySelector('.likes a');
        likeAElement.addEventListener('click', (e) => likeUnlike(e, element, likeAElement))
    });
}

function likeUnlike(e, recipeCardElement, likeAElement) {
    // TODO: Change at deploy
    const baseURL = 'http://localhost:8000';

    if (likeAElement.classList.contains('liked')) {
        unlike(likeAElement, baseURL);
    } else {
        like(recipeCardElement, likeAElement, baseURL);
    }
}

function like(recipeCardElement, likeAElement, baseURL) {
    const recipeID = likeAElement.parentElement.parentElement.id;
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
        .then(response => {
            if (response.ok) {
                likeAElement.classList.add('liked')
                refreshLikes(likeAElement, recipeID, baseURL);
            }
        })
        .catch(error => console.error(error));
}

function unlike(likeAElement, baseURL) {
    const recipeID = likeAElement.parentElement.parentElement.id;
    const csrfToken = getCSRFToken();

    fetch(`${baseURL}/like/${recipeID}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        credentials: 'same-origin'
    })
        .then(response => {
            if (response.ok) {
                likeAElement.classList.toggle('liked');
                refreshLikes(likeAElement, recipeID, baseURL);
            }
        })
        .catch(error => console.error(error))
}

function getCSRFToken() {
    return document.querySelector('#logout-form input[type="hidden"]').value;
}

function refreshLikes(likeAElement, recipeID, baseURL) {
    const likesSpanElement = likeAElement.parentElement.querySelector('.likes-count');
    const csrfToken = getCSRFToken();

    fetch(`${baseURL}/like/${recipeID}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        credentials: 'same-origin'
    })
        .then(response => response.json())
        .then(data => {
            const likesCount = data['likes_count'];
            likesSpanElement.textContent = `${likesCount} likes`
        })
        .catch(error => console.error(error));
}
