def call() {
    // Step 1: Install dependencies
    echo 'Installing dependencies from requirements.txt...'
    sh 'pip install -r requirements.txt'

    // Step 2: Run tests using pytest
    echo 'Running pytest tests...'
    sh 'pytest tests/ --maxfail=1 --disable-warnings -q'
}
