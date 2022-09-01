import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

function AboutPage() {
    return (
        <div className="container m-3 p-3 bg-light text-dark" id="about-page">
            <div className="container" id="about-div">
                <h3>About</h3>

                <p>Hey there! My name is Maria Campos and I'm from Brazil. I'm a Computer Programming student
                    at Seneca College and I'm currently living in Toronto, Canada.
                </p>

                <p>
                    This simple user management system is a personal project created with the intent
                    of learning more about programming concepts such as persistant storage, databases, OOP, APIs,
                    interface design, web development, etc.
                </p>
            </div>

            <div className="container" id="contact-div">
                <h3>Contact Info</h3>

                <div className="table-responsive">
                    <table className="table">
                        <tbody>
                            <tr>
                                <td>
                                    <i className="fa-solid fa-envelope"></i>
                                </td>
                                <td>
                                    <a className="link-dark" href="mailto:mariaboarettocampos@gmail.com">
                                        mariaboarettocampos@gmail.com

                                    </a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <i className="fa-brands fa-github"></i>
                                </td>
                                <td>
                                    <a className="link-dark" href="https://github.com/mariaboaretto">
                                        github.com/mariaboaretto
                                    </a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <i className="fa-brands fa-linkedin"></i>
                                </td>
                                <td>
                                    <a className="link-dark" href="https://www.linkedin.com/in/maria-clara-boaretto-campos/">
                                        linkedin.com/in/maria-clara-boaretto-campos/
                                    </a>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </div>


        </div>
    )
}

export default AboutPage