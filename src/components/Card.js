import React from 'react';

const Card = ({  image }) => {
  return (
    <div className="card">
      <img src={image}  className="card-image" />
      
    </div>
  );
};

export default Card;