import React, { useState } from "react";
import { Modal, ModalBody, ModalFooter, ModalHeader } from "react-bootstrap";

function DelUserModal(props) {
    const [show, setShow] = useState(true);

    const handleClose = () => setShow(false);

    const handleDelBtnClick = () => {
        props.handleClick();
        handleClose();
    }

    return (
        <Modal id="del-modal" show={show}>
            <ModalHeader className="bg-danger text-white">
                <h5>
                    <i className="fa-solid fa-circle-exclamation"></i>
                    &nbsp;Delete User?
                </h5>
            </ModalHeader>

            <ModalBody>
                <p>Are you sure you want to delete this user?</p>
                <p><b>This action cannot be undone.</b></p>
            </ModalBody>

            <ModalFooter>
                    <button className="btn btn-danger" onClick={handleDelBtnClick}>Delete</button>
                <button className="btn btn-secondary" onClick={handleClose}>Cancel</button>
            </ModalFooter>

        </Modal>
    )
}

export default DelUserModal