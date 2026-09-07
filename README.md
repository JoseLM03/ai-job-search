# AI Job Search

A Python-based job search pipeline that collects job postings from the Adzuna API, normalizes the returned data into structured job objects, and filters listings based on user-defined job preferences.

## V1 Overview

AI Job Search V1 focuses on building a reliable foundation for an automated job search system.

The V1 pipeline:

1. Collects job postings from the Adzuna API
2. Normalizes external API responses into a consistent structure
3. Represents jobs using a structured `Job` model
4. Defines user search preferences using `UserPreferences`
5. Filters jobs based on desired roles, work arrangements, location, and employment types
6. Uses role aliases to improve job-title matching
7. Returns relevant jobs through a reusable pipeline
8. Includes automated tests for core components

V1 does not use an LLM. AI-powered analysis is outside the scope of this version.

## Pipeline Architecture

```text
Adzuna API
    |
    v
Collector
    |
    v
Raw Job Data
    |
    v
Normalizer
    |
    v
Job Model
    |
    v
Job Filtering
    |
    +--> Role Matching
    |
    +--> Location Matching
    |
    +--> Work Arrangement Matching
    |
    +--> Employment Type Matching
    |
    v
Relevant Jobs
```

## Tech Stack

* Python
* Adzuna REST API
* JSON
* Pytest
* Git
* GitHub
* Linux / WSL
* Python Virtual Environment

## Project Structure

```text
ai-job-search/
├── README.md
├── api_test_manual.py
├── pyproject.toml
├── run_pipeline.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── pipeline.py
│   ├── collectors/
│   │   ├── __init__.py
│   │   └── adzuna.py
│   ├── filters/
│   │   ├── __init__.py
│   │   ├── job_filter.py
│   │   └── role_aliases.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── job.py
│   │   └── user_preferences.py
│   └── normalizers/
│       ├── __init__.py
│       └── adzuna.py
└── tests/
    ├── test_adzuna.py
    ├── test_filter.py
    ├── test_job.py
    └── test_pipeline.py
```

## Core Components

### Adzuna Collector

`src/collectors/adzuna.py`

Handles communication with the Adzuna API and retrieves job posting data.

### Job Model

`src/models/job.py`

Defines the structured representation of a job after the external API data has been processed.

### User Preferences

`src/models/user_preferences.py`

Defines the preferences used to determine which jobs are relevant.

Current preferences include:

* Desired roles
* Work arrangements
* Location
* Maximum commute time
* Employment types

### Adzuna Normalizer

`src/normalizers/adzuna.py`

Converts Adzuna job responses into the application's standardized job structure.

### Job Filtering

`src/filters/job_filter.py`

Determines whether a job matches the configured user preferences.

V1 supports filtering by:

* Job role
* Location
* Work arrangement
* Employment type

### Role Aliases

`src/filters/role_aliases.py`

Provides alternate job-title terms for desired roles so that searches can match related titles.

For example, a desired role can be associated with multiple equivalent or related job-title terms.

### Pipeline

`src/pipeline.py`

Connects the collection, normalization, and filtering stages into a reusable job-search pipeline.

### Configuration

`src/config.py`

Provides application configuration and default user preferences.

## Running the Pipeline

### 1. Clone the repository

```bash
git clone https://github.com/JoseLM03/ai-job-search.git
cd ai-job-search
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

This creates an isolated Python environment for the project's dependencies.

### 3. Activate the virtual environment

On Linux/WSL:

```bash
source .venv/bin/activate
```

### 4. Install the project

Install the project's dependencies according to the configuration defined in `pyproject.toml`.

### 5. Configure Adzuna credentials

The application requires Adzuna API credentials.

Store the required credentials in the project's environment configuration rather than committing secrets to GitHub.

### 6. Run the pipeline

```bash
python run_pipeline.py
```

The pipeline collects jobs, applies the configured preferences, and prints the relevant results.

Example output format:

```text
Found X relevant jobs:

Software Engineer | Company | Location | Remote | Salary | Employment Type | URL
```

## Testing

Run the automated test suite with:

```bash
pytest
```

V1 includes tests covering:

* Adzuna API behavior
* Job model behavior
* Job filtering
* Pipeline behavior

The test suite helps verify that individual components and the overall pipeline continue to behave as expected.

## Manual API Testing

The project also includes:

```text
api_test_manual.py
```

This script provides a way to manually test the Adzuna API integration outside of the automated test suite.

## V1 Features

* Adzuna API integration
* Job data collection
* Job data normalization
* Structured job model
* User preference model
* Role-based filtering
* Role aliases
* Location filtering
* Work arrangement filtering
* Employment type filtering
* Reusable job-search pipeline
* Automated pytest test suite
* Manual API testing
* Environment-based configuration

## V1 Scope

V1 is intentionally focused on the data collection and filtering foundation of the application.

The current version does not include:

* LLM-powered job analysis
* Resume matching
* AI-generated job insights
* Job ranking/scoring
* Persistent database storage
* User accounts
* Web interface
* Automated job applications

## Project Status

**Version: 1.0.0**

AI Job Search V1 establishes the core pipeline for collecting, normalizing, and filtering job postings based on user preferences.

The project is being developed incrementally, with each version introducing additional software engineering concepts and capabilities.
