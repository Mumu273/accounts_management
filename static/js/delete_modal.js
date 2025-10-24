document.addEventListener("DOMContentLoaded", function() {
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteForm = document.getElementById("deleteForm");

    document.querySelectorAll(".btn-delete").forEach(button => {
        button.addEventListener("click", function(e) {
            e.preventDefault(); // prevent default link click

            const url = this.dataset.url; // get URL from data-url
            deleteForm.action = url; // set form action dynamically

            deleteModal.show(); // open modal
        });
    });
});