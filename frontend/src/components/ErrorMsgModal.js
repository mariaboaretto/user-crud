import React, { useState } from "react";
import { Modal, ModalBody, ModalFooter, ModalHeader } from "react-bootstrap";

function ErrorMsgModal(props) {
    const [show, setShow] = useState(true);

    const handleClose = () => setShow(false);

    return (
        <Modal id="msg-modal" show={show}>
            <ModalHeader className="bg-danger text-white">
                <h5>
                    <i className="fa-solid fa-circle-exclamation"></i>
                    &nbsp;Error!
                </h5>
            </ModalHeader>
            <ModalBody>{props.msg}</ModalBody>
            <ModalFooter>
                <button className="btn btn-danger" onClick={handleClose}>Close</button>
            </ModalFooter>
        </Modal>
    )
}

export default ErrorMsgModal