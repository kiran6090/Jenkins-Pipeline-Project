// vars/publishTestReports.groovy
def call() {
    // Define the location of your test report (adjust the path as needed)
    def testReportPath = 'reports/test-results.xml'  // Path to your JUnit XML report

    // Archive the test reports for Jenkins to process
    junit(testReportPath)

    
}
