pipeline{
    agent any 
    stages {
        stage('setup') {
            steps {
                echo "installing dependencies"
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('build and test') {
            steps {
                echo "running ml pipeline"
                bat 'python ml_pipeline.py'
            }
        }
    }
    post {
        success {
            echo 'pipeline Success -model validated'
        }
        failure {
            echo 'pipeline failed -model validation failed'
        }
    }
}