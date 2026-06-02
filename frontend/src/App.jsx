import React, { useState, useEffect } from 'react';
import Navigation from './components/Navigation';
import Dashboard from './components/Dashboard';
import LiveMatches from './components/LiveMatches';
import StandingsPage from './components/StandingsPage';
import { initializeSocket } from './services/websocket';
import './index.css';

function App() {
  const [currentPage, setCurrentPage] = useState('dashboard');

  useEffect(() => {
    // Initialize WebSocket connection
    initializeSocket();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50">
      <Navigation currentPage={currentPage} setCurrentPage={setCurrentPage} />
      <main>
        {currentPage === 'dashboard' && <Dashboard />}
        {currentPage === 'live' && <LiveMatches />}
        {currentPage === 'standings' && <StandingsPage />}
        {currentPage === 'predictions' && (
          <div className="p-8 text-center text-gray-600 min-h-screen flex items-center justify-center">
            <div>
              <h2 className="text-2xl font-bold mb-2">Detailed Predictions</h2>
              <p>Coming soon</p>
            </div>
          </div>
        )}
        {currentPage === 'settings' && (
          <div className="p-8 text-center text-gray-600 min-h-screen flex items-center justify-center">
            <div>
              <h2 className="text-2xl font-bold mb-2">Settings</h2>
              <p>Coming soon</p>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
