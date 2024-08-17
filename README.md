# Inventory Management System

This is an Inventory Management System built using Django. The application allows users to manage and track inventory items, including adding, updating, and deleting items.

## Features

- Add new inventory items
- Update existing inventory items
- Delete inventory items
- View a list of all inventory items
- Search for inventory items

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ksh168/Inventory-django-project.git
   cd Inventory-django-project
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv ./venv
   source ./venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the application at `http://127.0.0.1:8000/`.

## Configuration

Make sure to update the `settings.py` file with your specific configuration, such as database settings, allowed hosts, and other settings as needed.

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage inventory items.
- Use the API endpoints to interact with the inventory items programmatically.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
