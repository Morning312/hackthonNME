import React, { useState } from 'react';
import TopicBar from '../components/TopicBar';
import Slider from '../components/Slider';

const categories = [
  { id: 'environment', name: 'Environment', color: 'bg-green-600' },
  { id: 'technology', name: 'Technology', color: 'bg-blue-600' },
  { id: 'doomsday', name: 'Doomsday', color: 'bg-red-600' },
  { id: 'health', name: 'Health', color: 'bg-yellow-500' },
  { id: 'wildcard', name: 'Wildcard', color: 'bg-purple-600' },
];

const HomePage: React.FC = () => {
  const [year, setYear] = useState(2025);

  return (
    <div className="min-h-screen flex flex-col justify-between p-8 bg-gray-50">
      <div className="space-y-8">
        <h1 className="text-4xl font-bold text-gray-800">Explore Global Trends</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {categories.map((cat) => (
            <TopicBar key={cat.id} id={cat.id} name={cat.name} color={cat.color} />
          ))}
        </div>
      </div>

      <div className="mt-12">
        <Slider min={2000} max={2100} onChange={(v) => setYear(v)} />
      </div>
    </div>
  );
};

export default HomePage;
