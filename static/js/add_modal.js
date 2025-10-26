document.addEventListener("DOMContentLoaded", function() {
    const addBtn = document.getElementById("btnAddCategory");
    const modalBody = document.getElementById("addCategoryModalBody");
    const modal = new bootstrap.Modal(document.getElementById("addCategoryModal"));
    const spinner = document.getElementById("loadingSpinner");
    addBtn.addEventListener("click", function() {
        const url = this.getAttribute("data-url");
        spinner.style.display = "block";
        modalBody.innerHTML = "";
        modal.show();

        fetch(url)
            .then(response => response.text())
            .then(html => {
                modalBody.innerHTML = html;
                spinner.style.display = "none";

                // Add submit listener for AJAX form
                const form = modalBody.querySelector("form");
                if (form) {
                    form.addEventListener("submit", function(e) {
                        e.preventDefault();
                        const formData = new FormData(form);
                        fetch(form.action, {
                            method: "POST",
                            body: formData,
                            headers: { "X-Requested-With": "XMLHttpRequest" }
                        })
                        .then(resp => resp.json())
                        .then(data => {
                            if (data.success) {
                                location.reload(); // Reload to show new category
                            } else {
                                modalBody.innerHTML = data.form_html; // Reload form with errors
                            }
                        });
                    });
                }
            })
            .catch(() => {
                spinner.style.display = "none";
                modalBody.innerHTML = "<p class='text-danger text-center'>Failed to load form.</p>";
            });
    });
});
