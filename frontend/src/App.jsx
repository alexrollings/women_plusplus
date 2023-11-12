import React from 'react';
import './App.css';
import Navigation from './components/dashboard';
import InitiativesPage from './components/initiativesPage';
import SideSignIn from './components/sideSignIn';
import InitiativeDetails from './components/initiativeDetails';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Goals from './components/goalsPage';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<SideSignIn />} />
        <Route path="/dashboard" element={<Navigation />} />
        <Route path='/initiatives' element={<InitiativesPage />} />
        <Route path='/goals' element={<Goals />} />
        <Route path='/initiatives/5' element={<InitiativeDetails />} />
      </Routes>
    </Router>
  );
}

//will implement a wrapped navigation component for protected routes
// function ProtectedRoutes() {
//   return (
//     <Navigation>
//       <Route path="/dashboard" element={<Dashboard />} />
//       {/* Add more routes as needed */}
//     </Navigation>
//   );
// }

export default App;
