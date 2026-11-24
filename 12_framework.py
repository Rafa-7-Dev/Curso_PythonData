from flask import Flask, render_template

# Criação do app Flask
app = Flask(__name__)

# Rota para a pagina principal
@app.route('/sobre')
def sobre () :
    
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sobre | Rafael Lima</title>

    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    :root {
        --bg: #050b18;
        --blue: #168bff;
        --cyan: #48d9ff;
        --white: #f2f7ff;
        --muted: #91a4c2;
        --glass: rgba(16, 38, 70, .48);
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html { scroll-behavior: smooth; }

    body {
        font-family: 'DM Sans', sans-serif;
        background: var(--bg);
        color: var(--white);
        overflow-x: hidden;
    }

    body::before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 0;
        opacity: .15;
        background-image: radial-gradient(#6caeff .7px, transparent .7px);
        background-size: 35px 35px;
    }

    /* =================================
    BOLA DE FUTEVÔLEI INTERATIVA
    ================================= */

    .ball-reveal {
        position: fixed;
        width: min(650px, 85vw);
        aspect-ratio: 1;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        z-index: 1;
        pointer-events: none;
        opacity: .85;

        -webkit-mask-image: radial-gradient(
            circle 280px at var(--mx, 50%) var(--my, 50%),
            black 0%,
            rgba(0,0,0,.8) 35%,
            transparent 100%
        );

        mask-image: radial-gradient(
            circle 280px at var(--mx, 50%) var(--my, 50%),
            black 0%,
            rgba(0,0,0,.8) 35%,
            transparent 100%
        );

        transition: opacity .4s ease;
    }

    .ball-reveal svg {
        width: 100%;
        height: 100%;
        overflow: visible;
        filter: drop-shadow(0 0 12px rgba(42, 172, 255, .15));
    }

    .ball-reveal .ball-outline {
        fill: rgba(26, 130, 210, .025);
        stroke: rgba(66, 194, 255, .48);
        stroke-width: 1.5;
    }

    .ball-reveal .ball-panel {
        fill: rgba(37, 155, 230, .025);
        stroke: rgba(66, 194, 255, .35);
        stroke-width: 1.2;
    }

    .ball-reveal .ball-detail {
        fill: none;
        stroke: rgba(66, 194, 255, .27);
        stroke-width: 1;
    }

    .ball-reveal .ball-center {
        fill: rgba(30, 145, 230, .025);
        stroke: rgba(72, 217, 255, .4);
        stroke-width: 1.5;
    }

    /* Luz do mouse */

    .mouse-glow {
        position: fixed;
        width: 450px;
        height: 450px;
        border-radius: 50%;
        pointer-events: none;
        z-index: 2;
        background: radial-gradient(
            circle,
            rgba(0, 130, 255, .13),
            rgba(0, 130, 255, .04) 40%,
            transparent 70%
        );
        transform: translate(-50%, -50%);
    }

    /* Progresso */

    .progress-bar {
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        width: 0;
        background: linear-gradient(90deg, var(--blue), var(--cyan));
        z-index: 1000;
        box-shadow: 0 0 15px var(--cyan);
    }

    /* Navegação */

    nav {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: min(92%, 1050px);
        padding: 15px 25px;
        border: 1px solid rgba(120,180,255,.15);
        border-radius: 18px;
        background: rgba(5,15,32,.78);
        backdrop-filter: blur(20px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 100;
    }

    .logo {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 19px;
        font-weight: 700;
    }

    .logo span { color: var(--cyan); }

    nav a {
        color: var(--muted);
        text-decoration: none;
        font-size: 13px;
        margin-left: 23px;
        transition: .3s;
    }

    nav a:hover { color: var(--cyan); }

    /* Estrutura */

    .container {
        width: min(1100px, 88%);
        margin: auto;
        position: relative;
        z-index: 3;
    }

    .section {
        padding: 110px 0;
        position: relative;
        z-index: 3;
    }

    .section-label {
        color: var(--cyan);
        text-transform: uppercase;
        letter-spacing: 4px;
        font-size: 11px;
        font-weight: 800;
        margin-bottom: 18px;
        display: inline-block;
    }

    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(32px, 5vw, 48px);
        line-height: 1.15;
        letter-spacing: -2px;
        margin-bottom: 25px;
    }

    .gradient {
        background: linear-gradient(100deg,#fff,#56baff,#36e0ff);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }

    /* HERO */

    .hero {
        min-height: 100vh;
        display: flex;
        align-items: center;
        position: relative;
        padding: 150px 0 100px;
        overflow: hidden;
        z-index: 3;
    }

    .hero::before {
        content: "";
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle,rgba(0,104,255,.17),transparent 70%);
        right: -150px;
        top: 10%;
        animation: pulse 6s infinite alternate;
    }

    .hero-content { max-width: 850px; }

    .availability {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        border: 1px solid rgba(58,220,255,.25);
        background: rgba(29,159,255,.08);
        border-radius: 50px;
        padding: 10px 17px;
        font-size: 12px;
        color: #a6eaff;
        margin-bottom: 30px;
    }

    .availability-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #39e6a0;
        box-shadow: 0 0 12px #39e6a0;
        animation: blink 1.5s infinite;
    }

    .hero h1 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(55px,9vw,100px);
        letter-spacing: -6px;
        line-height: .98;
        margin-bottom: 28px;
        animation: fadeUp 1s .15s both;
    }

    .hero h1 span { display: block; }

    .hero-description {
        color: var(--muted);
        font-size: 17px;
        line-height: 1.9;
        max-width: 650px;
        animation: fadeUp 1s .3s both;
    }

    .hero-description strong { color: #e7f5ff; }

    .hero-buttons {
        display: flex;
        gap: 15px;
        margin-top: 35px;
        flex-wrap: wrap;
        animation: fadeUp 1s .45s both;
    }

    .btn {
        padding: 15px 25px;
        border-radius: 12px;
        text-decoration: none;
        font-size: 13px;
        font-weight: 700;
        transition: .35s;
        display: inline-flex;
        align-items: center;
        gap: 10px;
    }

    .btn-primary {
        color: white;
        background: linear-gradient(110deg,#0876ed,#08a9ed);
        box-shadow: 0 8px 30px rgba(0,130,255,.2);
    }

    .btn-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0,160,255,.4);
    }

    .btn-secondary {
        color: #c3d9f5;
        border: 1px solid rgba(150,190,255,.2);
        background: rgba(255,255,255,.025);
    }

    .btn-secondary:hover {
        border-color: var(--cyan);
        color: var(--cyan);
        transform: translateY(-5px);
    }

    .hero-bottom {
        position: absolute;
        bottom: 35px;
        left: 50%;
        transform: translateX(-50%);
        color: #536b8b;
        font-size: 10px;
        letter-spacing: 3px;
        animation: float 2s infinite;
    }

    /* SOBRE */

    .about-grid {
        display: grid;
        grid-template-columns: 1.2fr .8fr;
        gap: 55px;
        align-items: center;
    }

    .about-text {
        color: var(--muted);
        font-size: 15px;
        line-height: 2;
    }

    .about-text p { margin-bottom: 18px; }
    .about-text strong { color: #e4f2ff; }

    .quote-card {
        padding: 40px 30px;
        border-radius: 22px;
        background: linear-gradient(145deg,rgba(17,65,119,.4),rgba(8,22,43,.7));
        border: 1px solid rgba(79,172,255,.18);
        position: relative;
        overflow: hidden;
        transition: .4s;
    }

    .quote-card:hover {
        transform: translateY(-8px);
        border-color: rgba(72,217,255,.5);
    }

    .quote-symbol {
        font-family: Georgia,serif;
        font-size: 75px;
        line-height: .8;
        color: var(--cyan);
        opacity: .7;
    }

    .quote-card p {
        font-family: 'Space Grotesk',sans-serif;
        font-size: 23px;
        line-height: 1.5;
        margin: 20px 0;
    }

    .quote-card small {
        color: var(--muted);
        letter-spacing: 2px;
        font-size: 10px;
        text-transform: uppercase;
    }

    /* CARDS */

    .cards-grid {
        display: grid;
        grid-template-columns: repeat(3,1fr);
        gap: 20px;
        margin-top: 45px;
    }

    .info-card {
        padding: 30px;
        background: var(--glass);
        border: 1px solid rgba(125,178,255,.12);
        border-radius: 18px;
        transition: transform .4s,background .4s,border-color .4s,box-shadow .4s;
        position: relative;
        overflow: hidden;
    }

    .info-card::before {
        content: "";
        position: absolute;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg,transparent,var(--cyan),transparent);
        top: 0;
        left: -100%;
        transition: .6s;
    }

    .info-card:hover::before { left: 100%; }

    .info-card:hover {
        transform: translateY(-9px);
        background: rgba(20,58,99,.6);
        border-color: rgba(72,217,255,.35);
        box-shadow: 0 15px 40px rgba(0,80,180,.12);
    }

    .card-icon {
        font-size: 30px;
        margin-bottom: 23px;
        display: block;
    }

    .info-card h3 {
        font-family: 'Space Grotesk',sans-serif;
        font-size: 19px;
        margin-bottom: 13px;
    }

    .info-card p {
        font-size: 13px;
        line-height: 1.8;
        color: var(--muted);
    }

    /* TECNOLOGIAS */

    .tech-section {
        background: linear-gradient(180deg,transparent,rgba(10,42,79,.35),transparent);
    }

    .tech-list {
        display: flex;
        flex-wrap: wrap;
        gap: 13px;
        margin-top: 35px;
    }

    .tech-item {
        border: 1px solid rgba(100,170,255,.18);
        background: rgba(22,66,117,.22);
        color: #c2dcfa;
        padding: 15px 22px;
        border-radius: 12px;
        font-size: 13px;
        transition: .3s;
    }

    .tech-item:hover {
        background: rgba(0,140,255,.15);
        border-color: var(--cyan);
        color: white;
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(0,150,255,.12);
    }

    /* TRAJETÓRIA */

    .timeline {
        margin-top: 45px;
        border-left: 1px solid rgba(72,180,255,.3);
        padding-left: 35px;
    }

    .timeline-item {
        position: relative;
        padding-bottom: 38px;
    }

    .timeline-item::before {
        content: "";
        position: absolute;
        width: 11px;
        height: 11px;
        background: var(--cyan);
        border-radius: 50%;
        left: -41px;
        top: 5px;
        box-shadow: 0 0 15px rgba(72,217,255,.7);
    }

    .timeline-item h3 {
        font-family: 'Space Grotesk',sans-serif;
        font-size: 19px;
        margin-bottom: 10px;
    }

    .timeline-item p {
        color: var(--muted);
        font-size: 14px;
        line-height: 1.8;
        max-width: 650px;
    }

    .timeline-tag {
        display: inline-block;
        font-size: 10px;
        color: var(--cyan);
        margin-bottom: 10px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* PROJETOS */

    .project-card {
        margin-top: 35px;
        padding: 35px;
        border-radius: 20px;
        background: linear-gradient(120deg,rgba(12,50,91,.7),rgba(7,20,39,.8));
        border: 1px solid rgba(89,168,255,.18);
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 25px;
        transition: .4s;
    }

    .project-card:hover {
        transform: scale(1.015);
        border-color: var(--cyan);
    }

    .project-card h3 {
        font-family: 'Space Grotesk',sans-serif;
        font-size: 23px;
        margin-bottom: 10px;
    }

    .project-card p {
        color: var(--muted);
        font-size: 13px;
        line-height: 1.8;
    }

    .project-link {
        color: var(--cyan);
        font-size: 25px;
        text-decoration: none;
        transition: .3s;
    }

    .project-link:hover { transform: translateX(7px); }

    /* CONTATO */

    .contact {
        text-align: center;
        padding: 120px 0;
        background: radial-gradient(ellipse at center,rgba(0,104,255,.13),transparent 65%);
        position: relative;
        z-index: 3;
    }

    .contact h2 {
        font-family: 'Space Grotesk',sans-serif;
        font-size: clamp(35px,6vw,65px);
        letter-spacing: -3px;
        margin-bottom: 20px;
    }

    .contact p {
        color: var(--muted);
        font-size: 15px;
        line-height: 1.8;
        max-width: 600px;
        margin: 0 auto 35px;
    }

    /* FOOTER */

    footer {
        padding: 30px 5%;
        border-top: 1px solid rgba(120,180,255,.12);
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
        flex-wrap: wrap;
        color: #637895;
        font-size: 11px;
        position: relative;
        z-index: 3;
    }

    footer a {
        color: var(--cyan);
        text-decoration: none;
    }

    /* =================================
    ANIMAÇÕES DE ROLAGEM
    ================================= */

    .reveal {
        opacity: 0;
        transform: translateY(55px);
        filter: blur(5px);
        transition:
            opacity .9s ease,
            transform .9s cubic-bezier(.16,1,.3,1),
            filter .9s ease;
    }

    .reveal.active {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }

    .reveal-left {
        opacity: 0;
        transform: translateX(-65px);
        transition: all 1s cubic-bezier(.16,1,.3,1);
    }

    .reveal-left.active {
        opacity: 1;
        transform: translateX(0);
    }

    .reveal-right {
        opacity: 0;
        transform: translateX(65px);
        transition: all 1s cubic-bezier(.16,1,.3,1);
    }

    .reveal-right.active {
        opacity: 1;
        transform: translateX(0);
    }

    .reveal-scale {
        opacity: 0;
        transform: scale(.88);
        filter: blur(4px);
        transition: all .9s cubic-bezier(.16,1,.3,1);
    }

    .reveal-scale.active {
        opacity: 1;
        transform: scale(1);
        filter: blur(0);
    }

    /* ANIMAÇÕES GERAIS */

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(35px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulse {
        from { transform: scale(.9); opacity: .5; }
        to { transform: scale(1.2); opacity: 1; }
    }

    @keyframes blink {
        50% { opacity: .3; }
    }

    @keyframes float {
        50% { transform: translate(-50%,-10px); }
    }

    /* RESPONSIVIDADE */

    @media(max-width:800px) {
        .about-grid { grid-template-columns: 1fr; gap: 30px; }
        .cards-grid { grid-template-columns: repeat(2,1fr); }
        .hero h1 { letter-spacing: -3px; }
        .ball-reveal { width: 85vw; }
    }

    @media(max-width:550px) {
        nav { padding: 14px 17px; }
        nav a { margin-left: 10px; font-size: 11px; }
        nav a:first-child { display: none; }
        .cards-grid { grid-template-columns: 1fr; }
        .section { padding: 80px 0; }
        .project-card { align-items: flex-start; padding: 25px; }
        .hero { min-height: 95vh; }
        .hero-description { font-size: 15px; }
        footer { justify-content: center; text-align: center; }
        .ball-reveal { width: 100vw; }
        .mouse-glow { display: none; }
    }

    @media(prefers-reduced-motion:reduce) {
        *,*::before,*::after {
            scroll-behavior: auto !important;
            animation-duration: .01ms !important;
            transition-duration: .01ms !important;
        }
        .reveal,.reveal-left,.reveal-right,.reveal-scale {
            opacity: 1;
            transform: none;
            filter: none;
        }
    }
    </style>
    </head>

    <body>

    <div class="progress-bar" id="progressBar"></div>

    <!-- BOLA VAZADA REVELADA PELA LUZ DO MOUSE -->

    <div class="ball-reveal" id="ballReveal">
        <svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">

            <circle class="ball-outline" cx="250" cy="250" r="210"/>

            <!-- Painel superior -->
            <path class="ball-panel"
                d="M250 40
                C310 65 370 85 425 145
                L320 205
                L250 155
                L180 205
                L75 145
                C130 85 190 65 250 40Z"/>

            <!-- Painel esquerdo -->
            <path class="ball-panel"
                d="M75 145
                L180 205
                L155 315
                L55 370
                C20 290 25 205 75 145Z"/>

            <!-- Painel direito -->
            <path class="ball-panel"
                d="M425 145
                L320 205
                L345 315
                L445 370
                C480 290 475 205 425 145Z"/>

            <!-- Painel central -->
            <path class="ball-center"
                d="M180 205
                L250 155
                L320 205
                L345 315
                L250 375
                L155 315Z"/>

            <!-- Painel inferior esquerdo -->
            <path class="ball-panel"
                d="M55 370
                L155 315
                L250 375
                L225 455
                C145 445 85 415 55 370Z"/>

            <!-- Painel inferior direito -->
            <path class="ball-panel"
                d="M345 315
                L445 370
                C415 415 355 445 275 455
                L250 375Z"/>

            <!-- Linhas internas -->
            <path class="ball-detail"
                d="M250 40 L250 155
                M75 145 L180 205
                M425 145 L320 205
                M55 370 L155 315
                M445 370 L345 315
                M250 375 L250 455"/>

            <path class="ball-detail"
                d="M180 205 L250 250 L320 205
                M155 315 L250 250 L345 315
                M250 250 L250 375"/>

            <circle class="ball-detail" cx="250" cy="250" r="155"/>
        </svg>
    </div>

    <div class="mouse-glow" id="mouseGlow"></div>

    <nav>
        <div class="logo">RAFAEL<span>.</span></div>
        <div>
            <a href="#inicio">Início</a>
            <a href="#sobre">Sobre</a>
            <a href="#habilidades">Habilidades</a>
            <a href="#projetos">Projetos</a>
        </div>
    </nav>

    <!-- HERO -->

    <header class="hero" id="inicio">
        <div class="container">
            <div class="hero-content">

                <div class="availability">
                    <span class="availability-dot"></span>
                    TECNOLOGIA • DADOS • NEGÓCIOS
                </div>

                <h1>
                    Olá, eu sou
                    <span class="gradient">Rafael Lima.</span>
                </h1>

                <p class="hero-description">
                    Profissional da área de <strong>vendas</strong>,
                    entusiasta de <strong>tecnologia, programação e inovação</strong>.
                    Construindo uma trajetória que conecta o universo comercial
                    ao poder dos dados e da automação.
                </p>

                <div class="hero-buttons">
                    <a href="#sobre" class="btn btn-primary">
                        Conheça minha história ↓
                    </a>

                    <a href="https://github.com/Rafa-7-Dev"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="btn btn-secondary">
                        ↗ Meu GitHub
                    </a>
                </div>
            </div>
        </div>

        <div class="hero-bottom">SCROLL PARA EXPLORAR ↓</div>
    </header>

    <!-- SOBRE -->

    <section class="section" id="sobre">
        <div class="container">
            <div class="about-grid">

                <div class="reveal-left">
                    <span class="section-label">01 / QUEM SOU EU</span>

                    <h2 class="section-title">
                        Mais do que aprender tecnologia,
                        <span class="gradient">quero transformar possibilidades em resultados.</span>
                    </h2>

                    <div class="about-text">
                        <p>
                            Sou Rafael Lima, profissional da área comercial,
                            apaixonado por vendas, tecnologia, dados e inovação.
                        </p>

                        <p>
                            Minha experiência no universo comercial despertou
                            meu interesse por encontrar maneiras mais inteligentes
                            de trabalhar, analisar informações e resolver problemas.
                        </p>

                        <p>
                            Atualmente, estou finalizando minha formação em
                            <strong>Python Completo</strong> e desenvolvendo projetos
                            que conectam programação, análise de dados e estratégias
                            comerciais.
                        </p>

                        <p>
                            Acredito que a tecnologia não deve existir apenas
                            para impressionar, mas principalmente para simplificar
                            processos, gerar oportunidades e entregar resultados reais.
                        </p>
                    </div>
                </div>

                <div class="quote-card reveal-right">
                    <div class="quote-symbol">“</div>
                    <p>
                        Transformando dados em decisões
                        e ideias em soluções.
                    </p>
                    <small>Minha forma de enxergar o futuro</small>
                </div>

            </div>
        </div>
    </section>

    <!-- HABILIDADES -->

    <section class="section" id="habilidades">
        <div class="container">

            <div class="reveal">
                <span class="section-label">02 / MEU UNIVERSO</span>

                <h2 class="section-title">
                    Onde meus interesses <span class="gradient">se encontram.</span>
                </h2>

                <p class="about-text">
                    Acredito na combinação de diferentes conhecimentos para
                    desenvolver soluções melhores e enxergar oportunidades
                    que muitas vezes passam despercebidas.
                </p>
            </div>

            <div class="cards-grid">

                <div class="info-card reveal">
                    <span class="card-icon">📈</span>
                    <h3>Vendas & Estratégia</h3>
                    <p>
                        Visão comercial, relacionamento com clientes,
                        identificação de oportunidades e busca constante
                        por melhores resultados.
                    </p>
                </div>

                <div class="info-card reveal">
                    <span class="card-icon">🐍</span>
                    <h3>Programação</h3>
                    <p>
                        Desenvolvimento em Python, construção de aplicações,
                        lógica de programação e resolução de problemas
                        através do código.
                    </p>
                </div>

                <div class="info-card reveal">
                    <span class="card-icon">📊</span>
                    <h3>Análise de Dados</h3>
                    <p>
                        Interesse em transformar informações em conhecimento,
                        identificar padrões e apoiar decisões mais inteligentes.
                    </p>
                </div>

                <div class="info-card reveal">
                    <span class="card-icon">⚙️</span>
                    <h3>Automação</h3>
                    <p>
                        Busca por processos mais eficientes, redução de tarefas
                        repetitivas e soluções que economizem tempo.
                    </p>
                </div>

                <div class="info-card reveal">
                    <span class="card-icon">💡</span>
                    <h3>Empreendedorismo</h3>
                    <p>
                        Transformação de ideias em projetos, identificação
                        de oportunidades e desenvolvimento de soluções
                        com potencial de negócio.
                    </p>
                </div>

                <div class="info-card reveal">
                    <span class="card-icon">🚀</span>
                    <h3>Aprendizado Contínuo</h3>
                    <p>
                        Evolução constante, curiosidade e disposição para
                        explorar novas ferramentas, tecnologias e possibilidades.
                    </p>
                </div>

            </div>
        </div>
    </section>

    <!-- TECNOLOGIAS -->

    <section class="section tech-section">
        <div class="container">

            <div class="reveal">
                <span class="section-label">03 / TECNOLOGIAS</span>

                <h2 class="section-title">
                    Ferramentas que estou <span class="gradient">explorando.</span>
                </h2>

                <p class="about-text">
                    Estou construindo minha base técnica e aprofundando
                    conhecimentos em tecnologias que permitem desenvolver
                    aplicações, trabalhar com informações e automatizar processos.
                </p>
            </div>

            <div class="tech-list reveal">
                <div class="tech-item">🐍 Python</div>
                <div class="tech-item">🗄️ SQL</div>
                <div class="tech-item">📊 Análise de Dados</div>
                <div class="tech-item">⚙️ Automação</div>
                <div class="tech-item">🌐 HTML</div>
                <div class="tech-item">🎨 CSS</div>
                <div class="tech-item">⚡ JavaScript</div>
                <div class="tech-item">🧠 Lógica de Programação</div>
            </div>

        </div>
    </section>

    <!-- TRAJETÓRIA -->

    <section class="section">
        <div class="container">

            <div class="reveal">
                <span class="section-label">04 / MINHA JORNADA</span>

                <h2 class="section-title">
                    Uma trajetória de <span class="gradient">evolução.</span>
                </h2>
            </div>

            <div class="timeline">

                <div class="timeline-item reveal-left">
                    <span class="timeline-tag">Experiência profissional</span>
                    <h3>O universo comercial</h3>
                    <p>
                        Desenvolvimento de conhecimentos e experiências
                        na área de vendas, compreendendo a importância
                        da estratégia, do relacionamento e dos resultados.
                    </p>
                </div>

                <div class="timeline-item reveal-left">
                    <span class="timeline-tag">Transição de conhecimentos</span>
                    <h3>A conexão com a tecnologia</h3>
                    <p>
                        O interesse por tecnologia e inovação abriu novas
                        possibilidades de aprendizado, especialmente na
                        aplicação da programação para resolver problemas reais.
                    </p>
                </div>

                <div class="timeline-item reveal-left">
                    <span class="timeline-tag">Em desenvolvimento</span>
                    <h3>Formação em Python</h3>
                    <p>
                        Aprofundamento em lógica de programação, Python,
                        SQL, análise de dados e automação, com desenvolvimento
                        de projetos práticos.
                    </p>
                </div>

                <div class="timeline-item reveal-left">
                    <span class="timeline-tag">Próximos passos</span>
                    <h3>Construindo novas possibilidades</h3>
                    <p>
                        Desenvolver soluções cada vez mais completas,
                        unir tecnologia e visão comercial e transformar
                        conhecimento em projetos que gerem valor.
                    </p>
                </div>

            </div>
        </div>
    </section>

    <!-- PROJETOS -->

    <section class="section" id="projetos">
        <div class="container">

            <div class="reveal">
                <span class="section-label">05 / MEU TRABALHO</span>

                <h2 class="section-title">
                    Ideias que começam a ganhar <span class="gradient">forma.</span>
                </h2>

                <p class="about-text">
                    Acredito que conhecimento só ganha força quando colocado
                    em prática. No meu GitHub compartilho minha evolução,
                    estudos e projetos desenvolvidos durante minha jornada.
                </p>
            </div>

            <div class="project-card reveal-scale">
                <div>
                    <h3>GitHub | Rafa-7-Dev</h3>
                    <p>
                        Um espaço dedicado ao aprendizado, experimentação
                        e desenvolvimento de projetos envolvendo programação,
                        tecnologia e soluções práticas.
                    </p>
                    <p style="margin-top:15px;color:#54caff;">
                        Python • Estudos • Desenvolvimento • Projetos
                    </p>
                </div>

                <a href="https://github.com/Rafa-7-Dev"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link">↗</a>
            </div>

            <div class="project-card reveal-scale">
                <div>
                    <h3>Minha evolução em Python</h3>
                    <p>
                        Estudos e exercícios de programação, explorando
                        conceitos fundamentais e construindo uma base
                        sólida para projetos cada vez mais complexos.
                    </p>
                </div>

                <a href="https://github.com/Rafa-7-Dev"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link">↗</a>
            </div>

        </div>
    </section>

    <!-- CONTATO -->

    <section class="contact">
        <div class="container reveal-scale">

            <span class="section-label">06 / VAMOS CONECTAR?</span>

            <h2>
                O próximo projeto pode
                <span class="gradient">começar com uma ideia.</span>
            </h2>

            <p>
                Estou sempre aberto a aprender, trocar experiências,
                conhecer projetos interessantes e descobrir novas
                oportunidades de conectar tecnologia e negócios.
            </p>

            <a href="https://github.com/Rafa-7-Dev"
            target="_blank"
            rel="noopener noreferrer"
            class="btn btn-primary">
                Conheça meu GitHub ↗
            </a>

        </div>
    </section>

    <footer>
        <div>
            <span class="logo">RAFAEL<span>.</span></span>
            <p style="margin-top:7px;">Tecnologia, dados e novas possibilidades.</p>
        </div>

        <div>Desenvolvido com dedicação por Rafael Lima © 2026</div>

        <div>
            <a href="https://github.com/Rafa-7-Dev"
            target="_blank"
            rel="noopener noreferrer">
                GITHUB ↗
            </a>
        </div>
    </footer>

    <script>

    /* =================================
    LUZ DO MOUSE + BOLA
    ================================= */

    const glow = document.getElementById('mouseGlow');
    const ball = document.getElementById('ballReveal');

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;

    document.addEventListener('mousemove', (event) => {

        mouseX = event.clientX;
        mouseY = event.clientY;

        glow.style.left = mouseX + 'px';
        glow.style.top = mouseY + 'px';

        // Converte a posição do mouse para coordenadas
        // relativas à bola fixa na tela.

        const ballRect = ball.getBoundingClientRect();

        const relativeX = ((mouseX - ballRect.left) / ballRect.width) * 100;
        const relativeY = ((mouseY - ballRect.top) / ballRect.height) * 100;

        ball.style.setProperty('--mx', relativeX + '%');
        ball.style.setProperty('--my', relativeY + '%');
    });

    /* =================================
    BARRA DE PROGRESSO
    ================================= */

    function updateProgress() {

        const scrollTop = window.scrollY;

        const documentHeight =
            document.documentElement.scrollHeight - window.innerHeight;

        const progress = documentHeight > 0
            ? (scrollTop / documentHeight) * 100
            : 0;

        document.getElementById('progressBar').style.width =
            progress + '%';
    }

    window.addEventListener('scroll', updateProgress, { passive: true });

    /* =================================
    ANIMAÇÕES DE ENTRADA NA ROLAGEM
    ================================= */

    const observer = new IntersectionObserver((entries) => {

        entries.forEach((entry) => {

            if (entry.isIntersecting) {

                entry.target.classList.add('active');

                observer.unobserve(entry.target);

            }

        });

    }, {
        threshold: 0.12,
        rootMargin: '0px 0px -35px 0px'
    });

    document.querySelectorAll(
        '.reveal, .reveal-left, .reveal-right, .reveal-scale'
    ).forEach((element, index) => {

        element.style.transitionDelay =
            (index % 3) * 100 + 'ms';

        observer.observe(element);

    });

    /* =================================
    EFEITO 3D NOS CARDS
    ================================= */

    document.querySelectorAll('.info-card').forEach((card) => {

        card.addEventListener('mousemove', (event) => {

            if (window.innerWidth < 800) return;

            const rect = card.getBoundingClientRect();

            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = (centerY - y) / 35;
            const rotateY = (x - centerX) / 35;

            card.style.transform =
                `translateY(-9px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;

        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
        });

    });

    /* =================================
    NAVEGAÇÃO SUAVE
    ================================= */

    document.querySelectorAll('nav a[href^="#"]').forEach((link) => {

        link.addEventListener('click', (event) => {

            const target = document.querySelector(link.getAttribute('href'));

            if (!target) return;

            event.preventDefault();

            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });

        });

    });

    /* =================================
    MOVIMENTO SUAVE DA BOLA
    ================================= */

    let ballRotation = 0;

    function animateBall() {

        ballRotation += 0.0005;

        ball.style.transform =
            `translate(-50%, -50%) rotate(${Math.sin(ballRotation) * 3}deg)`;

        requestAnimationFrame(animateBall);
    }

    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        animateBall();
    }

    </script>

    </body>
    </html>
    """
# esse arroba (@) é um decorator
@app.route('/')
def home():
    return "<h1> Bem vindo a minha Super pagina! </h1>"

# rota com variaveis na url
@app.route('/ola/<nome>')
def saudacao(nome) : 
    return f"<h1> Seja bem vindo </h1> {nome}"

if __name__ == '__main__':
    app.run(debug=True)