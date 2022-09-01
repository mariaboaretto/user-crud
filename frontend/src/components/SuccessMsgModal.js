import React from "react";
import { Modal, ModalBody, ModalFooter, ModalHeader } from "react-bootstrap";
import { Link } from "react-router-dom";

function SuccessMsgModal(props) {
    return (
        <Modal id="msg-modal" show={true}>
            <ModalHeader className="bg-success text-white">
                <h5>
                    <i className="fa-solid fa-circle-check"></i>
                    &nbsp;Success!
                </h5>
            </ModalHeader>
            <ModalBody>{props.msg}</ModalBody>
            <ModalFooter>
                <Link to="/">
                    <button className="btn btn-success">Close</button>
                </Link>
            </ModalFooter>
        </Modal>
    )
}

export default SuccessMsgModal