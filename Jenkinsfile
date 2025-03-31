pipeline {
    agent none
    stages {
        stage("build and test the project") {
            agent {
                docker "python:2"
            }
            stages {
                stage('En el contenedor') {
                steps {
                    sh 'python --version'
                    }
                }
            }
        }
        stage("deploy in production") {
            agent any
            stages {
                stage('En la máquina') {
                steps {
                    sh 'python3 --version'
                    }
                }
            }
        }
    }
}
