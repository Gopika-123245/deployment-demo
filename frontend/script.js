
const API_URL = "https://deployment-demo-api.onrender.com";

const notesList = document.getElementById("notes-list");
const statusText = document.getElementById("status");
const refreshButton = document.getElementById("refresh-btn");

async function loadNotes() {
    statusText.textContent = "Loading your notes...";
    notesList.innerHTML = "";

    try {
        const response = await fetch(`${API_URL}/notes`);

        if (!response.ok) {
            throw new Error("Could not fetch notes");
        }

        const data = await response.json();

        for (const note of data.notes) {
            const listItem = document.createElement("li");
            listItem.textContent = note;
            notesList.appendChild(listItem);
        }

        statusText.textContent =
            `Successfully loaded ${data.notes.length} notes!`;

    } catch (error) {
        statusText.textContent =
            "Unable to load notes. Please try again.";

        console.error("Error loading notes:", error);
    }
}

refreshButton.addEventListener("click", loadNotes);

loadNotes();
