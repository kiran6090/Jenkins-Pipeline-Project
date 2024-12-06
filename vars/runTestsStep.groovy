def call(Map config = [:]) {
    bat '''
        python -m venv venv
        venv\\Scripts\\activate
        pip install -r test\\requirements.txt
    '''
}

