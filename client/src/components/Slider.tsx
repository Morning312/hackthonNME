import React from 'react';
import "../styles/Slider.css";

interface SliderProps {
    min: number;
    max: number;
    onChange: (value: number) => void;
}

const Slider: React.FC<SliderProps> = ({ min, max, onChange }) => {
    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        onChange(Number(event.target.value));
    };

    return <input type="range" min={min} max={max} onChange={handleChange} />;
};

export default Slider;