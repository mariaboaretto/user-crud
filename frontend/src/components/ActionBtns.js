import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from "react-router-dom";
import DelUserModal from "./DelUserModal"

class ActionBtns extends React.Component {
    constructor(props) {
        super(props);
        this.state = {show: false}
    }

    showModal() {
        this.setState({show: true})
    }

    render() {
        return (
            <div className="container">
                <div className="btn-block" id="btn-group">
                    <Link to={`edit-user/${this.props.id}`}>
                        <button className="btn btn-outline-primary">
                            <i className="fa-solid fa-user-pen"></i>
                            &nbsp;Edit
                        </button>
                    </Link>
                    <button className="btn btn-outline-danger" onClick={() => this.showModal()}>
                        <i className="fa-solid fa-user-minus"></i>
                        &nbsp;Delete
                    </button>

                    {this.state.show ? <DelUserModal handleClick={this.props.handleClick} id={this.props.id}/> : null}
                </div>
            </div>
        )
    }
}

export default ActionBtns