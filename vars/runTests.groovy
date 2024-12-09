// vars/runTests.groovy
def call() {
    // Step 1: Create and activate a virtual environment
    echo 'Creating and activating virtual environment...'
    bat '''
        python -m venv venv
        .\\venv\\Scripts\\activate
        pip install pytest
    '''
    
    // Step 2: Run the specific pytest test file 'test/test_api.py'
    echo 'Running pytest tests for test/test_api.py...'
    bat '''
        .\\venv\\Scripts\\activate
        pytest test/test_api.py --maxfail=1 --disable-warnings -q
    '''
}


