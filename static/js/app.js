const searchBtn = document.getElementById("searchBtn");
const resultsDiv = document.getElementById("results");
const statusDiv = document.getElementById("status");

searchBtn.addEventListener("click", search);

async function search() {
    const query = document.getElementById("query").value.trim();
    const location = document.getElementById("location").value.trim();

    if (!query || !location) {
        statusDiv.innerText = "Please enter both query and location.";
        return;
    }

    statusDiv.innerText = "🧠 Scanning long-term disaster memory...";
    resultsDiv.innerHTML = "";

    try {
        const res = await fetch(`/search?query=${query}&location=${location}`);
        const data = await res.json();

        if (!data.results || data.results.length === 0) {
            statusDiv.innerText = "No relevant memory found.";
            return;
        }

        statusDiv.innerText = "Top relevant memory retrieved:";

        const r = data.results[0];
        const relevance = Math.min(100, r.importance * 100);

        resultsDiv.innerHTML = `
            <div class="card">
                <div class="tag">${r.type} | ${r.location}</div>
                <p>${r.text}</p>

                <div class="meter">
                    <div class="meter-fill" style="width:${relevance}%"></div>
                </div>

                <small>
                    Relevance Score: ${relevance}% <br>
                    Source Modality: ${r.modality}
                </small>
            </div>

            <div class="card">
                <strong>🤖 Why this was retrieved</strong><br><br>
                • Semantic similarity to query context<br>
                • Matching geographic metadata<br>
                • High reinforcement score
            </div>
        `;

    } catch (err) {
        statusDiv.innerText = "Error connecting to backend.";
        console.error(err);
    }
}
