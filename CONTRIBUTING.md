# Contributing to Gen-Z-Diaries

Thank you for your interest in contributing to Gen-Z-Diaries! This document outlines the guidelines and steps you should follow to contribute to this project.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gen-z-diaries.git
   cd gen-z-diaries
   ```

2. Install project dependencies using Pipenv:
   ```bash
   pipenv install --dev
   ```

3. Set up the database:
   - Create a PostgreSQL database for the project.
   - Configure the database connection in the `config.py` file.

4. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

5. Apply database migrations:
   ```bash
   flask db upgrade
   ```

6. Run the development server:
   ```bash
   flask run
   ```

7. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the application running.

## Contributing Guidelines

1. **Branching:**
   - Create a new branch for each feature or bug fix: `git checkout -b feature/new-feature` or `git checkout -b bugfix/fix-issue`.

2. **Coding Standards:**
   - Follow PEP 8 coding standards for Python code.
   - Maintain consistency with the existing codebase.

3. **Testing:**
   - Write tests for new features and ensure that existing tests pass.
   - Run tests locally before submitting a pull request.

4. **Documentation:**
   - Update relevant documentation for the changes you make.
   - Provide clear and concise comments within the code.

5. **Pull Requests:**
   - Submit a pull request against the `main` branch.
   - Include a clear and detailed description of your changes.
   - Reference any related issues in your pull request.

## License

By contributing to Gen-Z-Diaries, you agree that your contributions will be licensed under the [MIT License](LICENSE).

Thank you for contributing to Gen-Z-Diaries! Your help is much appreciated.
