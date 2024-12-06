def call(Map config = [:]) {
    emailext(
        subject: "Build ${currentBuild.fullDisplayName} - ${currentBuild.currentResult}",
        body: "Check Jenkins for details.\nBuild URL: ${env.BUILD_URL}",
        to: 'recipient@example.com'
    )
}
