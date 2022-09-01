import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import ActionBtns from './ActionBtns';

class UserTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = { users: [], error_message: null, isLoaded: false }
        this.renderTableRow = this.renderTableRow.bind(this)
        this.searchTxt = this.props.searchTxt;
    }

    // After component's been rendered, perform API request
    componentDidMount() {
        this.getUsers();
    }

    componentDidUpdate(prevProps) {
        if (prevProps.searchTxt !== this.props.searchTxt) {
            this.searchTxt = this.props.searchTxt;
            this.getUsers();
        }
    }

    // Renders table row with user information
    renderTableRow(user) {
        return (
            <tr key={user.user_id}>
                <td>{user.first_name + " " + user.last_name}</td>
                <td>{user.email}</td>
                <td>{user.username}</td>
                <td><ActionBtns id={user.user_id} handleClick={() => this.delUser(user.user_id)} /></td>
            </tr>)
    }

    getUsers() {
        let url = "http://localhost:5000/users/"

        if (this.searchTxt !== null && this.searchTxt !== "")
            url = url + `?search_txt=${this.searchTxt}`

        // GET Request for all users.
        // If successful, users array is populated with data from response
        axios.get(url)
            .then(response => {
                this.setState({ users: response.data, isLoaded: true })
            })
            // Otherwise, sets error_message accordingly
            .catch(error => {
                this.setState({ error_message: error.code + ": " + error.message, isLoaded: true })
            })

    }

    delUser(id) {
        axios.delete(`http://localhost:5000/users/${id}/`)
            .then(response => {
                // If delet request is successful, sends get request to update user list and re-render component
                if (response.status === 200) this.getUsers();
            })
            .catch(error => {
                this.setState({ error_message: error.code + ": " + error.message })
            })
    }

    render() {
        // If data is not loaded, returns Loading message
        if (!this.state.isLoaded) {
            return (
                <p>Loading...</p>
            )
        }

        // Returns error_message if an error occured
        if (this.state.error_message != null) {
            return (
                <p className='alert alert-danger'>{this.state.error_message}</p>
            )
        }

        // If users array is empty, return appropriate message
        if (this.state.users.length === 0) return (<p className='text text-muted'>No users to display...</p>)

        // Returns table otherwise
        return (
            <div className='table-responsive'>
                <table className='table table-light table-striped table-bordered'>
                    <thead>
                        <tr>
                            <th>Full Name</th>
                            <th>Email</th>
                            <th>Username</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.users.map(this.renderTableRow)}
                    </tbody>
                </table>
            </div>)
    }

}

export default UserTable