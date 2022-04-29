const express = require('express');
const app = express();
const newsRouter = require('./routers/app')

app.use(express.static('public'));
app.use('api',newsRouter)// => localhost:3000/api/create

app.listen(3000, () => {
  console.log('Port is listening.');
});
