const express = require('express');
const app = express();
const port = 3000;

const manhwaData = require('./manhwa_data.json');

app.use(express.static('public'));

// Serve index.html at the root path
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.get('/api/manhwa', (req, res) => {
  res.json(manhwaData);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
