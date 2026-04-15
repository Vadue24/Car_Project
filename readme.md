Here is the project which i developed with my groupmate in 2024.
Authors: Abdullo Kamoliddinov and Dmitriy Dogonkin

# ECARS.UZ Website

ECARS.UZ is a web application designed to assist users in selecting electric cars and calculating their total cost, including taxes and import fees, when bringing them into Uzbekistan. The platform is intuitive, responsive, and optimized for desktop and mobile devices.

## Features

- **Car Sorting:** Filter cars by price, brand, and other specifications.
- **Cost Calculator:** Calculate the total cost of cars, including VAT (12%), recycling fees, customs duties, and certification fees.
- **Car Descriptions:** Detailed pages for each car with specifications and images.
- **Admin Panel:** Manage car listings with ease through a secure backend.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Django 4.x
- Bootstrap 5.x (for front-end styling)
- SQLite (default Django database)
- A virtual environment tool (optional but recommended)

### Installation

Follow these steps to set up the project on your local machine:

1. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Enter Main Root**
   ```bash
   cd main

4. **Run the Development Server**
   ```bash
   python manage.py runserver

5. **Access the Application**
   ```
   http://127.0.0.1:8000
