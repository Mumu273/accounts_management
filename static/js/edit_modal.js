document.addEventListener("DOMContentLoaded", function () {
    const editModal = new bootstrap.Modal(document.getElementById("editCategoryModal"));
    const editModalBody = document.getElementById("editCategoryBody");
    const btnSaveEdit = document.getElementById("btnSaveEdit");

    // Open Edit Modal
    document.querySelectorAll(".btn-edit").forEach(btn => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            const url = this.getAttribute("data-url");

            fetch(url)
                .then(response => response.text())
                .then(html => {
                    editModalBody.innerHTML = html;
                    editModal.show();
                })
                .catch(error => console.error("Error loading edit form:", error));
        });
    });

    // Save Changes
    btnSaveEdit.addEventListener("click", function () {
        const form = editModalBody.querySelector("form");
        if (!form) return;

        const url = form.getAttribute("action");
        const formData = new FormData(form);

        fetch(url, {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
            },
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    editModal.hide();
                    location.reload(); // Reload table to reflect updates
                } else if (data.form_html) {
                    editModalBody.innerHTML = data.form_html;
                }
            })
            .catch(error => console.error("Error submitting edit form:", error));
    });
});
