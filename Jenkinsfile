pipeline {

    agent any
    
    environment {
        IMAGE_NAME = "jenkins-python-docker"
        CONTAINER_NAME = "jenkins-python-container"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from your Git repository
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the current directory
                    sh 'docker build -t ${IMAGE_NAME} .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the tests inside the Docker container
                    sh '''
                    docker run --name ${CONTAINER_NAME} ${IMAGE_NAME} sh -c "python -m unittest discover"
                    '''
                }
            }
        }
    }

    post {
        always {
            // Cleanup: Remove the container after tests are complete
            sh 'docker rm -f ${CONTAINER_NAME} || true'
        }
    }

}