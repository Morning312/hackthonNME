import React from 'react';
import ProgressBar from './ProgressBar';

interface ContainerProps {
    label: string;
    progress: number;
}

const Container: React.FC<ContainerProps> = ({ label, progress }) => {

    return (
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <span
                
                style={{ cursor: 'pointer', color: 'blue', textDecoration: 'underline' }}
            >
                {label}
            </span>
            <ProgressBar value={progress} min={0} max={100} />
        </div>
    );
};

export default Container;