pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo '✅ Code cloned automatically from GitHub webhook.'
                sh 'ls -la'  // Optional: Just to see files in Jenkins logs
            }
        }
        stage('Lint Check') {
            steps {
                echo '🔍 Running lint checks...'
                sh 'pylint *.py || true'  // Example for Python; adjust as needed
                // Add your linting commands here, e.g., sh 'npm run lint'
            }
        }
}