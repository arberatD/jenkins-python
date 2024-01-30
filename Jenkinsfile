pipeline {
    agent {
        node {
            label any
        }
    }
    stages {
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
