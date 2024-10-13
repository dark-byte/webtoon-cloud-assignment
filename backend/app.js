const express = require('express');
const app = express();
const port = 3000;

const manhwaData = require('./manhwa_data.json');

app.use(express.static('public'));

app.get('/api/manhwa', (req, res) => {
  res.json(manhwaData);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
