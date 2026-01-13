import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [formData, setFormData] = useState({
    feature1: 0,
    feature2: 0,
    feature3: 0
  });
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: parseFloat(e.target.value)
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      // URL del backend (ajustar por entorno)
      const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8080';
      
      const response = await axios.post(`${apiUrl}/process-prediction`, formData);
      setPrediction(response.data);
    } catch (err) {
      setError(err.message || 'Error al conectar con el servidor');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header>
        <h1>ML Prediction Dashboard</h1>
        <p>Introduce las características para obtener una predicción del modelo.</p>
      </header>

      <div className="card">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="feature1">Característica 1:</label>
            <input
              type="number"
              id="feature1"
              name="feature1"
              value={formData.feature1}
              onChange={handleChange}
              step="0.1"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="feature2">Característica 2:</label>
            <input
              type="number"
              id="feature2"
              name="feature2"
              value={formData.feature2}
              onChange={handleChange}
              step="0.1"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="feature3">Característica 3:</label>
            <input
              type="number"
              id="feature3"
              name="feature3"
              value={formData.feature3}
              onChange={handleChange}
              step="0.1"
              required
            />
          </div>

          <button type="submit" disabled={loading}>
            {loading ? 'Procesando...' : 'Predecir'}
          </button>
        </form>

        {prediction && (
          <div className="result">
            <h3>Resultado:</h3>
            <p><strong>Predicción Cruda:</strong> {prediction.prediction_raw.toFixed(4)}</p>
            <p><small>{prediction.input_summary}</small></p>
          </div>
        )}

        {error && (
          <div className="error">
            <p>Error: {error}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
