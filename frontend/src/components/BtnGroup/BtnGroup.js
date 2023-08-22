import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from "react-router-dom";
import "./BtnGroup.css"

export default function BtnGroup(props) {
    return (
        <div className="btn-block pt-2" id="btn-group">
            <button type="submit" className="btn btn-primary">Submit</button>
            <Link to="/">
                <button type="button" className="btn btn-secondary">Cancel</button>
            </Link>
        </div>
    )
}