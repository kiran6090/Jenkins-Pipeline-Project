def call() {
    // Step 1: Run tests using pytest
    echo 'Running pytest tests...'
    bat 'pytest tests/ --maxfail=1 --disable-warnings -q'
}

