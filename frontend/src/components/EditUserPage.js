import React from "react";
import { useParams } from "react-router-dom";
import UserInfoForm from "./UserInfoForm";

function EditUserPage() {
    const id = useParams().id;

    return (
        <UserInfoForm id={id}/>
    )
}

export default EditUserPage