pipeline {
    agent { docker { image 'python:3.8.3' } }
    stages {
        stage('prepare') {
            steps {
                    sh 'python --version'
                }
            }
        stage('build') {
            steps {
                    sh 'python sample.py'
                }
            }
        stage('test'){
            steps{
                    sh 'puthon sampletest.py'
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