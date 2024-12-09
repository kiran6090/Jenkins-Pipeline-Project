void call(Map args = [:]) {
    sh """
        python -m venv venv
        source venv/bin/activate || venv\\Scripts\\activate
        pip install -r requirements.txt
    """
}
