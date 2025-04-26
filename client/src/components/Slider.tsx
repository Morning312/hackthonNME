import React, { useState } from 'react';
import "../styles/Slider.css";

interface SliderProps {
    min: number;
    max: number;
    step?: number;
    onChange?: (value: number) => void;
}

const Slider: React.FC<SliderProps> = ({ min, max, step = 5, onChange }) => {
    const [value, setValue] = useState(min); // initialize value with min state w/useState hook
    const [isDragging, setIsDragging] = useState(false); // state to track if the slider is being dragged

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const newValue = Number(event.target.value); // get the new value from the event
        setValue(newValue);
        if (onChange) {
            onChange(newValue);
        }
    };

    return (
        <div style={{ width: '300px', margin: '20px auto', textAlign: 'center' }}>
            <input // slider input element
                type="range"
                min={min}
                max={max}
                step={step}
                value={value}
                onChange={handleChange}
                style={{ width: '100%' }}
            />
            <div style={{ marginTop: '10px' }}>Value: {value}</div>
        </div>
    );
};

const App: React.FC = () => {
    return (
        <div>
            <h1>Choose a year! </h1> 
            <Slider min={2025} max={3000} onChange={(value) => console.log('Slider value:', value)} />
        </div>
    );
};

export default App;