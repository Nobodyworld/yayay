document.addEventListener("DOMContentLoaded", function() {
    const filterButton = document.getElementById('filter-button');
    if (filterButton) {
        filterButton.addEventListener('click', function() {
            const endpoint = '/api/update-feed/';
            const data = {
                'filter': document.getElementById('filter').value
            };
            fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('feed-container').innerHTML = data.html;
            })
            .catch(error => console.error('Error:', error));
        });
    }
});
