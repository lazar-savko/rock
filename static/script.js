document.addEventListener('DOMContentLoaded', () => {
    const choices = document.querySelectorAll('.choice');
    const resultDiv = document.getElementById('result');

    choices.forEach(choice => {
        choice.addEventListener('click', () => {
            const userChoice = choice.getAttribute('data-choice');
            fetch('/play', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ choice: userChoice }),
            })
            .then(response => response.json())
            .then(data => {
                const { user_choice, computer_choice, result } = data;
                resultDiv.innerHTML = `You chose ${user_choice}, computer chose ${computer_choice}. You ${result}!`;
            });
        });
    });
});
