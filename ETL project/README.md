# ETL Project – COVID Data

This is a small ETL project that **extracts, transforms, and loads COVID data**. It includes unit tests and a GitHub Actions CI workflow to automatically test changes.

### Project Structure

---

covid_etl_project/
│
├── etl.py                      # Main ETL code (functions + classes)
├── test_etl.py                 # Unit tests with pytest
├── requirements.txt            # Python dependencies
├── .github/workflows/
│ └── python-ci.yml             # GitHub Actions CI workflow
└── README.md                   # Project description

---

### Setup (Windows)

Create a virtual environment (optional but recommended):

python -m venv .venv



### Activate the virtual environment:

.\.venv\Scripts\activate


### Install dependencies:

pip install -r requirements.txt


### Running Tests

Run unit tests using pytest:

pytest -v

All tests are located in test_etl.py.
Tests are also automatically run on GitHub Actions for every push or pull request to main.


### CI/CD

The workflow .github/workflows/python-ci.yml:

Sets up Python 3.11

Installs dependencies
Runs tests automatically on push and pull requests to main
