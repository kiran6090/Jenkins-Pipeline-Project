@Library('Jenkins-Pipeline-Project') _

pipeline {
    agent any
    environment {
        PATH = "C:\\Windows\\System32;C:\\Program Files\\Python312\\;C:\\Program Files\\Python312\\Scripts\\;%PATH%"
    }
    stages {
        stage('Install and Test') {
            steps {
                script {
                    runTests()  // Call the runTests function to install dependencies and run pytest
                }
            }
        }
        stage('Publish Reports') {
            steps {
                script {
                    publishTestReports()  // Call the function to publish the test reports
                }
            }
        }
        stage('Send Email with Report') {
            steps {
                script {
                    // Define the test report path
                    def reportPath = "${env.WORKSPACE}\\reports\\test-results.xml"
                    // Send email with the report
                    sendEmailNotification(
                        recipient: 'kiran.shankarmandal@in.bosch.com',
                        additionalInfo: "The test report is attached. Please find the report at: ${reportPath}"
                    )
                }
            }
        }
    }
}


