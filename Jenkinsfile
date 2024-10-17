pipeline {

    agent any

    stages {

        stage("build") {

            steps {
                echo "Bulding application"
                sh 'pip install -r requirements.txt'
            }

        }

        stage("test") {

            steps {
                echo "Testing application"
                sh "python -m unittest discover tests"
            }

        }

    }

}