const overlay = document.createElement("div");
overlay.className = "iframe-overlay";
document.body.appendChild(overlay);

fetch("header.html")
  .then(res => res.text())
  .then(data => {
    document.getElementById("navbar").innerHTML = data;

    const hamburger = document.getElementById("hamburger");
    const navLinks = document.getElementById("nav-links");

    const toggleMenu = () => {
      navLinks.classList.toggle("show");
      overlay.style.display = navLinks.classList.contains("show") ? "block" : "none";
    };

    hamburger.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleMenu();
    });

    overlay.addEventListener("click", () => {
      navLinks.classList.remove("show");
      overlay.style.display = "none";
    });

    navLinks.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
        navLinks.classList.remove("show");
        overlay.style.display = "none";
      });
    });
  });
