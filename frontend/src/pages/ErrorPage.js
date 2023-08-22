import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container } from "react-bootstrap";

function ErrorPage() {
    return (
        <Container className="mt-3">
            <div className="alert alert-danger">Error 404: Page Not Found!</div>
        </Container>
    )
}

export default ErrorPage