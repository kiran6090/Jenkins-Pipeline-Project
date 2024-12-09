def call(Map config = [:]) {
    sh '''
        python -m venv venv
        venv\\Scripts\\activate
        pip install -r test\\requirements.txt
    '''
}

