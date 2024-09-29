import React from 'react';
import CardContainer from '../components/CardContainer';

const Home = () => {
  return (
    <div className ="bg-min-h-screen flex flex-col items-center p-6">
      <h1 className="text-4xl font-bold mb-4 text-center">Welcome</h1>
      <p className="text-lg mb-8 text-center">View your catlog below..</p>
      <div className = "  flex flex-wrap justify-center gap-10"> 

     
      <CardContainer />
      
      </div>
    </div>
  );
};

export default Home;