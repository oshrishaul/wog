pipeline {
agent any
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/oshrishaul/wog.git'
            }
        }
        stage('build') {
            steps {
                bat 'docker-compose build'
            }
        }
        stage('run') {
            steps {
                bat 'docker-compose up &'
            }
        }
        stage('test') {
            steps {
                dir ('C:\\Users\\oshris\\PycharmProjects\\general_env\\WoG') {
                bat 'python e2e.py' }
            }
        }
    }
    post {
        always {
         bat 'docker-compose -f docker-compose.yml down'   
        }
    }
}