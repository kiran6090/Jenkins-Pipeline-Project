@Library('Jenkins-Pipeline-Project') _

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkoutStep() // Checkout code from the current branch
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    installDependenciesStep() // Set up the Python environment and install dependencies
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    runTestsStep() // Run the test suite
                }
            }
        }
    }
}



