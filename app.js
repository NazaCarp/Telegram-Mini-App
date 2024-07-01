document.addEventListener('DOMContentLoaded', function() {
    const mainButton = document.getElementById('mainButton');
    mainButton.addEventListener('click', function() {
        Telegram.WebApp.sendData("Botón principal clicado");
    });

    Telegram.WebApp.ready();
    Telegram.WebApp.expand();
});