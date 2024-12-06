stage('Install Dependencies') {
    steps {
        script {
            bat '''
            python -m venv venv
            venv\\Scripts\\activate
            pip install -r test\\requirements.txt
            '''
        }
    }
}
