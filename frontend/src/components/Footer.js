import React from "react";

function Footer() {
    return (
        <footer className="fixed-bottom bg-light mt-3 pt-3">
            <ul className="nav justify-content-center border-bottom pb-3 mb-3">
                <li className="nav-item">
                    <a href="/" className="nav-link px-2 text-dark">Home</a>
                </li>
                <li className="nav-item">
                    <a href="/about" className="nav-link px-2 text-dark">About</a>
                </li>
            </ul>
            <p className="text-center pb-3 mb-3 text-muted">
                <i className="fa-solid fa-users fa-xl"></i>
                &nbsp;&nbsp;User Management System
            </p>
        </footer>
    )
}

export default Footer