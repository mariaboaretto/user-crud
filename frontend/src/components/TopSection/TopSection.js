import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import SearchBar from "../SearchBar/SearchBar";
import CreateUserBtn from "../CreateUserBtn/CreateUserBtn";
import "./TopSection.css"

function TopSection(props) {
    return (
        <div className="container bg-light" id="top-section">
            <div className="row">
                <div className="col col-lg-5">
                    <SearchBar setSearchTxt={props.setSearchTxt}/>
                </div>
                <div className="col col-lg offset-md-5">
                    <CreateUserBtn />
                </div>
            </div>
        </div>
    )
}

export default TopSection