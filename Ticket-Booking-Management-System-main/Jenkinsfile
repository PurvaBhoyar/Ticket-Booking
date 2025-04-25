pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/yourusername/ticket-booking.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker-compose run web python manage.py test'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
    
    post {
        always {
            sh 'docker-compose down'
        }
    }
}