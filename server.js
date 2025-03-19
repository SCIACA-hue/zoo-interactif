const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Bienvenue sur votre API !');
});

const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Serveur en cours d'exécution sur http://localhost:${PORT}`);
});
npm 
function MyButton() {
    return (
      <button>I'm a button</button>
    );
  }
  export default function MyApp() {
    return (
      <div>
        <h1>Welcome to my app</h1>
        <MyButton />
      </div>
    );
  }