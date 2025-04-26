import React from 'react';
import "../styles/Card.css";
import ProgressBar from './ProgressBar'; // Import your ProgressBar component
import Slider from './Slider'; // Import your Slider component

interface CardProps {
    title: string;
    description: string;
    imageUrl: string;
    progress: number; // Add progress as a prop
}

const Card: React.FC<CardProps> = ({ title, description, imageUrl, progress }) => {
    return (
        <div className="card" style={{ width: '300px', margin: '20px auto', textAlign: 'center' }}>
            <img src={imageUrl} alt={title} style={{ width: '100%', height: 'auto', borderRadius: '10px' }} />
            <h2 className="card-title" style={{ margin: '10px 0', fontSize: '1.5em' }}>{title}</h2>
            <p className="card-description" style={{ fontSize: '1em', color: '#555' }}>{description}</p>
            <div style={{ marginTop: '10px' }}>
                <ProgressBar value={progress} min={0} max={100} /> {/* Use your ProgressBar component */}
            </div>
        </div>
    );
};
