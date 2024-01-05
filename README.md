# Django REST API for Notes

This project implements a secure and scalable RESTful API for managing notes. Users can create, read, update, and delete their notes, share notes with other users, and search for notes based on keywords.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Development Server](#running-the-development-server)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
  - [Unit Tests](#unit-tests)
  - [Integration Tests](#integration-tests)
  - [End-to-End Tests](#end-to-end-tests)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (signup, login)
- CRUD operations for managing notes
- Share notes with other users
- Search notes based on keywords
- Token-based authentication
- Rate limiting and request throttling
- Unit tests, integration tests, and end-to-end tests

## Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/khadeom/notes_backend.git
   cd yourproject
   ```
2. Create a virtual environment:
   ```bash
   virtualenv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py runserver
   ```
## Running the Development Server
Start the development server:
```bash
python manage.py runserver
```


