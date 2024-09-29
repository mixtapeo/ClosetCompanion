import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './pages/Home';
import Closet from './pages/Closet';
import Outfits from'./pages/Outfits';
import Add from './pages/Add';
import NavBar from './components/NavBar';
import './index.css';
function App() {
  return (
    <Router>
      
    <NavBar/>
    
       
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<Closet />} />
        <Route path="/contact" element={<Outfits />} />
        <Route path="/add" element={<Add />} />
      </Routes>
    </Router>

    
  );
}

export default App;
