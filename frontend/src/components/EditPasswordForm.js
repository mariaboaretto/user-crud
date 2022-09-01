import axios from "axios";
import React from "react";
import BtnGroup from "./BtnGroup";
import ErrorMsgModal from "./ErrorMsgModal";
import SuccessMsgModal from "./SuccessMsgModal";

class EditPasswordForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = { msg: null, requestError: false }
        // eslint-disable-next-line no-unused-vars
        var currentPwd, newPwd, newPwdConf = null
    }

    updatePassword(e) {
        e.preventDefault();
        this.setState({msg: null, requestError: false})

        axios.put(`http://localhost:5000/users/password/${this.props.id}/`,
            {
                "current_password": this.currentPwd,
                "new_password": this.newPwd,
                "password_confirmation": this.newPwdConf
            })
            .then(response => {
                if (response.status === 200) this.setState({ msg: response.data.message })
            })
            .catch(error => this.setState({ msg: error.response.data.message, requestError: true }))
    }

    render() {
        return (
            <form onSubmit={(e) => this.updatePassword(e)}>
                <div className="container user-info-form bg-light">
                    <h3>Edit Password</h3>

                    {/* CURRENT PASSWORD FIELD */}
                    <div className="form-group required">
                        <label htmlFor="current-password-field" className="col-sm-2 col-form-label">Current Password</label>
                        <input type="password" className="form-control" id="current-password-field" required onChange={(e) => this.currentPwd = e.target.value} />
                    </div>

                    {/* NEW PASSWORD FIELD */}
                    <div className="form-group required">
                        <label htmlFor="new-password-field" className="col-sm-2 col-form-label">New Password</label>
                        <input type="password" className="form-control" id="new-password-field" required onChange={(e) => this.newPwd = e.target.value} />
                    </div>

                    {/* NEW PASSWORD CONFIRMATION FIELD */}
                    <div className="form-group required">
                        <label htmlFor="new-password-conf-field" className="col-sm-2 col-form-label">Type New Password Again</label>
                        <input type="password" className="form-control" id="new-password-conf-field" required onChange={(e) => this.newPwdConf = e.target.value} />
                    </div>

                    <BtnGroup />
                </div>
                {this.state.msg != null && !this.state.requestError ? <SuccessMsgModal msg={this.state.msg}/> : null}
                {this.state.msg != null && this.state.requestError ? <ErrorMsgModal msg={this.state.msg}/> : null}
            </form>
        )
    }
}

export default EditPasswordForm