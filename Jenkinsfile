@Library('Jenkins-Pipeline-Project') _

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkoutStep()
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    installDependenciesStep()
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    runTestsStep()
                }
            }
        }
        stage('Publish Reports') {
            steps {
                script {
                    publishReportsStep()
                }
            }
        }
        stage('Email Notification') {
            steps {
                script {
                    emailNotificationStep()
                }
            }
        }
    }
}


