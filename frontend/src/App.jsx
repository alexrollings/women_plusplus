import React from 'react';
import './App.css';
import Navigation from './components/navigation';
import InitiativesPage from './components/initiativesPage';
import SideSignIn from './components/sideSignIn';
import SignIn from './components/login';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<SideSignIn />} />
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
