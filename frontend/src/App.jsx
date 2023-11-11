import React from 'react';
import './App.css';
import Navigation from './components/navigation';
import Dashboard from './components/initiativesPage';
import InitiativesPage from './components/initiativesPage';
import SignIn from './components/login';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Initiatives from './components/Initiatives';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<SignIn />} />
        <Route path="/dashboard" element={<Navigation />} />
        <Route path='/initiatives' element={<InitiativesPage />} />
      </Routes>
    </Router>
  );
}

// function ProtectedRoutes() {
//   return (
//     <Navigation>
//       <Route path="/dashboard" element={<Dashboard />} />
//       {/* Add more routes as needed */}
//     </Navigation>
//   );
// }

export default App;
