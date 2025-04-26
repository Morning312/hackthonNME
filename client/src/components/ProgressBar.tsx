import React from 'react';
import "../styles/ProgressBar.css";

interface ProgressBarProps {
    min: number;
    max: number;
    value: number; // Current value to calculate percentage
    topic?: string; // Optional label for the progress bar
}

const ProgressBar: React.FC<ProgressBarProps> = ({ min, max, value, topic }) => {
    // Calculate the percentage based on the value
    const percentage = ((value - min) / (max - min)) * 100;

    return (
        <div className="progress-bar-wrapper" style={{ margin: '20px 0', textAlign: 'center' }}>
             <h3 className="progress-bar-label" style={{ marginBottom: '10px', fontWeight: 'bold' }}>{topic}</h3>
            <div className="progress-bar-container" style={{ width: '100%', height: '20px', backgroundColor: '#e0e0e0', borderRadius: '10px', overflow: 'hidden' }}>
                <div
                    className="progress-bar-filled"
                    style={{
                        width: `${percentage}%`,
                        height: '100%',
                        backgroundColor: '#76c7c0',
                        transition: 'width 0.3s ease-in-out',
                    }}
                ></div>
            </div>
        </div>
    );
};

export default ProgressBar;