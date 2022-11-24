pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Riddhi-Chatterjee/SE-Assignment-6'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Division.py"
                sh "./Division.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}