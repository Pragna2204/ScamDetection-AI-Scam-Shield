async function scanInput() {

    const input = document.getElementById("inputText").value;

    if (input.trim() === "") {
        alert("Please enter a URL or message.");
        return;
    }

    try {

        const response = await fetch("http://localhost:3000/scan", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                input: input
            })
        });

        const data = await response.json();

        // Show classification
        document.getElementById("status").textContent =
            data.classification;

        // Show score
        document.getElementById("score").textContent =
            "Risk Score: " + data.score + "%";

        // Show reasons
        const reasonsDiv = document.getElementById("reasons");

        reasonsDiv.innerHTML = "<h4>Detection Reasons:</h4>";

        if (data.reasons.length === 0) {

            reasonsDiv.innerHTML +=
                "<p>No suspicious characteristics detected.</p>";

        } else {

            data.reasons.forEach(reason => {

                const p = document.createElement("p");

                p.textContent = "⚠️ " + reason;

                reasonsDiv.appendChild(p);

            });
        }

    } catch (error) {

        document.getElementById("status").textContent =
            "Server connection failed.";

        console.error(error);
    }
}