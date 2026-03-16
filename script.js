const seasonStatus = document.getElementById("season-status");
const yearEl = document.getElementById("year");
const form = document.querySelector(".contact-form");
const formStatus = document.querySelector(".form-status");
const navToggle = document.querySelector(".nav-toggle");
const mainNav = document.querySelector(".main-nav");

const seasonMessages = [
  { months: [11, 0, 1], message: "furnace safety checks" }, // Dec-Feb
  { months: [2, 3], message: "automotive diagnostics" }, // Mar-Apr
  { months: [4, 5, 6], message: "AC prep & repair" }, // May-Jul
  { months: [7, 8], message: "mixed HVAC + auto" }, // Aug-Sep
  { months: [9, 10], message: "fall maintenance" }, // Oct-Nov
];

function updateSeasonStatus() {
  const now = new Date();
  const month = now.getMonth();
  const match = seasonMessages.find((entry) => entry.months.includes(month));
  if (match && seasonStatus) {
    seasonStatus.innerHTML = `Currently prioritizing <strong>${match.message}</strong>`;
  }
}

function updateYear() {
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }
}

function handleFormSubmit(event) {
  event.preventDefault();
  if (formStatus) {
    formStatus.textContent = "Submitting...";
  }

  setTimeout(() => {
    if (formStatus) {
      formStatus.textContent = "Thanks! I'll be in touch within 24 hours.";
    }
    form?.reset();
  }, 800);
}

function initNavToggle() {
  if (!navToggle || !mainNav) return;
  navToggle.addEventListener("click", () => {
    const isOpen = mainNav.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  mainNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      if (mainNav.classList.contains("is-open")) {
        mainNav.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
      }
    });
  });
}

updateSeasonStatus();
updateYear();
initNavToggle();
form?.addEventListener("submit", handleFormSubmit);
