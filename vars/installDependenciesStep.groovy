def call(Map config = [:]) {
    sh '''
        python3 -m venv venv
        . venv/bin/activate
        pip install -r test/requirements.txt
    '''
}
