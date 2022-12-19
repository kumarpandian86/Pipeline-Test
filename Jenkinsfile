pipeline {
  agent any
  stages {
    
    stage('Installing packages') {
            steps {
                script {
                    sh ''' apt-get -qq update && apt-get -qq install -y python3.9
                    apt-get -qq update
                    apt-get -qq install -y python python-virtualenv python-pip
                    virtualenv venv
                    . venv/bin/activate
                    python -V
                    pip install requests '''
                    
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
