import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AboutPage from './components/AboutPage';
import CreateUserPage from './components/CreateUserPage';
import EditPasswordPage from './components/EditPasswordPage';
import EditUserPage from './components/EditUserPage';
import ErrorPage from './components/ErrorPage';
import Footer from './components/Footer';
import Header from './components/Header';
import HomePage from './components/HomePage';

class App extends React.Component {
    render() {  
      return (
        <Router>
          <Header/>
          <Routes>
            <Route path='/' element={<HomePage/>}/>
            <Route path='/create-user' element={<CreateUserPage/>}/>
            <Route path='/edit-user/:id' element={<EditUserPage/>}/>
            <Route path='/edit-password/:id' element={<EditPasswordPage/>}/>
            <Route path='/about' element={<AboutPage/>}></Route>
            <Route path='*' element={<ErrorPage/>}></Route>
          </Routes>
          <Footer/>
        </Router>
      );
    }
  }

  export default App