// vars/runTests.groovy
def call() {
    // Step 1: Create and activate the virtual environment, install pytest
    echo 'Creating and activating virtual environment...'
    bat '''
        python -m venv venv
        .\\venv\\Scripts\\activate
        pip install pytest
        pip show pytest  REM Check if pytest is installed successfully
    '''
    
    // Step 2: Run the specific pytest test file 'test/test_api.py' in the same shell session
    echo 'Running pytest tests for test/test_api.py...'
    bat '''
        .\\venv\\Scripts\\activate && pytest --version && pytest test/test_api.py --maxfail=1 --disable-warnings -q
    '''
}

