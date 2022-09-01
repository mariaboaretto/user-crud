import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import UserTable from "./UserTable";

function UserList(props) {
    return (
        <div className="container bg-light" id="user-list">
            <h4>User List</h4>
            <UserTable searchTxt={props.searchTxt}/>
        </div>
    )
}

export default UserList