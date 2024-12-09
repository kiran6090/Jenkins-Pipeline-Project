def call() {
    // Step 1: Run the specific pytest test file 'test/test_api.py'
    echo 'Running pytest tests for test/test_api.py...'
    bat '''
        pytest test/test_api.py --html=test-reports/html/index.html --self-contained-html --maxfail=1 --disable-warnings -q
    '''
}



