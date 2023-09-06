document.addEventListener("DOMContentLoaded", function() {
    const detailsLinks = document.querySelectorAll(".details a");
    const popup = document.createElement("div");
    popup.className = "popup";

    detailsLinks.forEach(function(detailsLink) {
        detailsLink.addEventListener("click", function(e) {
            e.preventDefault();
            const href = detailsLink.getAttribute("href");

            fetch(href) // Realiza una solicitud para obtener el contenido de la página referenciada
                .then(response => response.text())
                .then(content => {
                    popup.innerHTML = content;
                    document.body.appendChild(popup);
                    popup.style.display = "block";
                });
        });
    });

    popup.addEventListener("click", function() {
        popup.style.display = "none";
        popup.innerHTML = ""; // Limpia el contenido del popup
    });
});