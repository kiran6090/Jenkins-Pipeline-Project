@Library('Jenkins-Pipeline-Project') _

pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Function to install dependencies from requirements.txt
                    installDependencies()  // Call the installDependencies function
                }
            }
        }
        
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
    }
}

