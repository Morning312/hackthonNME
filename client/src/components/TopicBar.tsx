import React from 'react';
import { useNavigate } from 'react-router-dom';

interface TopicBarProps {
  id: string;
  name: string;
  color: string;
}

const TopicBar: React.FC<TopicBarProps> = ({ id, name, color }) => {
  const navigate = useNavigate();

  return (
    <div
      className={`flex-1 p-4 rounded-2xl text-center font-bold text-white ${color} hover:opacity-90 cursor-pointer`}
      onClick={() => navigate(`/category/${id}`)}
    >
      {name}
    </div>
  );
};

export default TopicBar;
