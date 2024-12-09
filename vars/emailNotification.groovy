// vars/emailNotification.groovy

def call(Map config = [:]) {
    // Default email recipient if none provided
    def recipient = config.recipient ?: 'kiran.shankarmandal@in.bosch.com'
    // Attach the test report in the email
    def reportPath = config.reportPath ?: ''

    emailext(
        subject: "Build ${currentBuild.fullDisplayName} - ${currentBuild.currentResult}",
        body: "Check Jenkins for details.\nBuild URL: ${env.BUILD_URL}\n\nAdditional Info: ${config.additionalInfo ?: ''}",
        to: recipient,
        attachmentsPattern: reportPath, // Attach the report file
        mimeType: 'text/html'
    )
}
