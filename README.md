# Counter Service - CI/CD Final Project

This is a RESTful API microservice for managing and tracking counters, built as part of the CI/CD final project.

## Features

- Create, read, update, and delete counters
- Increment and decrement counter values
- Health check endpoint
- Comprehensive unit tests
- CI/CD pipeline with GitHub Actions and Tekton

## API Endpoints

- `GET /health` - Health check
- `GET /counters` - Get all counters
- `GET /counters/<name>` - Get a specific counter
- `POST /counters/<name>` - Create a new counter
- `PUT /counters/<name>/increment` - Increment a counter
- `PUT /counters/<name>/decrement` - Decrement a counter
- `DELETE /counters/<name>` - Delete a counter

## CI/CD Pipeline

### GitHub Actions (Continuous Integration)

The CI pipeline includes:
1. Checkout code
2. Install dependencies
3. Run Flake8 linting
4. Run unit tests with nose

### Tekton Pipelines (Continuous Deployment)

The CD pipeline includes:
1. Cleanup workspace
2. Git clone
3. Flake8 linting
4. Nose tests
5. Build container image with Buildah
6. Deploy to OpenShift

## Running the Application

```bash
python service/app.py
```

## Running Tests

```bash
nosetests -v --with-spec --spec-color --with-coverage --cover-package=app
```

## Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `nosetests`
4. Start the service: `python service/app.py`