import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import ProjectDetail from './pages/ProjectDetail';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-dark text-white font-sans selection:bg-primary selection:text-white">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/projects" element={<Home />} /> {/* Re-using Home for now or scroll behavior */}
          <Route path="/project/:id" element={<ProjectDetail />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
