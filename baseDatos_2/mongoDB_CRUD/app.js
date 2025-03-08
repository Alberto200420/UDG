const express = require("express");
const mongoose = require("mongoose");
const movieRoutes = require("./routes/movieRoutes");

const app = express();

// Conexión a MongoDB
mongoose
  .connect("mongodb://localhost:27017/movieDB", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("Conectado a MongoDB"))
  .catch((err) => console.error("Error conectando a MongoDB:", err));

// Rutas
app.use("/api/movies", movieRoutes);

// Iniciar servidor
app.listen(5000, () => {
  console.log(`Servidor corriendo en http://localhost:5000`);
});
