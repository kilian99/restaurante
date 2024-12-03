// static/js/scripts.js

// Script para navbar
document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) { // Cambia después de 50px de desplazamiento
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });
});

// Script para carrusel
document.addEventListener("DOMContentLoaded", function () {
    var carrusel = document.getElementById('carruselRestaurante');

    // Pausar el carrusel al pasar el mouse
    carrusel.addEventListener('mouseenter', function () {
        var carouselInstance = bootstrap.Carousel.getInstance(carrusel);
        if (carouselInstance) carouselInstance.pause();
    });

    // Reanudar el carrusel al salir el mouse
    carrusel.addEventListener('mouseleave', function () {
        var carouselInstance = bootstrap.Carousel.getInstance(carrusel);
        if (carouselInstance) carouselInstance.cycle();
    });

    // Opcional: Configuración personalizada
    new bootstrap.Carousel(carrusel, {
        interval: 3000, // Cambiar imágenes cada 3 segundos
        ride: 'carousel' // Inicia automáticamente
    });
});

// Script para imagen arriba navbar
document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled'); // Añade la clase cuando bajas
        } else {
            navbar.classList.remove('scrolled'); // La quita al volver arriba
        }
    });
});

// Desplazamiento
document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('.menu-index .nav-link');

    links.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Ajuste para compensar el espacio del índice fijo
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Confeti reserva
confetti({
    particleCount: 150,
    spread: 70,
    origin: { y: 0.6 },
});

