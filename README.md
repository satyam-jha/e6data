### Project Setup Guide

Follow these steps to set up and run the project:

1. **Create Virtual Environment**:
   - Create a virtual environment with Python version 3.9 or above.
     ```bash
     python3 -m venv myenv
     ```

2. **Install Dependencies**:
   - Install project dependencies using the `requirements.txt` file.
     ```bash
     pip install -r requirements.txt
     ```

3. **Run Migrations**:
   - Run migrations to set up the database.
     ```bash
     python manage.py migrate
     ```

4. **Run the Application**:
   - Start the server using the following command. By default, it runs on port 8000.
     ```bash
     python manage.py runserver
     ```
   - To specify a different port, use:
     ```bash
     python manage.py runserver <port_number>
     ```

5. **Run Unit Tests**:
   - Execute unit tests for the `blog` app.
     ```bash
     python manage.py test blog
     ```

6. **API Documentation**:
   - Refer to the [Postman Collection](https://api.postman.com/collections/10910644-7d572167-6d05-45b6-b44d-fe383b8966a2?access_key=PMAT-01HX3VAW7SBWK86WG2J97V7SBV) for API documentation.

Feel free to reach out if you encounter any issues or have further questions!
