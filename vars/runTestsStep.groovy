def call(Map config = [:]) {
    sh '''
        . venv/bin/activate
        pytest test/ --junitxml=reports/results.xml
    '''
}
