// ================================
// ELEMENTOS
// ================================
const toggle = document.getElementById("menu-toggle");
const menu = document.getElementById("menu");
const overlay = document.getElementById("menu-overlay");
const progressBar = document.getElementById("progress-bar");


// ================================
// MENU SANDUÍCHE
// ================================
function openMenu() {
    if (menu) menu.classList.add("active");
    if (overlay) overlay.classList.add("active");
    if (toggle) toggle.classList.add("active");
}

function closeMenu() {
    if (menu) menu.classList.remove("active");
    if (overlay) overlay.classList.remove("active");
    if (toggle) toggle.classList.remove("active");
}

function toggleMenu() {
    if (!menu) return;

    menu.classList.toggle("active");

    if (overlay) overlay.classList.toggle("active");
    if (toggle) toggle.classList.toggle("active");
}

// Clique no botão
if (toggle) {
    toggle.addEventListener("click", toggleMenu);
}

// Clique fora (overlay)
if (overlay) {
    overlay.addEventListener("click", closeMenu);
}

// Fechar ao clicar em links
document.querySelectorAll(".menu a").forEach(link => {
    link.addEventListener("click", closeMenu);
});


// ================================
// FECHAR COM ESC
// ================================
document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
        closeMenu();
    }
});


// ================================
// BARRA DE PROGRESSO
// ================================
function updateProgressBar() {
    if (!progressBar) return;

    const scroll = document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;

    const progress = (scroll / height) * 100;
    progressBar.style.width = progress + "%";
}

window.addEventListener("scroll", updateProgressBar);


// ================================
// SCROLL SUAVE (MELHORADO)
// ================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        const targetId = this.getAttribute("href");

        if (targetId.length > 1) {
            e.preventDefault();

            const target = document.querySelector(targetId);

            if (target) {
                const offset = 90; // evita ficar escondido atrás do header
                const top = target.offsetTop - offset;

                window.scrollTo({
                    top: top,
                    behavior: "smooth"
                });
            }
        }
    });
});


// ================================
// DEBUG (opcional)
// ================================
// console.log("Script carregado com sucesso 🚀");

// ================================
// MVP INTERATIVO
// ================================
const recordVideoBtn = document.getElementById('record-video');
const videoPreview = document.getElementById('video-preview');
const runDiagnosisBtn = document.getElementById('run-diagnosis');
const addProjectBtn = document.getElementById('add-project');
const scoreValue = document.getElementById('score-value');

function changeScore(newScore) {
    if (!scoreValue) return;
    scoreValue.textContent = `${newScore}%`;
}

if (recordVideoBtn) {
    recordVideoBtn.addEventListener('click', () => {
        const confirmation = window.confirm('Simulação: gravar vídeo de apresentação de 60–90s?');
        if (!confirmation) return;
        videoPreview.textContent = 'Vídeo de apresentação salvo! Pronto para envio às instituições.';
        changeScore(78);
        alert('Vídeo registrado no perfil. Boa!');
    });
}

if (runDiagnosisBtn) {
    runDiagnosisBtn.addEventListener('click', () => {
        runDiagnosisBtn.textContent = 'Diagnóstico em andamento...';
        runDiagnosisBtn.disabled = true;
        setTimeout(() => {
            runDiagnosisBtn.textContent = 'Executar Diagnóstico';
            runDiagnosisBtn.disabled = false;
            changeScore(82);
            alert('Diagnóstico concluído. Adicione 1 projeto com ODS ou atualize sua nota de inglês para ascender.');
        }, 1100);
    });
}

if (addProjectBtn) {
    addProjectBtn.addEventListener('click', () => {
        const projectName = prompt('Nome do projeto (ex: Plataforma de Educação Social):');
        if (!projectName) return;

        const projectContainer = document.createElement('div');
        projectContainer.className = 'project';
        projectContainer.innerHTML = `
            <h4>${projectName}</h4>
            <p>Problema: Coloque aqui o problema que você resolveu.</p>
            <p>Solução: Explique brevemente como foi implementado.</p>
            <p>Impacto: Adapte essa métrica à realidade do projeto.</p>
            <p>Score de Impacto: <strong>84</strong></p>
        `;

        const portfolioCard = document.querySelector('.section-portfolio');
        if (portfolioCard) {
            portfolioCard.insertBefore(projectContainer, addProjectBtn);
        }

        alert(`Projeto "${projectName}" adicionado ao portfólio com score inicial e geração de impacto.`);
        changeScore(88);

        const globalScoreEl = document.getElementById('global-score');
        if (globalScoreEl) {
            globalScoreEl.textContent = '88%';
        }

        const miniProgress = document.querySelector('.section-global-score .mini-progress span');
        if (miniProgress) {
            miniProgress.style.width = '88%';
        }
    });
}

const applyJobsBtn = document.getElementById('apply-jobs');
const applyRecommendedBtn = document.getElementById('apply-recommended');
const markODSMissionBtn = document.getElementById('mark-ODS');

if (applyJobsBtn) {
    applyJobsBtn.addEventListener('click', () => {
        alert('Candidatura iniciada (simulação): 3 vagas em aberto processadas.');
        changeScore(90);
    });
}

if (applyRecommendedBtn) {
    applyRecommendedBtn.addEventListener('click', () => {
        alert('Aplicando em oportunidades recomendadas... Concluído! Verifique sua caixa de mensagem.');
        changeScore(92);
    });
}

if (markODSMissionBtn) {
    markODSMissionBtn.addEventListener('click', () => {
        alert('Missão ODS concluída e marcada. Score de impacto aumentado.');
        changeScore(95);
        const readiness = document.getElementById('job-readiness');
        if (readiness) {
            readiness.textContent = '82%';
        }
    });
}

// ================================
// TABS FOR APPLYNOW
// ================================
const tabButtons = document.querySelectorAll('.tab-btn');
const tabPanes = document.querySelectorAll('.tab-pane');

tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        // Remove active from all buttons and panes
        tabButtons.forEach(b => b.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));

        // Add active to clicked button
        btn.classList.add('active');

        // Show corresponding pane
        const tabId = btn.dataset.tab;
        const pane = document.getElementById(tabId);
        if (pane) {
            pane.classList.add('active');
        }
    });
});

// ================================
// DEBUG (opcional)
// ================================
// console.log("Script carregado com sucesso 🚀");
