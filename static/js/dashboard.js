// ---------------- Sidebar toggle ----------------
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const overlay = document.getElementById("overlay");
  const welcome = document.getElementById("welcome-text");

  sidebar.classList.toggle("show");
  overlay.classList.toggle("show");

  const sidebarWidth = 250; // must match .sidebar width
  if(sidebar.classList.contains("show")) {
    welcome.style.marginLeft = sidebarWidth + "px";
  } else {
    welcome.style.marginLeft = "0px";
  }
}

function closeSidebar() {
  const sidebar = document.getElementById("sidebar");
  const overlay = document.getElementById("overlay");
  const welcome = document.getElementById("welcome-text");

  sidebar.classList.remove("show");
  overlay.classList.remove("show");
  welcome.style.marginLeft = "0px";
}

// ---------------- Settings submenu toggle ----------------
document.addEventListener('DOMContentLoaded', function() {
  // Find all settings toggles (in case you add more)
  const toggles = document.querySelectorAll('.settings-toggle');

  toggles.forEach(function(toggle) {
    const parentItem = toggle.parentElement;

    toggle.addEventListener('click', function() {
      parentItem.classList.toggle('open'); // add/remove "open" class
    });
  });
});
