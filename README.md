# User CRUD

This is the **User CRUD** project, a simple web application for performing CRUD (Create, Read, Update, Delete) operations on user data. It provides a user management system with basic functionalities.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Technologies](#technologies)
- [Authors](#authors)

## Introduction

This **User CRUD** project was created with the intent of learning more about programming concepts such as persistant storage, databases, OOP, APIs, interface design, web development, etc. It was designed to demonstrate the fundamental CRUD operations using a web application. It allows users to manage user data by performing various operations such as creating new users, reading user information, updating user details, and deleting users from the system.

## Features

- Create a new user with details such as name, email, and more.
- View user information, including their details.
- Update user details like name, email, etc.
- Delete users from the system.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Node.js (version 18.13.0)
- npm (version 9.2.0)
- Python (version 3.11.2)
- A modern web browser

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/mariaboaretto/user-crud.git
   ```

2. Navigate to the project directory:

    ```sh
    cd user-crud
    ```

3. Install the required dependencies for the frontend:

    ```sh
    cd frontend
    npm install
    ```

4. Create and activate a Python virtual environment (venv):

    ```sh
    cd ../backend
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

5. Install the required Python dependencies for the backend:

    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Run the backend server:

    ```sh
    cd backend
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    python main.py
    ```

2. The backend server should now be running, enabling communication between the frontend and the database.

3. Start the frontend application:

    ```sh
    cd frontend
    npm start
    ```

4. Open your web browser and visit: 'http://localhost:3000'.

5. Use the web interface to perform CRUD operations on user data.

## Technologies
- Python: Programming language for backend server implementation.
- Flask: Micro web framework for Python.
- SQLite: Relational database for storing user data.
- React, HTML, CSS, JavaScript: Frontend technologies for building the user interface.

## Authors
- Maria Campos (macampos.dev@gmail.com)