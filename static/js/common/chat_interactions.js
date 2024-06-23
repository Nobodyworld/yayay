document.addEventListener("DOMContentLoaded", function() {
    const commentForm = document.getElementById('comment-form');
    if (commentForm) {
        commentForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(commentForm);
            fetch("{% url 'chat-comment' chat.pk %}", {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                }
            })
            .then(response => response.json())
            .then(data => {
                const commentsList = document.getElementById('comments-list');
                commentsList.innerHTML += `<li>${data.comment}</li>`;
            })
            .catch(error => console.error('Error:', error));
        });
    }
});
