const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

app.post("/scan", async (req, res) => {

    const input = req.body.input;

    if (!input) {
        return res.status(400).json({
            error: "No input provided"
        });
    }

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    url: input
                })
            }
        );

        const mlResult = await response.json();

        res.json({
            score: mlResult.probability,
            classification: mlResult.prediction,
            reasons: mlResult.prediction === "PHISHING"
    ? [
        "The ML model detected phishing-like characteristics in this URL.",
        "The URL structure contains patterns commonly associated with suspicious websites."
      ]
    : [
        "The ML model did not detect significant phishing characteristics.",
        "The URL appears relatively safe based on the analyzed features."
      ]
        });

    } catch (error) {

        console.error("ML Error:", error);

        res.status(500).json({
            error: "ML server is not available"
        });
    }
});

app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});