import React, { useState, useEffect } from 'react';
import Slider from '../components/Slider';
import '../styles/HomePage.css';

interface Category {
  name: string;
  min: number;
  max: number;
  unit: string;
}

const categories: Category[] = [
  { name: "Global Warming", min: 0, max: 100, unit: " °C" },
  { name: "Nitrogen Air Pollution", min: 100000, max: 300000000, unit: " tons per year" },
  { name: "Carbon Monoxide Air Pollution", min: 10000000, max: 1000000000, unit: " tons per year" },
  { name: "Black Carbon Air Pollution", min: 1000000, max: 20000000, unit: " tons per year" },
  { name: "Poverty", min: 0, max: 100, unit: "%" },
  { name: "World Hunger", min: 0, max: 100, unit: "%" },
  { name: "Microplastics", min: 0, max: 25, unit: " pieces per m^3" },
  { name: "Clean Water", min: 0, max: 100, unit: "%" },
  { name: "HIV", min: 0, max: 5, unit: " diagnoses per 100,000" },
  { name: "Tuberculosis", min: 0, max: 1000, unit: " diagnoses per 100,000" },
  { name: "Malaria", min: 0, max: 200, unit: " diagnoses per 1,000" },
  { name: "Life Expectancy", min: 0, max: 250, unit: " years" }
];

const HomePage: React.FC = () => {
  const [selectedYear, setSelectedYear] = useState<number>(2000);
  const [predictions, setPredictions] = useState<Record<string, number>>({});

  useEffect(() => {
    const fetchPredictions = async () => {
      const newPredictions: Record<string, number> = {};
      
      for (const category of categories) {
        try {
          console.log(`Fetching prediction for ${category.name} at year ${selectedYear}`);
          const response = await fetch(`http://localhost:8000/predict?metric=${encodeURIComponent(category.name)}&year=${selectedYear}&min=${category.min}&max=${category.max}`);
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const data = await response.json();
          console.log(`Received data for ${category.name}:`, data);
          
          // Ensure we're getting a number value
          const prediction = typeof data.prediction === 'number' ? data.prediction : parseFloat(data.prediction);
          if (isNaN(prediction)) {
            throw new Error(`Invalid prediction value received: ${data.prediction}`);
          }
          
          // Ensure the prediction is within the min-max range
          const clampedValue = Math.max(category.min, Math.min(category.max, prediction));
          newPredictions[category.name] = clampedValue;
        } catch (error) {
          console.error(`Error fetching prediction for ${category.name}:`, error);
          // Fallback to random value if API call fails
          newPredictions[category.name] = Math.floor(Math.random() * (category.max - category.min) + category.min);
        }
      }
      
      console.log('Updated predictions:', newPredictions);
      setPredictions(newPredictions);
    };

    fetchPredictions();
  }, [selectedYear]);

  return (
    <div className="homepage">
      <h1>Environmental and Health Indicators</h1>
      <div className="year-selector">
        <h2>Select Year: {selectedYear}</h2>
        <Slider 
          min={2000} 
          max={3000} 
          onChange={setSelectedYear} 
        />
      </div>
      
      <div className="categories-container">
        {categories.map((category) => {
          const value = predictions[category.name] || category.min;
          // Ensure value is within bounds
          const clampedValue = Math.max(category.min, Math.min(category.max, value));
          const percentage = ((clampedValue - category.min) / (category.max - category.min)) * 100;
          
          console.log(`Category: ${category.name}`);
          console.log(`Value: ${clampedValue}, Min: ${category.min}, Max: ${category.max}`);
          console.log(`Percentage: ${percentage}%`);
          
          return (
            <div key={category.name} className="category-container">
              <div className="category-header">
                <h3>{category.name}</h3>
                <span className="category-value">{clampedValue.toLocaleString()}{category.unit}</span>
              </div>
              <div className="progress-bar-container">
                <div 
                  className="progress-bar" 
                  style={{ 
                    width: `${percentage}%`,
                    transition: 'width 0.3s ease-in-out'
                  }}
                />
              </div>
              <div className="range-info">
                <span>Min: {category.min.toLocaleString()}{category.unit}</span>
                <span>Max: {category.max.toLocaleString()}{category.unit}</span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default HomePage; 