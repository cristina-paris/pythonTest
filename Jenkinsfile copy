pipeline {
    agent {
        docker { image 'python:3' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python test_utils.py'
            }
        }
    }
}