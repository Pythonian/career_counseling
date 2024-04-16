# Career Compass

![Career Compass Hero Section](docs/hero.jpeg)

![Static Badge](https://img.shields.io/badge/Owner-Pythonian-green)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Pythonian/career_counseling)
![GitHub last commit](https://img.shields.io/github/last-commit/pythonian/career_counseling)
![GitHub top language](https://img.shields.io/github/languages/top/pythonian/career_counseling)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/pythonian/career_counseling)
![GitHub contributors](https://img.shields.io/github/contributors/pythonian/career_counseling)
![GitHub Repo stars](https://img.shields.io/github/stars/pythonian/career_counseling)
![GitHub forks](https://img.shields.io/github/forks/pythonian/career_counseling)

## Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  * [Requirements](#requirements)
  * [Tech Stacks](#tech-stacks)
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
   make populatedb
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
   *include settings configuration*

## Running Tests

To run tests, run the following command

```bash
   make test
```

## Contributing

Contributions are always welcome!

Please see [the contributing guide](docs/CONTRIBUTING.md) for ways to get started.

## Support

If you encounter any bug or problem while using the project, please [open an issue](https://github.com/Pythonian/career_counseling/issues)

## Changelog

For a detailed list of changes, see the [Changelog](docs/CHANGELOG.md).

## License

This project is licensed under the [MIT License](LICENSE.md).

## Contact

If you have any questions, suggestions, or feedback, feel free to reach out to me

Seyi Pythonian - [@Ajibel](https://twitter.com/Ajibel) - seyipythonian@gmail.com
