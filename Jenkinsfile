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
        stage('Pass Test Code') {
            steps {
                sh "chmod u+x PassTestCases.py"
                sh "./PassTestCases.py"
            }
        }
        stage('Fail Test Code') {
            steps {
                sh "chmod u+x FailTestCases.py"
                sh "./FailTestCases.py"
            }
        }
    } 
}