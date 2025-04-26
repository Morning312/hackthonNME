import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import Card from '../components/Card';
import Slider from '../components/Slider';

const subcategories = [
  { id: 1, title: 'Subgoal A', description: 'Short description here', imageUrl: 'https://via.placeholder.com/300' },
  { id: 2, title: 'Subgoal B', description: 'Short description here', imageUrl: 'https://via.placeholder.com/300' },
];

const CategoryPage: React.FC = () => {
  const { categoryId } = useParams();
  const [year, setYear] = useState(2025);

  return (
    <div className="min-h-screen p-8 bg-gray-100 flex flex-col gap-8">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {subcategories.map((sub) => (
          <Card
            key={sub.id}
            title={sub.title}
            description={sub.description}
            imageUrl={sub.imageUrl}
            progress={(year - 2000) / 1}
          />
        ))}
      </div>

      <div className="mt-12">
        <Slider min={2000} max={2100} onChange={(v) => setYear(v)} />
      </div>
    </div>
  );
};

export default CategoryPage;
