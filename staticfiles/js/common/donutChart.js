document.addEventListener('DOMContentLoaded', function() {
    const charts = document.querySelectorAll('.attribute-chart');

    function initializeChart(canvas) {
        const value = parseFloat(canvas.getAttribute('data-value'));
        if (isNaN(value)) {
            console.error('Invalid data-value attribute:', canvas.getAttribute('data-value'));
            return;
        }

        const ctx = canvas.getContext('2d');
        const chart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [value, 100 - value],
                    backgroundColor: ['#4CAF50', '#ddd'],
                }]
            },
            options: {
                circumference: Math.PI,
                rotation: -Math.PI,
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                tooltips: {
                    enabled: true
                }
            }
        });
    }

    if (charts.length) {
        charts.forEach(initializeChart);
    } else {
        console.log('No charts found to initialize.');
    }
});
