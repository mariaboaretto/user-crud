import React from "react";
import "./Content.css"
import BtnGroup from "./BtnGroup";
import { Link } from "react-router-dom";
import axios from "axios";
import SuccessMsgModal from "./SuccessMsgModal";
import ErrorMsgModal from "./ErrorMsgModal";

class UserInfoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = { user: null, isLoaded: false, msg: null, pwdsMatch: true, requestError: false, showModal: false };
        // eslint-disable-next-line no-unused-vars
        var f_name, l_name, email, username, psswrd, psswrd_conf;
    }

    componentDidMount() {
        // If id is not null, perform GET request to retrieve user details
        if (this.props.id != null) {
            axios.get(`http://localhost:5000/users/${this.props.id}/`)
                .then(response => {
                    this.setState({ user: response.data, isLoaded: true });
                })
                .catch(error => {
                    this.setState({ requestError: true, msg: error.response.data.message });
                })
        }
    }

    handleClick(e) {
        e.preventDefault();
        // If user is null, a user should be created
        if (this.state.user == null) {
            this.createUser(this.f_name, this.l_name, this.email, this.username, this.psswrd, this.psswrd_conf);
        } else {
            // If the fields are empty, the user details won't be changed
            if (this.f_name == null) this.f_name = this.state.user.first_name;
            if (this.l_name == null) this.l_name = this.state.user.last_name;

            this.editUser(this.f_name, this.l_name);
        }
    }

    createUser(f_name, l_name, email, username, passwd, passwd_conf) {
        // Validating passwords
        // eslint-disable-next-line
        if (passwd != passwd_conf) {
            this.setState({ pwdsMatch: false })
            return;
        }

        // If passwords match, change state accordingly
        this.setState({ pwdsMatch: true, showModal: false, requestError: false });

        axios.post("http://localhost:5000/users/", {
            "first_name": f_name,
            "last_name": l_name,
            "email": email,
            "username": username,
            "password": passwd
        })
            .then(() => {
                this.setState({ showModal: true, msg: "User created successfully!" })
            })
            .catch(error => {
                this.setState({ msg: error.response.data.message, requestError: true, showModal: true })
            })
    }

    editUser(f_name, l_name) {
        axios.put(`http://localhost:5000/users/${this.props.id}/`, {
            "first_name": f_name,
            "last_name": l_name
        })
            .then(() => {
                this.setState({ showModal: true, msg: "User updated successfully!" })
            })
            .catch(error => {
                this.setState({ msg: error.response.data.message, requestError: true })
            })
    }

    renderFormLayout() {
        // CREATE USER FORM
        if (this.props.id == null) {
            return (
                <>
                    {/* PASSWORD FIELD */}
                    <div className="form-group required">
                        <label htmlFor="password-field" className="col-sm-2 col-form-label">Password</label>
                        <input type="password" className="form-control" onChange={(e) => this.psswrd = e.target.value} id="password-field" placeholder="Enter Password" required />
                    </div>

                    {/* PASSWORD CONFIRMATION FIELD */}
                    <div className="form-group required">
                        <label htmlFor="password-confirmation-field" className="col-sm-2 col-form-label">Confirm Password</label>
                        <input type="password" className="form-control" onChange={(e) => this.psswrd_conf = e.target.value} id="password-confirmation-field" placeholder="Confirm Password" required />
                        {/* If passwords do not match, an error msg will be displayed */}
                        <small id="pwd-conf-help" className="form-text text-danger">{!this.state.pwdsMatch ? "Passwords do not match!" : null}</small>
                    </div>
                </>
            )
        } else {
            // EDIT USER FORM
            if (this.state.isLoaded) {
                return (
                    <>
                        {/* EDIT PASSWORD LINK */}
                        <Link to={`/edit-password/${this.state.user.user_id}`} className="link-dark">
                            <i className="fa-solid fa-pen">&nbsp;&nbsp;</i>
                            Edit Password...
                        </Link>
                    </>
                )
            }
        }
    }

    render() {
        return (
            <form onSubmit={(e) => this.handleClick(e)}>
                <div className="container user-info-form bg-light">
                    <h3>{this.props.id == null ? "Create User" : "Edit User"}</h3>

                    {/* FIRST NAME FIELD */}
                    <div className={this.props.id == null ? "form-group required" : "form-group"}>
                        <label htmlFor="first-name-field" className="col-sm-2 col-form-label">First Name</label>
                        <input
                            id="first-name-field"
                            type="text"
                            className="form-control"
                            onChange={(e) => this.f_name = e.target.value}
                            defaultValue={this.state.user == null ? "" : this.state.user.first_name}
                            placeholder={this.state.user == null ? "Enter First Name" : null}
                            required={this.props.id == null ? true : false}
                        />
                    </div>

                    {/* LAST NAME FIELD */}
                    <div className={this.props.id == null ? "form-group required" : "form-group"}>
                        <label htmlFor="last-name-field" className="col-sm-2 col-form-label">Last Name</label>
                        <input
                            id="last-name-field"
                            type="text"
                            className="form-control"
                            onChange={(e) => this.l_name = e.target.value}
                            defaultValue={this.state.user == null ? "" : this.state.user.last_name}
                            placeholder={this.state.user == null ? "Enter Last Name" : null}
                            required={this.props.id == null ? true : false}
                        />
                    </div>

                    {/* EMAIL FIELD */}
                    <div className={this.state.user == null ? "form-group required" : "form-group"}>
                        <label htmlFor="email-field" className="col-sm-2 col-form-label">Email</label>
                        <input
                            id="email-field"
                            type="email"
                            className="form-control"
                            onChange={(e) => this.email = e.target.value}
                            placeholder={this.state.user == null ? "email@example.com" : this.state.user.email}
                            required={this.state.user == null ? true : false} disabled={this.state.user == null ? false : true}
                        />
                    </div>

                    {/* USERNAME FIELD */}
                    <div className={this.state.user == null ? "form-group required" : "form-group"}>
                        <label htmlFor="username-field" className="col-sm-2 col-form-label">Username</label>
                        <input
                            id="username-field"
                            type="text"
                            className="form-control"
                            onChange={(e) => this.username = e.target.value}
                            placeholder={this.state.user == null ? "Enter Username" : this.state.user.username}
                            required={this.state.user == null ? true : false} disabled={this.state.user == null ? false : true}
                        />
                    </div>

                    {this.renderFormLayout()}

                    <BtnGroup />

                    {this.state.showModal && !this.state.requestError ? <SuccessMsgModal msg={this.state.msg} /> : null}
                    {this.state.showModal && this.state.requestError ? <ErrorMsgModal msg={this.state.msg} /> : null}
                </div>
            </form>
        )
    }
}

export default UserInfoForm