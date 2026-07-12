#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run the test suite
pytest --webdriver Chrome

# Return the pytest exit code
exit $?