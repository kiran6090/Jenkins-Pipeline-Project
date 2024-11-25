@Library('Jenkins-Shared-Library') _

pipeline {
    agent any

    environment {
        // You can add environment variables here if needed
    }

    stages {
        stage('Checkout') {
            steps {
                checkoutPipeline()  // Calls checkout.groovy
            }
        }

        stage('Run Tests') {
            steps {
                runTests()  // Calls runTest.groovy
            }
        }

        stage('Publish Reports') {
            steps {
                publishTestReports()  // Calls publishReports.groovy
            }
        }

        stage('Email Notification') {
            steps {
                sendEmailNotification()  // Calls emailNotification.groovy
            }
        }
    }
}
