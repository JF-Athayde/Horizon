// ================================
// ELEMENTOS
// ================================
const toggle = document.getElementById("menu-toggle");
const menu = document.getElementById("main-nav");
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
document.querySelectorAll(".main-nav a").forEach(link => {
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
// JOB SEARCH AND FILTER
// ================================
const jobSearchInput = document.getElementById('job-search');
const searchBtn = document.getElementById('search-btn');
const jobList = document.getElementById('job-list');
const jobItems = document.querySelectorAll('.job-item');
const filterTags = document.querySelectorAll('.filter-tag');
const advancedFilterBtn = document.getElementById('advanced-filter-btn');
const advancedFilters = document.getElementById('advanced-filters');
const applyFiltersBtn = document.getElementById('apply-filters-btn');
const minSalaryInput = document.getElementById('min-salary');
const maxSalaryInput = document.getElementById('max-salary');
const contractRadios = document.getElementsByName('contract');
const experienceLevelSelect = document.getElementById('experience-level');
const locationFilterSelect = document.getElementById('location-filter');

let currentFilter = 'all';
let minSalary = 0;
let maxSalary = Infinity;
let contractType = 'all';
let experienceLevel = 'all';
let locationFilter = 'all';

// Search functionality
function performSearch() {
    const searchTerm = jobSearchInput.value.toLowerCase().trim();
    
    let visibleCount = 0;
    jobItems.forEach(item => {
        const title = item.querySelector('h4').textContent.toLowerCase();
        const company = item.querySelector('.company').textContent.toLowerCase();
        const description = item.querySelector('.description').textContent.toLowerCase();
        const location = item.querySelector('.location').textContent.toLowerCase();
        const salaryText = item.querySelector('.salary').textContent;
        const salaryMatch = salaryText.match(/R\$ (\d+(?:\.\d+)?) - R\$ (\d+(?:\.\d+)?)/);
        const itemMinSalary = salaryMatch ? parseFloat(salaryMatch[1].replace('.', '')) : 0;
        const itemMaxSalary = salaryMatch ? parseFloat(salaryMatch[2].replace('.', '')) : Infinity;
        
        const matchesSearch = !searchTerm || 
            title.includes(searchTerm) || 
            company.includes(searchTerm) || 
            description.includes(searchTerm) || 
            location.includes(searchTerm);
        
        const matchesCategory = currentFilter === 'all' || item.dataset.category === currentFilter;
        
        const matchesSalary = (itemMinSalary >= minSalary && itemMaxSalary <= maxSalary) || 
                              (itemMaxSalary >= minSalary && itemMinSalary <= maxSalary);
        
        const matchesContract = contractType === 'all' || 
            (contractType === 'full-time' && description.includes('integral')) ||
            (contractType === 'part-time' && description.includes('meio')) ||
            (contractType === 'freelance' && description.includes('freelance'));
        
        const matchesExperience = experienceLevel === 'all' || 
            (experienceLevel === 'junior' && (description.includes('júnior') || description.includes('junior'))) ||
            (experienceLevel === 'pleno' && description.includes('pleno')) ||
            (experienceLevel === 'senior' && description.includes('sênior'));
        
        const matchesLocation = locationFilter === 'all' || 
            (locationFilter === 'remoto' && location.includes('remoto')) ||
            (locationFilter === 'presencial' && !location.includes('remoto') && !location.includes('híbrido')) ||
            (locationFilter === 'hibrido' && location.includes('híbrido'));
        
        if (matchesSearch && matchesCategory && matchesSalary && matchesContract && matchesExperience && matchesLocation) {
            item.style.display = 'block';
            visibleCount++;
        } else {
            item.style.display = 'none';
        }
    });
    
    // Update job count
    const jobCountEl = document.getElementById('job-count');
    if (jobCountEl) {
        jobCountEl.textContent = `(${visibleCount})`;
    }
}

// Filter functionality
function applyFilter(filter) {
    currentFilter = filter;
    
    // Update active filter tag
    filterTags.forEach(tag => {
        if (tag.dataset.filter === filter) {
            tag.classList.add('active');
        } else {
            tag.classList.remove('active');
        }
    });
    
    performSearch();
}

// Apply advanced filters
function applyAdvancedFilters() {
    minSalary = parseFloat(minSalaryInput.value) || 0;
    maxSalary = parseFloat(maxSalaryInput.value) || Infinity;
    
    contractRadios.forEach(radio => {
        if (radio.checked) {
            contractType = radio.value;
        }
    });
    
    experienceLevel = experienceLevelSelect.value;
    locationFilter = locationFilterSelect.value;
    
    performSearch();
}

// Toggle advanced filters
function toggleAdvancedFilters() {
    if (advancedFilters.style.display === 'none') {
        advancedFilters.style.display = 'block';
    } else {
        advancedFilters.style.display = 'none';
    }
}

// Initialize intelligent filtering on page load
document.addEventListener('DOMContentLoaded', () => {
    performSearch(); // Initial display
    
    // Event listeners
    if (jobSearchInput) {
        jobSearchInput.addEventListener('input', performSearch);
    }

    if (searchBtn) {
        searchBtn.addEventListener('click', performSearch);
    }

    filterTags.forEach(tag => {
        tag.addEventListener('click', () => {
            applyFilter(tag.dataset.filter);
        });
    });

    if (advancedFilterBtn) {
        advancedFilterBtn.addEventListener('click', toggleAdvancedFilters);
    }

    if (applyFiltersBtn) {
        applyFiltersBtn.addEventListener('click', applyAdvancedFilters);
    }
});

// ================================
// DEBUG (opcional)
// ================================
// console.log("Script carregado com sucesso 🚀");
