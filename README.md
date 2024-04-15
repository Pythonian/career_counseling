Project Scope
---

**Web Application: Career Counselor for Junior Secondary School Students based on their academic performance from JSS 1-3**

This application is for students who are about to enter senior secondary school, using their grades from JSS 1-3, help them decide on what area to go for **Science**, **Arts**, **Humanties** or **Commercials**, based on their academic performance.


### Project Installation

**Requirements**

- Python 3

_Follow the steps below to get the program working on your system locally. These steps are tailored for users developing on Linux OS._

1. Clone the repo
   ```sh
   git clone https://github.com/Pythonian/career_counseling.git
   ```
2. Change into the directory of the cloned repo
   ```sh
   cd career_counseling
   ```
3. Setup a Python virtual environment
   ```sh
   make venv
   ```
4. Activate the virtual environment
   ```sh
   . venv/bin/activate
   ```
5. Install project requirements
   ```sh
   make install
   ```
6. Run database migrations
   ```sh
   make migrate
   ```
7. Create an admin superuser
   ```sh
   make admin
   ```
   _Note: Use `admin` for both the `username` and `password`, and skip entering the `email`. Also type `y` to bypass Password validation._
8. Populate the database with fake data (Optional)
   ```sh
   python manage.py populate_db 5
   ```
9. Run the development server
   ```sh
   make run
   ```
10. Visit the URL in your browser
   ```sh
   127.0.0.1:8000
   ```
   You can also visit the admin dashboard in a new tab and login with the credentials used in step 7.
   ```sh
   127.0.0.1:8000/admin/
   ```
