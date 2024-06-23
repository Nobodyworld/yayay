document.addEventListener('DOMContentLoaded', function() {
    const feedFilter = document.getElementById('feed-filter');
    const feedItems = document.querySelectorAll('.feed-item');

    if (feedFilter) {
        feedFilter.addEventListener('change', () => {
            const selectedValue = feedFilter.value;

            feedItems.forEach((item) => {
                if (selectedValue === 'all') {
                    item.style.display = 'block';
                } else {
                    if (item.dataset.category === selectedValue) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                }
            });
        });
    }
});
