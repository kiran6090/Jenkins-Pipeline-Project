@Library('Jenkins-Pipeline-Project') _

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from the repository
                    MPLModule('Checkout', [url: scm.userRemoteConfigs[0].url])
                }
            }
        }
        stage('Setup Environment') {
            steps {
                script {
                    // Set up the Python environment and install dependencies
                    MPLModule('SetupEnvironment')
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run tests in the virtual environment
                    MPLModule('RunTests')
                }
            }
        }
    }
}



