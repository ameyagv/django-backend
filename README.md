# Django Backend Project

## Overview

This project is a Django-based backend application providing APIs for managing car data. It includes endpoints for retrieving and adding car information. The project demonstrates how to set up a Django application and create simple RESTful APIs.

## Features

- **`/cars`**: GET endpoint to retrieve car data.
- **`/add/`**: POST endpoint to add a new car to the system.

## Prerequisites

- **Python**: 3.8 or higher
- **Pip**: Ensure you have `pip` installed for managing Python packages
- **Virtual Environment**: Recommended for isolating dependencies

## Setup

1. **Clone the Repository**

   Clone the project repository from GitHub:
   ```bash
   git clone https://github.com/ameyagv/django-backend.git
   cd django-backend

 2. **Set Up the Virtual Environment**
    Create and activate a virtual environment:
    ```bash
    python -m venv venv

    On Windows:
    venv\Scripts\activate
    
    On macOS/Linux:
    source venv/bin/activate

  3. **Install Dependencies**
     Install the required Python packages using pip:
     ```bash
     pip install -r requirements.txt

  4. **Apply Migrations**
      Set up the database by applying migrations:
      ```bash
      python manage.py migrate

  5. **Run the Development Server**
     ```bash
     python manage.py runserver


    

