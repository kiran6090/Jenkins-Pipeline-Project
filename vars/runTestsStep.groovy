void call(Map args = [:]) {
    sh """
        source venv/bin/activate || venv\\Scripts\\activate
        pytest --maxfail=1 --disable-warnings
    """
}

