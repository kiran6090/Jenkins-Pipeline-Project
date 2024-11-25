def call() {
    echo "Setting up environment and running tests..."
    
    // Assuming you use virtualenv or any test environment setup
    sh 'python3 -m venv venv'
    sh 'source venv/bin/activate'
    sh 'pip install -r test/requirements.txt'
    sh 'pytest test/test_one.py test/test_two.py test/test_three.py'
}
