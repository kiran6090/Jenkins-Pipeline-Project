def call() {
    stage('Publish Reports') {
        steps {
            echo 'Publishing test reports...'
            // Adjust the paths and tools based on your test framework and report type
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'test-reports/html',
                reportFiles: 'index.html',
                reportName: 'Test Report'
            ])
        }
    }
}

