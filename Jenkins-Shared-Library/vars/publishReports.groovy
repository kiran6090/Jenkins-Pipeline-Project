def call() {
    echo "Publishing test results..."
    junit '**/target/test-*.xml'  // Adjust according to your test result location
}
