@Library('Jenkins-Pipeline-Project') _

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    MPLModule('Checkout', [url: scm.userRemoteConfigs[0].url])
                }
            }
        }
        stage('Setup Environment') {
            steps {
                script {
                    MPLModule('SetupEnvironment')
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    MPLModule('RunTests')
                }
            }
        }
    }
}




