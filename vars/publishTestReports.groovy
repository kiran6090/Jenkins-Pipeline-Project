def call() {
    // Publish JUnit test results
    junit '**/reports/test-results.xml'

    // Archive the reports for later use
    archiveArtifacts artifacts: 'reports/test-results.xml', allowEmptyArchive: true
}



