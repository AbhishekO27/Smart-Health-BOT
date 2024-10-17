
const form = document.getElementById('greetingForm');
const resultDiv = document.getElementById('result');


form.addEventListener('submit', (event) => {
    event.preventDefault(); 

    
    const name = document.getElementById('name').value;

  
    resultDiv.textContent = `Hello, ${name}! Welcome to my project.`;

    form.reset();
});
