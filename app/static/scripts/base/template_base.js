document.addEventListener("DOMContentLoaded", function () {
  const toggleAsideBtn = document.getElementById("boton-mostrar-menu");
  const aside = document.querySelector("aside");
  const closeMenuBtn = document.getElementById("boton-cerrar-menu");

  // Event listener para el botón de mostrar menú
  toggleAsideBtn.addEventListener("click", function () {
    aside.style.transform = "translateY(0)";
  });

  // Event listener para el botón de cerrar menú
  closeMenuBtn.addEventListener("click", function () {
    aside.style.transform = "translateY(-100%)";
  });

  // Function to set the theme mode
  function setThemeMode(mode) {
    document.body.setAttribute("data-bs-theme", mode);
    localStorage.setItem("theme", mode);
  }

  // Function to toggle between light and dark modes
  function toggleTheme() {
    const currentMode = document.body.getAttribute("data-bs-theme");
    const newMode = currentMode === "light" ? "dark" : "light";
    setThemeMode(newMode);
  }

  // Event listener for the button to toggle menu visibility
  const btnClaro = document.querySelector(".modo-claro");
  const btnOscuro = document.querySelector(".modo-oscuro");

  btnClaro.addEventListener("click", function () {
    setThemeMode("light");
    btnClaro.classList.add("active");
    btnOscuro.classList.remove("active");
  });

  btnOscuro.addEventListener("click", function () {
    setThemeMode("dark");
    btnClaro.classList.remove("active");
    btnOscuro.classList.add("active");
  });

  // Check if there's a stored theme preference
  const storedTheme = localStorage.getItem("theme");
  if (storedTheme) {
    setThemeMode(storedTheme);
    if (storedTheme === "dark") {
      btnOscuro.classList.add("active");
    } else {
      btnClaro.classList.add("active");
    }
  } else {
    // Detect system preference and set the theme accordingly
    const prefersDarkMode =
      window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches;
    setThemeMode(prefersDarkMode ? "dark" : "light");

    if (prefersDarkMode) {
      btnOscuro.classList.add("active");
    } else {
      btnClaro.classList.add("active");
    }
  }
});
