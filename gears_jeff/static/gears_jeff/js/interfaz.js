document.addEventListener("DOMContentLoaded", () => {
    const elementos = document.querySelectorAll(
        ".modulo, .transmision-contenido, .transmision-imagen"
    );

    if (!("IntersectionObserver" in window)) {
        elementos.forEach(elemento => {
            elemento.classList.add("visible");
        });
        return;
    }

    elementos.forEach(elemento => {
        elemento.classList.add("animar-entrada");
    });

    const observador = new IntersectionObserver((entradas, observer) => {
        entradas.forEach(entrada => {
            if (entrada.isIntersecting) {
                entrada.target.classList.add("visible");
                observer.unobserve(entrada.target);
            }
        });
    }, {
        threshold: 0.12
    });

    elementos.forEach(elemento => observador.observe(elemento));
});
