import React from "react";
import { useParams } from "react-router-dom";
import EditPasswordForm from "../components/EditPasswordForm/EditPasswordForm";

function EditPasswordPage() {
    const { id } = useParams();

    return (
        <EditPasswordForm id={id}/>
        
    )
}

export default EditPasswordPage
