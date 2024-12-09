def call() {
    stage('Publish Reports') {
        echo 'Publishing test reports...'
        // Use publishHTML to publish HTML reports
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


