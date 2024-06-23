document.addEventListener('DOMContentLoaded', function() {
    const animatedElements = document.querySelectorAll('.animated');

    animatedElements.forEach((element) => {
        element.classList.add('animate__animated');
    });
});
