pipeline {
    agent any

    environment{
          App_Version = 1.1.0
          Deploy_New = "Stagging"
    }

    stages {
        stage('Build') {
            steps {
                echo "building App version ${App_Version}"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying to ${Deploy_New} environment"
            }
        }
    }
}
