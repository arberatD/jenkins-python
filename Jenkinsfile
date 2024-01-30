pipeline {
    agent {
        node {
            label "docker-agent-python"
        }
    }
    stages {
        stage('Preparation') {
            steps {
                // Installiert Git, wenn es nicht bereits installiert ist
                sh 'apt-get update && apt-get install -y git'
            }
        }
        stage('Checkout') {
            steps {
                git 'https://github.com/arberatD/jenkins-python.git'
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r myapp/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 myapp/tests.py'
            }
        }
        stage('Run') {
            steps {
                sh 'python3 myapp/main.py'
            }
        }
    }
}
