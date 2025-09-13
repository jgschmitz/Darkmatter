// server.js
import express from "express";
import fetch from "node-fetch";
import bodyParser from "body-parser";
import dotenv from "dotenv";

dotenv.config();
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Load config
const config = {
  apiKey: process.env.API_KEY,
  apiSecret: process.env.API_SECRET,
  imageCount: 2,
  maxCompareScale: 5,
};

// Utility function to talk to SETI API
async function callSeti(endpoint, method = "GET", body = null) {
  const headers = {
    "Content-Type": "application/json",
    "X-API-KEY": config.apiKey,
    "X-API-SECRET": config.apiSecret,
  };

  const response = await fetch(`https://seti.example.com/${endpoint}`, {
    method,
    headers,
    body: body ? JSON.stringify(body) : null,
  });

  return response.json();
}

// Get images
app.get("/api/images", async (req, res) => {
  try {
    const images = await callSeti(`images?count=${config.imageCount}`);
    if (!images || images.length < config.imageCount) {
      return res.status(404).json({ error: "No images to process." });
    }
    res.json(images);
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch images." });
  }
});

// Submit comparison
app.post("/api/report", async (req, res) => {
  const { ids, scale } = req.body;
  try {
    await callSeti("report", "POST", { ids, scale });
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: "Failed to submit report." });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
