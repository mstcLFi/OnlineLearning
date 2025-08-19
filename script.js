// Load the navbar dynamically
fetch("header.html")
  .then(res => res.text())
  .then(data => {
    document.getElementById("navbar").innerHTML = data;

    const hamburger = document.getElementById("hamburger");
    const navLinks = document.getElementById("nav-links");

    // Toggle menu when hamburger clicked
    hamburger.addEventListener("click", (e) => {
      e.stopPropagation(); // prevent click from bubbling up
      navLinks.classList.toggle("show");
    });

    // Close menu when clicking outside of it
    document.addEventListener("click", (e) => {
      if (navLinks.classList.contains("show") && 
          !navLinks.contains(e.target) && 
          !hamburger.contains(e.target)) {
        navLinks.classList.remove("show");
      }
    });

    // Optional: close menu when a link is clicked (mobile UX)
    navLinks.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
        navLinks.classList.remove("show");
      });
    });
  })
  .catch(err => console.error("Error loading header:", err));
