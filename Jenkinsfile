@Library('Jenkins-Shared-Library') _

import Utils.HelloWorld

pipeline {
    agent any
    stages {
        stage('Test Library') {
            steps {
                script {
                    echo 'Library loaded successfully!'
                    
                    // Use the class from src/
                    def greeting = HelloWorld.greet('Jenkins User')
                    echo greeting
                }
            }
        }
    }
}

