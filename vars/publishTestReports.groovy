def call() {
    // Step 2: Generate the test report
    echo 'Generating test report...'
    sh 'pytest --junitxml=reports/test-results.xml'
}



