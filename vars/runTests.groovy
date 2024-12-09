def call() {
    // Step 1: Run tests using pytest
    echo 'Running pytest tests...'
    bat 'pytest test/ --maxfail=1 --disable-warnings -q'
}

