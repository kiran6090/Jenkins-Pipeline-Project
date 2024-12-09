@Library('Jenkins-Pipeline-Project') _


pipeline {
    agent any
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

