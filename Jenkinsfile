@Library('Jenkins-Pipeline-Project') _

pipeline {
    agent any
    environment {
        PATH = "C:\\Windows\\System32;C:\\Program Files\\Python312\\;%PATH%"
    }
    stages {
        stage('Install and Test') {
            steps {
                script {
                    runTests()  // Call the runTests function to install dependencies and run pytest
                }
            }
        }
    }
}

