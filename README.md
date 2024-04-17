# Career Compass

![Career Compass Hero Section](docs/hero.jpeg)

![Static Badge](https://img.shields.io/badge/Owner-Pythonian-green)
![GitHub last commit](https://img.shields.io/github/last-commit/pythonian/career_counseling)
![GitHub top language](https://img.shields.io/github/languages/top/pythonian/career_counseling)

## Contents

- [About the Project](#about-the-project)
  * [How does it Work](#how-does-it-work)
- [Getting Started](#getting-started)
  * [Requirements](#requirements)
  * [Installation](#installation)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [Support](#support)
- [Changelog](#changelog)
- [License](#license)
- [Contact](#contact)

## About The Project

**A Career Counselor Web Application for Junior Secondary School Students based on their academic performance from JSS 1-3**

This application is for students who are about to enter senior secondary school, using their grades from JSS 1-3, help them decide on what area to go for **Science**, **Arts**, **Humanties** or **Commercials**, based on their academic performance.

### How does it Work

An explanation of how the project works

## Getting Started

### Requirements

- Python 3

### Installation

_Follow the steps below to get the program working on your system locally. These steps are tailored for users developing on Linux OS._

1. Clone the repo
   ```sh
   git clone https://github.com/Pythonian/career_counseling.git
   ```
2. Change into the directory of the cloned repo
   ```sh
   cd career_counseling
   ```
3. Setup a Python virtual environment and activate it
   ```sh
   make venv
   source venv/bin/activate
   ```
4. Install project requirements
   ```sh
   make install
   ```
5. Run database migrations
   ```sh
   make migrate
   ```
6. Create an admin superuser
   ```sh
   make admin
   ```
   _Note: Use `admin` for both the `username` and `password`, and skip entering the `email`. Also type `y` to bypass Password validation._
7. Populate the database with fake data (Optional)
   ```sh
   make populatedb
   ```
8. Run the development server
   ```sh
   make run
   ```
9. Visit the URL in your browser
   ```sh
   127.0.0.1:8000
   ```
   You can also visit the admin dashboard in a new tab and login with the credentials used in step 7.
   ```sh
   127.0.0.1:8000/admin/
   ```
   *include settings configuration*

## Running Tests

To run tests, run the following command

```bash
   make test
```

## Contributing

Contributions are always welcome! Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

If you encounter any bug or problem while using the project, please [open an issue](https://github.com/Pythonian/career_counseling/issues)

## Changelog

For a detailed list of changes, see the [Changelog](docs/CHANGELOG.md).

## License

This project is licensed under the [MIT License](LICENSE.md).

## Contact

If you have any questions, suggestions, or feedback, feel free to reach out to me

Seyi Pythonian - [@Ajibel](https://twitter.com/Ajibel) - [seyipythonian@gmail.com](mailto:seyipythonian@gmail.com)
