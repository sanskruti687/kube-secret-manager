pipeline {
    agent any

    environment {
        REGISTRY = "sanskrutipawar"  // Your DockerHub username
        IMAGE_NAME = "internship-app"
        IMAGE_TAG = "latest"
        DOCKER_USERNAME = credentials('docker-username')  // Stored in Jenkins credentials
        DOCKER_PASSWORD = credentials('docker-password')  // Stored in Jenkins credentials
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $REGISTRY/$IMAGE_NAME:$IMAGE_TAG ."
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                    sh "docker push $REGISTRY/$IMAGE_NAME:$IMAGE_TAG"
                }
            }
        }
    }
}
