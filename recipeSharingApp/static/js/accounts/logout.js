function setupLogout() {
    const logoutAElement = document.getElementById('logout-a');
    const logoutForm = document.getElementById('logout-form');

    logoutAElement.addEventListener('click', (e) => logoutForm.submit())
}

setupLogout();
