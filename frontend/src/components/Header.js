import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';

class Header extends React.Component {
  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark py-4 sticky">
        <div className="container">
          {/* Icon */}
          <Link to="/" className='navbar-brand'>
            <i className="fa-solid fa-users fa-xl"></i>
            &nbsp;&nbsp;User Management
          </Link>

          {/* Button for showing menu options in smaller screens*/}
          <button
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#menu-options"
            className="navbar-toggler">
            <span className="navbar-toggler-icon"></span>
          </button>

          {/* Menu options */}
          <div className="collapse navbar-collapse" id="menu-options">
            <ul className="navbar-nav">
              <li className="nav-item active">
                <Link to="/about" className="nav-link active" id="about-section">About</Link>
              </li>
            </ul>
          </div>
        </div>

      </nav>
    )
  }
}

export default Header