// vars/runTests.groovy
def call() {
    // Step 1: Run the specific pytest test file 'test/test_api.py'
    echo 'Running pytest tests for test/test_api.py...'
    sh 'pytest test --maxfail=1 --disable-warnings -q '    
}


