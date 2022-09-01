import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from "react-router-dom";

class CreateUserBtn extends React.Component {
    render() {
        return (
            <Link to="/create-user">
                <button className="btn btn-outline-success">
                    <i className="fa-solid fa-user-plus"></i>
                    &nbsp;Create User
                </button>
            </Link>
        )
    }
}

export default CreateUserBtn