document.getElementById('workoutForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const goal = document.getElementById('goal').value;
    const level = document.getElementById('level').value;
    const equipment = document.getElementById('equipment').value;

    const response = await fetch('/recommend', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({goal, level, equipment})
    });

    const data = await response.json();

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
        <h3>Recommended Workouts:</h3>
        <ul>${data.recommendations.map(r => `<li>${r}</li>`).join('')}</ul>
        <p><strong>Reason:</strong> ${data.explanation}</p>
    `;
});
