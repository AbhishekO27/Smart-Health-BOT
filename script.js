
const form = document.getElementById('greetingForm');
const resultDiv = document.getElementById('result');
const errorDiv = document.getElementById('error');
const historyList = document.getElementById('history');

form.addEventListener('submit', (event) => {
    event.preventDefault(); 

    
    const name = document.getElementById('name').value;

    if (!name) {
        showError("Please enter a name.");
        hideResult();
        return;
    }


    clearError();

   
    displayGreeting(name);

  
    addToHistory(name);

   
    form.reset();

   
});

function showError(message) {
    errorDiv.textContent = message;
}

function clearError() {
    errorDiv.textContent = "";
}

function hideResult() {
    resultDiv.style.opacity = 0;
}

function displayGreeting(name) {
    resultDiv.textContent = `Hello, ${name}! Welcome to my project.`;
    resultDiv.style.opacity = 1; 
}

function addToHistory(name) {
    const listItem = document.createElement('li');
    listItem.textContent = `Greeted: ${name}`;
    historyList.appendChild(listItem);
}