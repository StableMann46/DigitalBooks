// Load Books and Display on Page
async function loadBooks() {
    try {
        let response = await fetch("books.json");
        let books = await response.json();

        // Sort books alphabetically
        books.sort((a, b) => a.name.localeCompare(b.name));

        let bookList = document.getElementById("book-list");
        bookList.innerHTML = books.map(book => 
            `<div class="book-item">
                <img src="${book.cover}" alt="Cover of ${book.name}">
                <h3>${book.name}</h3>
                <a href="${book.file}" target="_blank">Read Now</a>
            </div>`
        ).join("");
    } catch (error) {
        console.error("Error loading books:", error);
    }
}

// Search Book Functionality
function searchBook() {
    let query = document.getElementById("search-input").value.trim().toLowerCase();
    let books = document.querySelectorAll(".book-item");

    books.forEach(book => {
        let title = book.querySelector("h3").textContent.toLowerCase();
        book.style.display = title.includes(query) ? "block" : "none";
    });
}

// Dark Mode Toggle Functionality
document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.getElementById("dark-mode-toggle");

    // Check user preference in localStorage
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
        toggleButton.textContent = "☀️ Light Mode";
    }

    // Toggle Dark Mode on Button Click
    toggleButton.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
        
        // Store user preference in localStorage
        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
            toggleButton.textContent = "☀️ Light Mode";
        } else {
            localStorage.setItem("darkMode", "disabled");
            toggleButton.textContent = "🌙 Dark Mode";
        }
    });
});

// Load books on page load
window.onload = loadBooks;
