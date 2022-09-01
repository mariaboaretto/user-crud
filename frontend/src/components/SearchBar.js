import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import "./Content.css"

function SearchBar(props) {
    let searchTxt = null;

    return (
        <div className="input-group mb-3" id="search-bar">
            <input type="text" className="form-control" placeholder="Search User..." onChange={(e) => searchTxt = e.target.value} />
            <div className="input-group-append">
                <button className="btn btn-outline-secondary" type="button" onClick={() => props.setSearchTxt(searchTxt)}><i className="fa-solid fa-magnifying-glass"></i></button>
            </div>
        </div>
    )
}

export default SearchBar