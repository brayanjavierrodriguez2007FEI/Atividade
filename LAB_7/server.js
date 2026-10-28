const express = require('express');
const path = require('path');

const app = express();
const PORT = 80;

const pastaSite = path.join(__dirname, '..', 'LAB_3');

app.use(express.static(pastaSite));

app.get('/', (req, res) => {
    res.sendFile(path.join(pastaSite, 'copy.html'));
});

app.listen(PORT, '0.0.0.0', () => {
    console.log('Servidor rodando na porta ' + PORT);
});
