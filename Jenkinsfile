pipeline {

    agent any

    stages {

        stage("build") {

            steps {
                echo "Bulding application"
                sh 'docker build -t test-app:latest .'
            }

        }

        stage("test") {

            steps {
                echo "Testing application"
                sh "docker run --rm test-app:latest python -m unittest discover tests"
            }

        }

    }

    post {
        success {
            echo "Pipeline completed successully."
        }
        failure {
            echo "Pipeline failed."
        }
    }

}