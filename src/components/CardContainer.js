import React, { useEffect, useState } from 'react';
import Card from './Card';
import './CardContainer.css'; // Adng
import images from '../imageLoader';
const CardContainer = () => {
  const [cardsData, setCardsData] = useState([]);

  // Retrieve captured images from localStorage when the component mounts
  useEffect(() => {
    const storedImages = JSON.parse(localStorage.getItem('capturedImages')) || [];
    const imageArray = Object.values(images);
    setCardsData([...storedImages, ...imageArray]);
  }, []);

  return (
    <div className="card-container">
      {cardsData.length === 0 ? (
        <p className= "text-white text-2xl font-mono">No images added yet.</p>
      ) : (
        cardsData.map((image, index) => (
          <Card key={index} title={`Card ${index + 1}`} description={`This is card ${index + 1}`} image={image} />
        ))
      )}
    </div>
  );
};

export default CardContainer;
