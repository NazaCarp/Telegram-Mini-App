Tengo un proyecto con estos archivos:
mine.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mine</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <script src="https://code.iconify.design/iconify-icon/2.1.0/iconify-icon.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: radial-gradient(circle at center, #0047ab, #002357, #000000);
            color: white;
            margin: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            user-select: none; /* Evita que la imagen sea seleccionable */
            -webkit-tap-highlight-color: transparent; /* Deshabilita el resaltado en dispositivos Android */
            transition: filter 0.3s ease;
        }
        * {
            margin: 0px;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }
        .score {
            font-weight: bold;
            text-align: center;
            margin-top: 70px;
            font-size: 80px;
        }
        .navbar {
            display: flex;
            justify-content: space-around;
            align-items: center;
            width: 100%;
            height: 60px;
            border-radius: 50px;
            margin: 0 auto; /* Centra la barra de navegación */
            background-color: #222222;
            position: fixed;
            bottom: 0;
            user-select: none; /* Evita que los íconos sean seleccionables */
            -webkit-tap-highlight-color: transparent; /* Deshabilita el resaltado en dispositivos Android */
            z-index: 1000; /* Asegura que la barra de navegación esté por encima del contenido */
        }
        .navbar a {
            color: gray;
            text-decoration: none;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 14px;
            position: relative;
        }
        .navbar a.active span, .navbar a.active iconify-icon {
            color: white;
        }
        .navbar a iconify-icon {
            font-size: 24px;
        }
        .navbar a.active::before {
            content: '';
            position: absolute;
            top: -7px;
            left: -14px;
            right: -14px;
            bottom: -7px;
            border-radius: 50px;
            background-color: rgba(0, 0, 0, 0.267);
            z-index: -1;
        }
        .tabs {
            display: flex;
            justify-content: space-around;
            align-items: center;
            width: 100%;
            height: 60px;
            background-color: #222222;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
        }
        .tabs a {
            color: gray;
            text-decoration: none;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 14px;
            position: relative;
        }
        .tabs a.active span, .tabs a.active iconify-icon {
            color: white;
        }
        .tabs a iconify-icon {
            font-size: 24px;
        }
        .tabs a.active::before {
            content: '';
            position: absolute;
            top: -7px;
            left: -14px;
            right: -14px;
            bottom: -7px;
            border-radius: 50px;
            background-color: rgba(0, 0, 0, 0.267);
            z-index: -1;
        }
        .tab-content {
            display: none;
            flex-direction: column;
            align-items: center;
            width: 100%;
            margin-top: 60px;
            margin-bottom: 70px; /* Añadido para evitar que la barra de navegación tape el contenido */
        }
        .tab-content.active {
            display: flex;
        }
        .rectangle {
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #333;
            border-radius: 50px;
            border: 2px solid white;
            width: 95%;
            margin: 5px;
            padding: 5px;
            cursor: pointer;
        }
        .icon {
            margin: 10px;
            width: 75px; /* Ajusta el ancho de la imagen */
            height: 75px; /* Ajusta la altura de la imagen */
            object-fit: contain; /* Asegura que la imagen se ajuste sin deformarse */
        }
        .row {
            display: flex;
            justify-content: space-around;
            width: 100%;
        }
        /* Añadir estilos para el subtítulo y el contenido adicional */
        .subtitle {
            font-size: 14px;
            color: gray;
            margin-top: 5px;
        }
        .profit-info {
            display: flex;
            align-items: center;
            margin-top: 5px;
        }
        .profit-info iconify-icon {
            font-size: 18px;
            margin-right: 5px;
        }
        .profit-info span {
            font-size: 16px;
            color: yellow;
        }
        /* Añadir estilos para la línea divisora y las secciones adicionales */
        .divider {
            width: 100%;
            height: 1px;
            background-color: rgb(255, 255, 255, 0.2);
            margin: 10px 0;
        }

        .vertical-divider {
            width: 1px;
            height: 100%;
            margin-left: 5px;
            margin-right: 5px;
            background-color: rgb(255, 255, 255, 0.2);
        }

        .section {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .section-left {
            display: flex;
            justify-content: flex-end; /* Alinea el contenido a la derecha */
            align-items: center;
            flex: 4; /* 70% del espacio */
        }

        .section-right {
            display: flex;
            align-items: center;
            flex: 6; /* 30% del espacio */
        }

        .section-right iconify-icon {
            font-size: 18px;
            margin-right: 5px;
        }

        .section-right span {
            font-size: 16px;
            color: yellow;
        }

        .text-content {
            display: flex;
            flex-direction: column;
            width: 100%;
            align-items: center;
        }

        .tab-container {
            width: 100%;
            overflow: hidden;
            position: relative;
        }

        .tab-slider {
            display: flex;
            transition: transform 0.3s ease-in-out;
        }

        .tab-slide {
            flex: 0 0 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Estilos para la alerta */
        .alert-menu {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 80%;
            max-width: 400px;
            background-color: #333;
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            z-index: 1000;
        }
        .alert-menu .icon {
            margin: 20px auto; /* Centrar el ícono */
            width: 100%; /* Aumentar el ancho del ícono */
            height: 100%; /* Aumentar la altura del ícono */
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .alert-menu .icon img {
            max-width: 100%;
            max-height: 100%;
        }
        .alert-menu .close {
            position: absolute;
            top: 10px;
            right: 10px;
            cursor: pointer;
            font-size: 20px;
        }
        .blur-content {
            filter: blur(5px);
            pointer-events: none;
            transition: filter 0.3s ease;
        }
        .alert-text {
            font-size: 24px; /* Tamaño del título en los rectángulos */
        }
        .subtitle {
            margin-top: 20px;
            font-size: 14px;
            color: rgba(255, 255, 255, 0.7);
        }
        .second-subtitle {
            margin-top: 10px;
            font-size: 14px;
            color: rgba(255, 255, 255, 0.7);
        }
        .cost {
            font-size: 48px;
            margin-top: 25px;
            font-weight: bold;
        }
        .cost.yellow {
            color: yellow;
        }
        .cost.gray {
            color: gray;
        }
        .action-button {
            width: 100%;
            margin-top: 10px;
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .action-button.active {
            background-color: #0066ff;
            color: white;
        }
        .action-button.inactive {
            background-color: #808080;
            color: white;
            cursor: not-allowed;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="score" id="score" style="color: rgb(255, 255, 255)"><iconify-icon icon="twemoji:coin" style="font-size: 60px;"></iconify-icon>0</div>
        <h5>Balance</h5>
        <div class="tabs">
            <a href="#" id="northAmericaTab" class="active"><iconify-icon icon="simple-icons:mls"></iconify-icon><span>North America</span></a>
            <a href="#" id="southAmericaTab"><iconify-icon icon="simple-icons:conmebol"></iconify-icon><span>South America</span></a>
            <a href="#" id="europeTab"><iconify-icon icon="simple-icons:uefa"></iconify-icon><span>Europe</span></a>
            <a href="#" id="asiaTab"><iconify-icon icon="simple-icons:afc"></iconify-icon><span>Asia</span></a>
            <a href="#" id="africaTab"><iconify-icon icon="simple-icons:caf"></iconify-icon><span>Africa</span></a>
            <a href="#" id="oceaniaTab"><iconify-icon icon="simple-icons:caf"></iconify-icon><span>Oceania</span></a>
        </div>
        <div class="tab-container">
            <div class="tab-slider" id="tabSlider">
                <div class="tab-slide" id="northAmericaContent"></div>
                <div class="tab-slide" id="southAmericaContent"></div>
                <div class="tab-slide" id="europeContent"></div>
                <div class="tab-slide" id="asiaContent"></div>
                <div class="tab-slide" id="africaContent"></div>
                <div class="tab-slide" id="oceaniaContent"></div>
            </div>
        </div>
    </div>
    <div class="navbar">
        <a href="index.html" id="exchangeNav"><iconify-icon icon="simple-icons:binance"></iconify-icon><span>Exchange</span></a>
        <a href="mine.html" id="mineNav" class="active"><iconify-icon icon="mdi:pickaxe"></iconify-icon><span>Mine</span></a>
        <a href="friends.html" id="friendsNav"><iconify-icon icon="clarity:group-solid"></iconify-icon><span>Friends</span></a>
        <a href="index.html#earn" id="earnNav"><iconify-icon icon="fa6-solid:coins"></iconify-icon><span>Earn</span></a>
        <a href="index.html#airdrop" id="airdropNav"><iconify-icon icon="et:wallet"></iconify-icon><span>Airdrop</span></a>
    </div>
    <div class="alert-menu" id="alertMenu">
        <div class="close" onclick="closeAlertMenu()"><iconify-icon icon="ph:x-circle-duotone"></iconify-icon></div>
        <div class="icon" id="alertIcon"></div>
        <div class="alert-text" id="alertText"></div>
        <div class="subtitle" id="alertSubtitle"></div>
        <div class="second-subtitle" id="alertSecondSubtitle"></div>
        <div class="cost" id="alertCost"></div>
        <button class="action-button" id="actionButton">Buy</button>
    </div>
    <script>
        let levels
        const tg = window.Telegram.WebApp;
        const user_id = tg.initDataUnsafe.user.id;

        let score = 0;
        let profitPerHour = 0;

        async function loadScore() {
            let storedScore = localStorage.getItem('score');
            let storedProfitPerHour = localStorage.getItem('profit_per_hour');
            
            if (storedScore === null || storedProfitPerHour === null){
                const response = await fetch(`/get_counters?user_id=${user_id}`);
                const data = await response.json();
                storedScore = data.score;
                storedProfitPerHour = data.profit_per_hour;
            }
            
            // Convertir los valores almacenados en números
            score = parseFloat(storedScore);
            profitPerHour = parseFloat(storedProfitPerHour);

            // Actualizar la interfaz del usuario
            document.getElementById('score').innerHTML = `<iconify-icon icon="twemoji:coin" style="font-size: 60px;"></iconify-icon> ${score.toFixed(3)}`;
            
            // Guardar score y profitPerHour en localStorage
            localStorage.setItem('score', score);
            localStorage.setItem('profit_per_hour', profitPerHour);
            
            // Iniciar el intervalo para incrementar el score cada segundo
            setInterval(incrementScore, 1000);
        }

        function incrementScore() {
            const scoreElement = document.getElementById('score');
            score += profitPerHour / 3600;
            scoreElement.innerText = score.toFixed(3);
            localStorage.setItem('score', score);

            // Actualizar el score en la base de datos
            saveCounts();
        }
        async function saveCounts() {
            fetch('/update_counters', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_id: user_id, score: score })
            });
        }

        async function loadMineLevels() {
            const response = await fetch(`/get_mine_levels?user_id=${user_id}`);
            const data = await response.json();
            return data.clubs; // Asegúrate de que estás accediendo al campo correcto
        }

        function generateRectangles(containerId, clubs, levels) {
            const rows = Math.ceil(clubs.length / 2);

            // Limpiar contenido anterior
            const height = 233 * rows + 85;

            const containernorth = document.getElementById('northAmericaContent');
            containernorth.style = `height: ${height}px;`
            
            const containersouth = document.getElementById('southAmericaContent');
            containersouth.style = `height: ${height}px;`

            const containereurope = document.getElementById('europeContent');
            containereurope.style = `height: ${height}px;`
            
            const containerasia = document.getElementById('asiaContent');
            containerasia.style = `height: ${height}px;`
            
            const containerafrica = document.getElementById('africaContent');
            containerafrica.style = `height: ${height}px;`

            const containeroceania = document.getElementById('oceaniaContent');
            containeroceania.style = `height: ${height}px;`
            
            const container = document.getElementById(containerId);
            container.innerHTML = ''; // Limpiar contenido anterior

            for (let i = 0; i < rows; i++) {
                const row = document.createElement('div');
                row.className = 'row';

                for (let j = 0; j < 2; j++) {
                    const index = i * 2 + j;
                    if (index >= clubs.length) break; // Salir si no hay más clubes

                    const club = clubs[index];

                    const rectangle = document.createElement('div');
                    rectangle.className = 'rectangle';
                    rectangle.setAttribute('data-cost', club.cost); // Añadir el costo como atributo
                    rectangle.setAttribute('data-club-id', club.name); // Añadir el identificador del club

                    const imageElement = document.createElement('img');
                    imageElement.className = 'icon';
                    imageElement.src = club.image;
                    imageElement.alt = club.name;

                    const textContent = document.createElement('div');
                    textContent.className = 'text-content';

                    const title = document.createElement('h3');
                    title.style.fontSize = '14px'; // Tamaño de letra más chico
                    title.textContent = club.name;

                    const subtitle = document.createElement('div');
                    subtitle.className = 'subtitle';
                    subtitle.textContent = 'Profit per hour';

                    const profitInfo = document.createElement('div');
                    profitInfo.className = 'profit-info';
                    const profitIcon = document.createElement('iconify-icon');
                    profitIcon.icon = 'twemoji:coin';
                    const profitSpan = document.createElement('span');

                    // Calcular el 'Profit per hour' como el 10% del 'cost'
                    const profitPerHour = Math.round(club.cost * 0.1);
                    profitSpan.textContent = profitPerHour;

                    profitInfo.appendChild(profitIcon);
                    profitInfo.appendChild(profitSpan);

                    const divider = document.createElement('div');
                    divider.className = 'divider';

                    const section = document.createElement('div');
                    section.className = 'section';

                    const sectionLeft = document.createElement('div');
                    sectionLeft.className = 'section-left';
                    sectionLeft.textContent = `lvl ${levels[club.name] || 1}`;

                    const verticalDivider = document.createElement('div');
                    verticalDivider.className = 'vertical-divider';

                    const sectionRight = document.createElement('div');
                    sectionRight.className = 'section-right';
                    const sectionRightIcon = document.createElement('iconify-icon');
                    sectionRightIcon.icon = 'twemoji:coin';
                    const sectionRightSpan = document.createElement('span');
                    sectionRightSpan.textContent = club.cost; // Mostrar el valor de 'cost' aquí

                    sectionRight.appendChild(sectionRightIcon);
                    sectionRight.appendChild(sectionRightSpan);

                    section.appendChild(sectionLeft);
                    section.appendChild(verticalDivider);
                    section.appendChild(sectionRight);

                    textContent.appendChild(title);
                    textContent.appendChild(subtitle);
                    textContent.appendChild(profitInfo);
                    textContent.appendChild(divider);
                    textContent.appendChild(section);

                    rectangle.appendChild(imageElement);
                    rectangle.appendChild(textContent);
                    row.appendChild(rectangle);

                    // Añadir evento de clic para mostrar la alerta
                    rectangle.addEventListener('click', () => {
                        showAlert(club);
                    });
                }

                container.appendChild(row);
            }
        }

        document.addEventListener('DOMContentLoaded', async function() {
            await loadScore();
            levels = await loadMineLevels();

            const tabs = document.querySelectorAll('.tabs a');
            const tabSlider = document.getElementById('tabSlider');

            const northAmericaClubs = [
                { name: 'Inter Miami CF', image: '/static/images/North America/Inter Miami CF.svg', cost: 7823 },
                { name: 'Houston Dynamo FC', image: '/static/images/North America/Houston Dynamo FC.svg', cost: 3159 },
                { name: 'Los Angeles Galaxy', image: '/static/images/North America/Los Angeles Galaxy.svg', cost: 9467 },
                { name: 'CF Montreal', image: '/static/images/North America/CF Montreal.svg', cost: 2614 },
                { name: 'New York Red Bulls', image: '/static/images/North America/New York Red Bulls.svg', cost: 5981 },
                { name: 'Seattle Sounders FC', image: '/static/images/North America/Seattle Sounders FC.svg', cost: 8302 },
                { name: 'Atlanta United FC', image: '/static/images/North America/Atlanta United FC.svg', cost: 4736 },
                { name: 'DC United', image: '/static/images/North America/DC United.svg', cost: 1895 },
                { name: 'FC Dallas', image: '/static/images/North America/FC Dallas.svg', cost: 6248 },
                { name: 'Los Angeles FC', image: '/static/images/North America/Los Angeles FC.svg', cost: 9573 },
                { name: 'Minnesota United FC', image: '/static/images/North America/Minnesota United FC.svg', cost: 3741 },
                { name: 'Nashville SC', image: '/static/images/North America/Nashville SC.svg', cost: 7109 },
                { name: 'Orlando City SC', image: '/static/images/North America/Orlando City SC.svg', cost: 5624 },
                { name: 'Philadelphia Union', image: '/static/images/North America/Philadelphia Union.svg', cost: 8937 },
                { name: 'Portland Timbers', image: '/static/images/North America/Portland Timbers.svg', cost: 2483 },
                { name: 'San Jose Earthquakes', image: '/static/images/North America/San Jose Earthquakes.svg', cost: 6795 },
                { name: 'Club America', image: '/static/images/North America/Club America.svg', cost: 4128 },
                { name: 'Cruz Azul', image: '/static/images/North America/Cruz Azul.svg', cost: 9361 },
                { name: 'Chivas Guadalajara', image: '/static/images/North America/Chivas Guadalajara.svg', cost: 1574 },
                { name: 'Monterrey', image: '/static/images/North America/Monterrey.svg', cost: 7846 },
                { name: 'Necaxa', image: '/static/images/North America/Necaxa.svg', cost: 3259 },
                { name: 'Pachuca', image: '/static/images/North America/Pachuca.svg', cost: 5917 },
                { name: 'Pumas UNAM', image: '/static/images/North America/Pumas UNAM.svg', cost: 8432 },
                { name: 'Tigres UANL', image: '/static/images/North America/Tigres UANL.svg', cost: 2695 },
                { name: 'Toluca', image: '/static/images/North America/Toluca.svg', cost: 6183 }
            ];

            const southAmericaClubs = [
                { name: 'Santos FC', image: '/static/images/South America/Santos FC.svg', cost: 4729 },
                { name: 'Club Libertad', image: '/static/images/South America/Club Libertad.svg', cost: 8156 },
                { name: 'Boca Juniors', image: '/static/images/South America/Boca Juniors.svg', cost: 3847 },
                { name: 'River Plate', image: '/static/images/South America/River Plate.svg', cost: 9235 },
                { name: 'Colo-Colo', image: '/static/images/South America/Colo-Colo.svg', cost: 1692 },
                { name: 'Independiente', image: '/static/images/South America/Independiente.svg', cost: 7384 },
                { name: 'Flamengo', image: '/static/images/South America/Flamengo.svg', cost: 5921 },
                { name: 'Palmeiras', image: '/static/images/South America/Palmeiras.svg', cost: 2468 },
                { name: 'Nacional', image: '/static/images/South America/Nacional.svg', cost: 8739 },
                { name: 'Peñarol', image: '/static/images/South America/Peñarol.svg', cost: 6175 },
                { name: 'São Paulo FC', image: '/static/images/South America/São Paulo FC.svg', cost: 3592 },
                { name: 'Cruzeiro EC', image: '/static/images/South America/Cruzeiro EC.svg', cost: 9814 },
                { name: 'Grêmio FBPA', image: '/static/images/South America/Gremio FPBA.svg', cost: 1357 },
                { name: 'Internacional', image: '/static/images/South America/Internacional.svg', cost: 7629 },
                { name: 'Estudiantes de La Plata', image: '/static/images/South America/Estudiantes de La Plata.svg', cost: 4981 },
                { name: 'Racing Club', image: '/static/images/South America/Racing Club.svg', cost: 2845 },
                { name: 'Olimpia', image: '/static/images/South America/Olimpia.svg', cost: 6237 },
                { name: 'Cerro Porteño', image: '/static/images/South America/Cerro Porteño.svg', cost: 9473 },
                { name: 'Universidad de Chile', image: '/static/images/South America/Universidad de Chile.svg', cost: 5168 },
                { name: 'Universitario', image: '/static/images/South America/Universitario.svg', cost: 3726 },
                { name: 'Alianza Lima', image: '/static/images/South America/Alianza Lima.svg', cost: 8294 },
                { name: 'The Strongest', image: '/static/images/South America/The Strongest.svg', cost: 1985 },
                { name: 'Club Bolívar', image: '/static/images/South America/Club Bolivar.svg', cost: 7542 },
                { name: 'Emelec', image: '/static/images/South America/Emelec.svg', cost: 4619 },
                { name: 'LDU Quito', image: '/static/images/South America/LDU Quito.svg', cost: 9137 }
            ];

            const europeClubs = [
                { name: 'FC Barcelona', image: '/static/images/Europe/FC Barcelona.svg', cost: 8756 },
                { name: 'Real Madrid CF', image: '/static/images/Europe/Real Madrid CF.svg', cost: 3214 },
                { name: 'Manchester United FC', image: '/static/images/Europe/Manchester United FC.svg', cost: 6879 },
                { name: 'Bayern Munich', image: '/static/images/Europe/Bayern Munich.svg', cost: 9543 },
                { name: 'Paris Saint-Germain FC', image: '/static/images/Europe/Paris Saint-Germain FC.svg', cost: 2167 },
                { name: 'Liverpool FC', image: '/static/images/Europe/Liverpool FC.svg', cost: 7395 },
                { name: 'Chelsea FC', image: '/static/images/Europe/Chelsea FC.svg', cost: 4628 },
                { name: 'Arsenal FC', image: '/static/images/Europe/Arsenal FC.svg', cost: 1952 },
                { name: 'AC Milan', image: '/static/images/Europe/AC Milan.svg', cost: 8374 },
                { name: 'Inter Milan', image: '/static/images/Europe/Inter Milan.svg', cost: 5719 },
                { name: 'Juventus FC', image: '/static/images/Europe/Juventus FC.svg', cost: 3846 },
                { name: 'Borussia Dortmund', image: '/static/images/Europe/Borussia Dortmund.svg', cost: 9281 },
                { name: 'Atletico Madrid', image: '/static/images/Europe/Atletico Madrid.svg', cost: 6537 },
                { name: 'Manchester City FC', image: '/static/images/Europe/Manchester City FC.svg', cost: 1794 },
                { name: 'Tottenham Hotspur FC', image: '/static/images/Europe/Tottenham Hotspur FC.svg', cost: 7928 },
                { name: 'Napoli', image: '/static/images/Europe/Napoli.svg', cost: 4165 },
                { name: 'AS Roma', image: '/static/images/Europe/AS Roma.svg', cost: 2639 },
                { name: 'FC Porto', image: '/static/images/Europe/FC Porto.svg', cost: 8492 },
                { name: 'Benfica', image: '/static/images/Europe/Benfica.svg', cost: 5316 },
                { name: 'Ajax Amsterdam', image: '/static/images/Europe/Ajax Amsterdam.svg', cost: 3784 }
            ];

            const asiaClubs = [
                { name: 'Al-Hilal SFC', image: '/static/images/Asia/Al-Hilal SFC.svg', cost: 6921 },
                { name: 'Al-Ain FC', image: '/static/images/Asia/Al-Ain FC.svg', cost: 4378 },
                { name: 'Persepolis FC', image: '/static/images/Asia/Persepolis FC.svg', cost: 1835 },
                { name: 'Al-Sadd SC', image: '/static/images/Asia/Al-Sadd SC.svg', cost: 9267 },
                { name: 'Urawa Red Diamonds', image: '/static/images/Asia/Urawa Red Diamonds.svg', cost: 7594 },
                { name: 'Jeonbuk Hyundai Motors FC', image: '/static/images/Asia/Jeonbuk Hyundai Motors FC.svg', cost: 3142 },
                { name: 'Guangzhou Evergrande FC', image: '/static/images/Asia/Guangzhou Evergrande FC.svg', cost: 5786 },
                { name: 'Al-Nassr FC', image: '/static/images/Asia/Al-Nassr FC.svg', cost: 2419 },
                { name: 'FC Tokyo', image: '/static/images/Asia/FC Tokyo.svg', cost: 8653 },
                { name: 'Al-Jazira Club', image: '/static/images/Asia/Al-Jazira Club.svg', cost: 6297 },
                { name: 'Esteghlal FC', image: '/static/images/Asia/Esteghlal FC.svg', cost: 4731 },
                { name: 'Sepahan FC', image: '/static/images/Asia/Sepahan FC.svg', cost: 1968 },
                { name: 'Al-Rayyan SC', image: '/static/images/Asia/Al-Rayyan SC.svg', cost: 9384 },
                { name: 'Al-Wahda FC', image: '/static/images/Asia/Al-Wahda FC.svg', cost: 7126 },
                { name: 'Shanghai SIPG FC', image: '/static/images/Asia/Shanghai SIPG FC.svg', cost: 3579 },
                { name: 'Jeju United FC', image: '/static/images/Asia/Jeju United FC.svg', cost: 5842 },
                { name: 'FC Seoul', image: '/static/images/Asia/FC Seoul.svg', cost: 2317 },
                { name: 'Suwon Samsung Bluewings', image: '/static/images/Asia/Suwon Samsung Bluewings.svg', cost: 8795 },
                { name: 'Al-Ittihad FC', image: '/static/images/Asia/Al-Ittihad FC.svg', cost: 6534 },
                { name: 'Al-Ahli SC', image: '/static/images/Asia/Al-Ahli SC.svg', cost: 4189 }
            ];

            const africaClubs = [
                { name: 'Al-Ahly SC', image: '/static/images/Africa/Al-Ahly SC.svg', cost: 7863 },
                { name: 'Esperance de Tunis', image: '/static/images/Africa/Esperance de Tunis.svg', cost: 3529 },
                { name: 'Kaizer Chiefs FC', image: '/static/images/Africa/Kaizer Chiefs FC.svg', cost: 9176 },
                { name: 'Mamelodi Sundowns FC', image: '/static/images/Africa/Mamelodi Sundowns FC.svg', cost: 5742 },
                { name: 'Wydad AC', image: '/static/images/Africa/Wydad AC.svg', cost: 1985 },
                { name: 'TP Mazembe', image: '/static/images/Africa/TP Mazembe.svg', cost: 8324 },
                { name: 'ES Setif', image: '/static/images/Africa/ES Setif.svg', cost: 4697 },
                { name: 'Al-Hilal Omdurman', image: '/static/images/Africa/Al-Hilal Omdurman.svg', cost: 2153 },
                { name: 'Zamalek SC', image: '/static/images/Africa/Zamalek SC.svg', cost: 6918 },
                { name: 'Orlando Pirates FC', image: '/static/images/Africa/Orlando Pirates FC.svg', cost: 9485 },
                { name: 'Asante Kotoko SC', image: '/static/images/Africa/Asante Kotoko SC.svg', cost: 3762 },
                { name: 'JS Kabylie', image: '/static/images/Africa/JS Kabylie.svg', cost: 7239 },
                { name: 'CS Sfaxien', image: '/static/images/Africa/CS Sfaxien.svg', cost: 5814 },
                { name: 'ASEC Mimosas', image: '/static/images/Africa/ASEC Mimosas.svg', cost: 1397 },
                { name: 'Club Africain', image: '/static/images/Africa/Club Africain.svg', cost: 8652 },
                { name: 'Al-Merrikh SC', image: '/static/images/Africa/Al-Merrikh SC.svg', cost: 4129 },
                { name: 'Enyimba FC', image: '/static/images/Africa/Enyimba FC.svg', cost: 6573 },
                { name: 'Raja CA', image: '/static/images/Africa/Raja CA.svg', cost: 2946 },
                { name: 'Cotonsport FC', image: '/static/images/Africa/Cotonsport FC.svg', cost: 9381 },
                { name: 'Horoya AC', image: '/static/images/Africa/Horoya AC.svg', cost: 5729 }
            ];

            const oceaniaClubs = [
                { name: 'Sydney FC', image: '/static/images/Oceania/Sydney FC.svg', cost: 8246 },
                { name: 'Wellington Phoenix FC', image: '/static/images/Oceania/Wellington Phoenix FC.svg', cost: 3917 },
                { name: 'Melbourne Victory FC', image: '/static/images/Oceania/Melbourne Victory FC.svg', cost: 6582 },
                { name: 'Perth Glory FC', image: '/static/images/Oceania/Perth Glory FC.svg', cost: 1735 },
                { name: 'Auckland City FC', image: '/static/images/Oceania/Auckland City FC.svg', cost: 9463 },
                { name: 'Team Wellington', image: '/static/images/Oceania/Team Wellington.svg', cost: 4129 },
                { name: 'Hobart Zebras FC', image: '/static/images/Oceania/Hobart Zebras FC.svg', cost: 7894 },
                { name: 'Canberra United FC', image: '/static/images/Oceania/Canberra United FC.svg', cost: 2651 },
                { name: 'Brisbane Roar FC', image: '/static/images/Oceania/Brisbane Roar FC.svg', cost: 5378 },
                { name: 'Central Coast Mariners FC', image: '/static/images/Oceania/Central Coast Mariners FC.svg', cost: 8742 },
                { name: 'Tasmania United FC', image: '/static/images/Oceania/Tasmania United FC.svg', cost: 3196 },
                { name: 'Waitakere United FC', image: '/static/images/Oceania/Waitakere United FC.svg', cost: 6957 },
                { name: 'Eastern Suburbs AFC', image: '/static/images/Oceania/Eastern Suburbs AFC.svg', cost: 1584 },
                { name: 'South Melbourne FC', image: '/static/images/Oceania/South Melbourne FC.svg', cost: 9325 },
                { name: 'Heidelberg United FC', image: '/static/images/Oceania/Heidelberg United FC.svg', cost: 4768 },
                { name: 'Oakleigh Cannons FC', image: '/static/images/Oceania/Oakleigh Cannons FC.svg', cost: 7139 },
                { name: 'Lae City Dwellers FC', image: '/static/images/Oceania/Lae City Dwellers FC.svg', cost: 2873 },
                { name: 'Hekari United FC', image: '/static/images/Oceania/Hekari United FC.svg', cost: 5621 },
                { name: 'Tafea FC', image: '/static/images/Oceania/Tafea FC.svg', cost: 8497 },
                { name: 'Amicale FC', image: '/static/images/Oceania/Amicale FC.svg', cost: 3942 }
            ];

            tabs.forEach(tab => {
                tab.addEventListener('click', (event) => {
                    event.preventDefault();
                    tabs.forEach(t => t.classList.remove('active'));
                    tab.classList.add('active');

                    const targetId = tab.id.replace('Tab', 'Content');
                    const targetIndex = Array.from(tabs).indexOf(tab);
                    tabSlider.style.transform = `translateX(-${targetIndex * 100}%)`;

                    // Generar rectángulos según la pestaña activa
                    switch (targetId) {
                        case 'northAmericaContent':
                            generateRectangles('northAmericaContent', northAmericaClubs, levels);
                            break;
                        case 'southAmericaContent':
                            generateRectangles('southAmericaContent', southAmericaClubs, levels);
                            break;
                        case 'europeContent':
                            generateRectangles('europeContent', europeClubs, levels);
                            break;
                        case 'asiaContent':
                            generateRectangles('asiaContent', asiaClubs, levels);
                            break;
                        case 'africaContent':
                            generateRectangles('africaContent', africaClubs, levels);
                            break;
                        case 'oceaniaContent':
                            generateRectangles('oceaniaContent', oceaniaClubs, levels);
                            break;
                    }
                });
            });

            // Generar rectángulos iniciales para la pestaña activa por defecto
            generateRectangles('northAmericaContent', northAmericaClubs, levels);

            tg.onEvent('backButtonClicked', () => {
                window.location.href = 'index.html';
            });

            tg.BackButton.show();

            let startX = 0;
            let endX = 0;
            let currentIndex = 0;

            tabSlider.addEventListener('touchstart', (event) => {
                startX = event.touches[0].clientX;
            });

            tabSlider.addEventListener('touchmove', (event) => {
                endX = event.touches[0].clientX;
            });

            tabSlider.addEventListener('touchend', () => {
                const deltaX = endX - startX;
                const threshold = 50; // Umbral para considerar un deslizamiento

                if (Math.abs(deltaX) > threshold) {
                    let newIndex = currentIndex;
                    if (deltaX > 0 && currentIndex > 0) {
                        // Deslizamiento hacia la izquierda (anterior pestaña)
                        newIndex--;
                    } else if (deltaX < 0 && currentIndex < tabs.length - 1) {
                        // Deslizamiento hacia la derecha (siguiente pestaña)
                        newIndex++;
                    }
                    
                    // Solo actualizamos si el índice ha cambiado
                    if (newIndex !== currentIndex) {
                        currentIndex = newIndex;
                        tabs[currentIndex].click();
                    }
                }
            });
        });

        async function updateMineLevel(user_id, club_id, level) {
            const response = await fetch('/update_mine_level', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_id, club_id, level })
            });
            return await response.json();
        }
        
        let currentActionButtonListener = null;

        async function showAlert(club) {
            const currentScore = parseFloat(document.getElementById('score').textContent);
            const cost = club.cost;
            const costColor = cost <= currentScore ? 'yellow' : 'gray';
            const buttonClass = cost <= currentScore ? 'active' : 'inactive';

            document.getElementById('alertIcon').innerHTML = `<img src="${club.image}" alt="${club.name}" style="width: 50%; height: 50%;">`;
            document.getElementById('alertText').innerText = club.name;
            document.getElementById('alertSubtitle').innerText = 'Profit per hour';
            document.getElementById('alertSecondSubtitle').innerText = 'Cost';
            document.getElementById('alertCost').innerHTML = `<p><iconify-icon icon="twemoji:coin" style="font-size: 35px;"></iconify-icon> ${cost}</p>`;
            document.getElementById('alertCost').classList.remove('yellow', 'gray');
            document.getElementById('alertCost').classList.add(costColor);
            document.getElementById('actionButton').classList.remove('active', 'inactive');
            document.getElementById('actionButton').classList.add(buttonClass);
            document.getElementById('alertMenu').style.display = 'block';
            document.querySelector('.container').classList.add('blur-content');
            document.querySelector('.navbar').classList.add('blur-content');

            // Eliminar el evento anterior si existe
            if (currentActionButtonListener) {
                document.getElementById('actionButton').removeEventListener('click', currentActionButtonListener);
            }

            // Asignar un nuevo evento
            currentActionButtonListener = async () => {
                
                const club_id = club.name;
                const currentLevel = levels[club_id] || 1;
                const newLevel = currentLevel + 1;
                if (currentScore >= cost) {
                    score = currentScore - cost;
                    result = await updateMineLevel(user_id, club_id, newLevel);
                    if (result.status === 'success') {
                        document.getElementById('score').innerText = score.toFixed(3);
                        closeAlertMenu();
                    } else {
                        alert('Error al actualizar el score');
                    }
                } else {
                    alert('No tienes suficientes monedas para comprar este boost');
                }
            };

            document.getElementById('actionButton').addEventListener('click', currentActionButtonListener);
        }

        function closeAlertMenu() {
            document.getElementById('alertMenu').style.display = 'none';
            document.querySelector('.container').classList.remove('blur-content');
            document.querySelector('.navbar').classList.remove('blur-content');

            // Eliminar el evento del botón "Buy" al cerrar la alerta
            if (currentActionButtonListener) {
                document.getElementById('actionButton').removeEventListener('click', currentActionButtonListener);
                currentActionButtonListener = null;
            }
        }
    </script>
</body>
</html>

app.py:
import os
from flask import Flask, jsonify, request, render_template
from db import SessionLocal  # Importa SessionLocal desde db.py
from models import Base, Counter, Referral, MineLevels
from datetime import datetime, timezone
import json
import logging

app = Flask(__name__, template_folder='.')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/friends.html')
def serve_friends():
    return render_template('friends.html')

@app.route('/mine.html')
def mine():
    return render_template('mine.html')

@app.route('/boosts.html')
def serve_boosts():
    return render_template('boosts.html')

@app.route('/get_counters', methods=['GET'])
def get_counters():
    user_id = request.args.get('user_id')
    startParam = request.args.get('startParam')
    name = request.args.get('name')
    username = request.args.get('username')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        db = SessionLocal()
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            counter = Counter(user_id=user_id, name=name, username=username, score=0.0, secondarycount=0, tap=1, energy_limit=1000, recharge_speed=1, profit_per_hour=0)
            db.add(counter)
            db.commit()

            # Crear la tabla referrals para el nuevo usuario
            referral = Referral(user_id=user_id, name=name, from_user=startParam, referrals_count=0, referrals_name='', referrals_id=None)
            db.add(referral)
            db.commit()
        
            # Incrementar el número de referidos
            if startParam.isdigit():
                referrer = db.query(Referral).filter_by(user_id=startParam).first()
                if referrer:
                    referrer.referrals_count += 1
                    if referrer.referrals_name:
                        referrer.referrals_name += f', {name}'
                    else:
                        referrer.referrals_name = name
                    if referrer.referrals_id:
                        referrer.referrals_id += f', {user_id}'
                    else:
                        referrer.referrals_id = user_id
                    db.commit()

                referrer_counter = db.query(Counter).filter_by(user_id=int(startParam)).first()
                referrer_counter.score += 100
                db.commit()

        return jsonify({
            'score': round(counter.score, 3),  # Redondear a 3 decimales
            'secondarycount': counter.secondarycount,
            'timestamp': counter.timestamp.replace(tzinfo=timezone.utc).isoformat(),  # Convertir a ISO 8601 con UTC
            'tap': counter.tap,
            'energy_limit': counter.energy_limit,
            'recharge_speed': counter.recharge_speed,
            'profit_per_hour': counter.profit_per_hour
        })
    except Exception as e:
        logging.error(f"Error in get_counters: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@app.route('/update_counters', methods=['POST'])
def update_counters():
    data = request.get_json()
    user_id = data.get('user_id')
    score = data.get('score')
    secondarycount = data.get('secondarycount')

    if not user_id or score is None:
        return jsonify({'error': 'user_id, score are required'}), 400

    try:
        db = SessionLocal()
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            counter = Counter(user_id=user_id, score=score, secondarycount=secondarycount, timestamp=datetime.utcnow())
            db.add(counter)
        else:
            counter.score = score
            counter.timestamp = datetime.utcnow()
            if secondarycount is not None:
                counter.secondarycount = secondarycount
        db.commit()
        return jsonify({'status': 'success'})
    
    except Exception as e:
        logging.error(f"Error in update_counters: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@app.route('/get_referrals', methods=['GET'])
def get_referrals():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        db = SessionLocal()
        referral = db.query(Referral).filter_by(user_id=user_id).first()
        if not referral:
            return jsonify({'referrals_count': 0, 'referrals_name': '', 'referrals_score': '', 'referrals_username': ''})

        referrals_id = referral.referrals_id.split(', ') if referral.referrals_id else []
        referrals_name = referral.referrals_name.split(', ') if referral.referrals_name else []
        referrals_score = []
        referrals_username = []

        for ref_id in referrals_id:
            counter = db.query(Counter).filter_by(user_id=int(ref_id)).first()
            if counter:
                referrals_score.append(str(counter.score))
                referrals_username.append(str(counter.username))
            else:
                referrals_score.append('0')
                referrals_username.append('0')

        return jsonify({
            'referrals_count': referral.referrals_count,
            'referrals_name': ', '.join(referrals_name),
            'referrals_score': ', '.join(referrals_score),
            'referrals_username': ', '.join(referrals_username)
        })
    except Exception as e:
        logging.error(f"Error in get_referrals: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        db = SessionLocal()
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'score': counter.score,
            'tap': counter.tap,
            'energy_limit': counter.energy_limit,
            'recharge_speed': counter.recharge_speed
        })
    except Exception as e:
        logging.error(f"Error in get_user_data: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@app.route('/update_boost', methods=['POST'])
def update_boost():
    data = request.get_json()
    user_id = data.get('user_id')
    score = data.get('score')
    boost_type = data.get('boost_type')
    cost = data.get('cost')

    if not all([user_id, score, boost_type, cost]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        db = SessionLocal()
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            return jsonify({'error': 'User not found'}), 404

        counter.score = score
        if boost_type == 'multitap':
            counter.tap += 1
        elif boost_type == 'energy_limit':
            counter.energy_limit = (counter.energy_limit or 1000) + 500
        elif boost_type == 'recharge_speed':
            counter.recharge_speed = (counter.recharge_speed or 1) + 1

        db.commit()
        return jsonify({'status': 'success'})
    
    except Exception as e:
        logging.error(f"Error in update_boost: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@app.route('/get_mine_levels', methods=['GET'])
def get_mine_levels():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        db = SessionLocal()
        mine_level = db.query(MineLevels).filter_by(user_id=user_id).first()
        if not mine_level:
            return jsonify({'clubs': {}})

        return jsonify({'clubs': mine_level.clubs})
    except Exception as e:
        logging.error(f"Error in get_mine_levels: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@app.route('/update_mine_level', methods=['POST'])
def update_mine_level_route():
    data = request.get_json()
    user_id = data.get('user_id')
    club_id = data.get('club_id')
    level = data.get('level')

    if not all([user_id, club_id, level]):
        return jsonify({'error': 'Missing required fields'}), 400

    result = update_mine_level(user_id, club_id, level)
    if result['status'] == 'success':
        return jsonify(result)
    else:
        return jsonify(result), 500

def update_mine_level(user_id, club_id, level):
    db = SessionLocal()
    try:
        mine_level = db.query(MineLevels).filter_by(user_id=user_id).first()

        if not mine_level:
            # Si no existe un registro para este user_id, crea uno nuevo
            mine_level = MineLevels(user_id=user_id, clubs={club_id: level})
            db.add(mine_level)
        else:
            # Si el club ya existe, actualiza su nivel
            clubs = mine_level.clubs
            clubs[club_id] = level
            mine_level.clubs = clubs

        db.commit()
        return {'status': 'success'}
    except Exception as e:
        db.rollback()
        return {'error': str(e)}
    finally:
        db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

models.py:


db.py:


migrate.py:


migration_script.py:


Pero tengo un error al guardar un nuevo elemento en la columna 'clubs' de la tabla 'mine_levels'. El primer elemento lo guarda correctamente, pero al ya haber un elemento dentro de la columna 'clubs' e intentar agregar un nuevo 'club_id' o aumentar el valor del 'club_id' ya existente en la columna 'clubs', éste no hace nada