document.addEventListener('DOMContentLoaded', function() {
    const themeButton = document.getElementById('theme-button');
    const currentTheme = localStorage.getItem('theme') || 'light';

    if (currentTheme === 'dark') {
        document.body.classList.add('dark');
    }

    if (themeButton) {
        themeButton.addEventListener('click', () => {
            document.body.classList.toggle('dark');
            let theme = 'light';
            if (document.body.classList.contains('dark')) {
                theme = 'dark';
            }
            localStorage.setItem('theme', theme);
        });
    }
});
