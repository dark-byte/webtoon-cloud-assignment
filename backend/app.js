const express = require('express');
const app = express();
const path = require('path');
const port = 3000;

const manhwaData = require('./manhwa_data.json');

app.use(express.static('public'));


// Serve static files from the 'frontend' directory
app.use(express.static(path.join(__dirname, '../frontend')));

// Serve index.html at the root path
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/index.html'));
});

app.get('/api/manhwa', (req, res) => {
  res.json(manhwaData);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
