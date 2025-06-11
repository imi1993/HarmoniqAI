// popup services
const services = document.querySelectorAll('.service');
const popups = document.querySelectorAll('.popup');
const overlay = document.getElementById('overlay');

services.forEach(service => {
    service.addEventListener('click', () => {
        const key = service.dataset.service;
        const popup = document.querySelector(`.popup[data-service="${key}"]`);
        if (popup) {
            popup.style.display = 'block';
            overlay.style.display = 'block';
        }
    });
});

overlay.addEventListener('click', () => {
    popups.forEach(p => p.style.display = 'none');
    overlay.style.display = 'none';
});

// ROI calculator
const roiForm = document.getElementById('roi-form');
const roiResult = document.getElementById('roi-result');

roiForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const hours = parseFloat(document.getElementById('roi-hours').value) || 0;
    const rate = parseFloat(document.getElementById('roi-rate').value) || 0;
    const people = parseInt(document.getElementById('roi-people').value) || 1;
    const monthly = hours * rate * people * 4;
    const yearly = monthly * 12;
    let pack = 'Zen';
    if (monthly > 2000) pack = 'Harmonie';
    else if (monthly > 800) pack = 'Sérénité';
    roiResult.textContent = `Économie potentielle : ${yearly.toFixed(0)}€ par an. Pack recommandé : ${pack}`;
});

// needs analyzer
const needsForm = document.getElementById('needs-form');
const needsResult = document.getElementById('needs-result');

needsForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const tasks = parseInt(document.getElementById('need-tasks').value) || 0;
    const budget = parseFloat(document.getElementById('need-budget').value) || 0;
    let pack = 'Zen';
    if (tasks > 5 && budget >= 1000) pack = 'Harmonie';
    else if (tasks > 2 && budget >= 500) pack = 'Sérénité';
    const sector = document.getElementById('need-sector').value;
    needsResult.textContent = `Secteur: ${sector}. Pack conseillé: ${pack}.`; 
});
