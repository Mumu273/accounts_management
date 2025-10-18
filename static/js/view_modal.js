document.addEventListener('DOMContentLoaded', function() {
    const viewButtons = document.querySelectorAll('.btn-view');

    viewButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const url = this.dataset.url;

            fetch(url)
                .then(response => response.text())
                .then(html => {
                    // Remove existing modal if present
                    let existingModal = document.getElementById('viewCategoryModal');
                    if (existingModal) existingModal.remove();

                    // Insert new modal HTML
                    document.body.insertAdjacentHTML('beforeend', html);

                    // Show the modal
                    const modal = new bootstrap.Modal(document.getElementById('viewCategoryModal'));
                    modal.show();
                });
        });
    });
});
