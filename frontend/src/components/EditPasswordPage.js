import React from "react";
import { useParams } from "react-router-dom";
import "./Content.css"
import EditPasswordForm from "./EditPasswordForm";

function EditPasswordPage() {
    const { id } = useParams();

    return (
        <EditPasswordForm id={id}/>
        
    )
}

export default EditPasswordPage
