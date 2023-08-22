import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CreateUserPage from './pages/CreateUserPage';
import EditPasswordPage from './pages/EditPasswordPage';
import EditUserPage from './pages/EditUserPage';
import ErrorPage from './pages/ErrorPage';
import Footer from './components/Footer/Footer';
import Header from './components/Header/Header';
import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';

class App extends React.Component {
  render() {
    return (
      <Router>
        <Header />
        <Routes>
          <Route path='/' element={<HomePage />} />
          <Route path='/create-user' element={<CreateUserPage />} />
          <Route path='/edit-user/:id' element={<EditUserPage />} />
          <Route path='/edit-password/:id' element={<EditPasswordPage />} />
          <Route path='/about' element={<AboutPage />}></Route>
          <Route path='*' element={<ErrorPage />}></Route>
        </Routes>
        <Footer />
      </Router>
    );
  }
}

export default App