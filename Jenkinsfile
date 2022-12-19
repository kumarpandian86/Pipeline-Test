pipeline {
  agent any
  stages {
    
    stage('Installing packages') {
            steps {
                script {
                    sh 'apt-get -qq update && apt-get -qq install -y python3.9',
                    sh 'apt-get -qq update',
                    sh 'apt-get -qq install -y python python-virtualenv python-pip',
                    sh 'virtualenv venv',
                    sh '. venv/bin/activate',
                    sh 'python -V',
                    sh 'pip install requests'
                    
                }
            }
        }
    stage('hello') {
      steps {
        sh 'python3.9 hello.py'
      }
    }
  }
}
