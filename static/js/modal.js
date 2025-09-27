document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById("viewModal");
    const modalBody = document.getElementById("modal-body");
    const closeBtn = modal.querySelector(".close");

    document.querySelectorAll(".btn-view").forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const row = btn.closest('tr');
            const categoryId = row.dataset.id;
            const url = btn.dataset.url;
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    modalBody.innerHTML = '';
                    for (const key in data) {
                        modalBody.innerHTML += `
                            <div class="modal-field">
                                <strong>${key}:</strong>
                                <span>${data[key]}</span>
                            </div>
                        `;
                    }
                    modal.style.display = "block";
                })
                .catch(err => console.error('Fetch error:', err));
        });
    });

    closeBtn.onclick = () => modal.style.display = "none";
    window.onclick = event => { if (event.target == modal) modal.style.display = "none"; }
});