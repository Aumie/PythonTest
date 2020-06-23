pipeline {
    agent { docker { image 'python:3.8.3' } }
    stages {
        stage('preparing') {
            steps {
                    sh 'python --version'
                    
                }
            }
        stage('building') {
            steps {
                    sh 'python --version'
                    sh 'python sample.py'
                }
            }
    }
    post{
        success {
            echo 'successful'
        }
        failure {
            echo 'failed'
        }
    }
}