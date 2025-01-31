// Function to process text input
function processText(endpoint) {
    let text = document.getElementById("textInput").value;
    
    fetch(`http://127.0.0.1:5000/${endpoint}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        let formattedOutput = JSON.stringify(data, null, 4); // Pretty JSON format
        document.getElementById("result").innerText = formattedOutput;
    })
    .catch(error => console.error("Error:", error));
}

// Theme Toggle
function toggleTheme() {
    document.body.classList.toggle("dark-mode");

    // Save preference to local storage
    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}

// Load theme preference
window.onload = function() {
    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
    }
};
