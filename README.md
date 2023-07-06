Project Scope
---

**Web Application: Career Counselor for Junior Secondary School Students based on their academic performance from JSS 1-3**

This application is for students who are about to enter senior secondary school, using their grades from JSS 1-3, help them decide on what area to go for **Science**, **Arts** or **Commercials**, based on their performance.


**Features of the Web Application:**

1. **User Registration and Login:** Allow students to create accounts and log in to access the counselor's features.

2. **Academic Performance Tracking:** Provide a feature for students to input their academic performance data, including grades and subjects.

3. **Subject Classification:** Develop a feature that categorizes the subjects taken in JSS 1-3 into their respective fields (science, arts, or commerce). This classification will help in analyzing a student's performance in each field.

4. **Performance Analysis:** Offer a detailed analysis of a student's academic performance in each field, highlighting their strengths and weaknesses.

5. **Career Prediction:** Based on the student's academic performance in JSS 1-3 and the field classification of subjects, predict the most suitable career field for the student (science, arts, or commerce).

6. **Career Exploration:** Provide a comprehensive list of various careers within the predicted field of study. Include detailed information about each career, such as job descriptions, required skills, educational pathways, and potential salary ranges.

7. **Related Disciplines:** Offer a list of related disciplines or specialized fields within the predicted career field. This feature will allow students to explore specific areas of interest within their chosen field.


**Development Process with Django:**

1. **Design the Database:** Identify the necessary database tables based on the features outlined above. Define the fields and relationships between the tables.

   - User: Stores user account information, including username, email, and password.
   - Subject: Stores information about JSS subjects, including their names and respective fields (science, arts, commerce).
   - AcademicPerformance: Stores the academic performance data of students, including subject grades and fields.
   - CareerField: Stores information about the three career fields (science, arts, commerce).
   - Career: Stores information about various careers, including their descriptions, required skills, and related career field.
   - Discipline: Stores information about specialized disciplines within each career field.

2. **Create Django Models:** Define Django models based on the database design.

3. **Implement Views and Templates:** Create views that handle user interactions and display the appropriate templates.

4. **Develop Business Logic:** Implement the logic behind the features, such as calculating career recommendations based on academic performance data.

5. **Implement User Authentication:** Set up user registration, login, and authentication functionality.

6. **Create Forms:** Design and implement forms for inputting academic performance data, career assessment information, and goal setting.

**Workflow of the Web App:**

1. **User Registration and Login:** Students can create accounts and log in to the web application.

2. **Input Academic Performance Data:** Students provide their academic performance data for JSS 1-3 subjects.

3. **Subject Classification:** The web app categorizes the subjects into their respective fields (science, arts, commerce) for performance analysis.

4. **Performance Analysis:** The app analyzes and evaluates the student's academic performance in each field, providing a detailed analysis of their strengths and weaknesses.

5. **Career Prediction:** Based on the performance analysis, the web app predicts the most suitable career field for the student (science, arts, or commerce).

6. **Career Exploration:** The web app provides a list of careers within the predicted field of study. It displays detailed information about each career, including job descriptions, required skills, educational pathways, and potential salary ranges.

7. **Related Disciplines:** The web app offers a list of related disciplines or specialized fields within the predicted career field. This allows students to explore specific areas of interest within their chosen field.
