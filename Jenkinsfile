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
                echo '🔍 Running pylint...'
                sh 'pylint *.py || true'
            }
        }
    }
}