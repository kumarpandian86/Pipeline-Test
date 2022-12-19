pipeline {
  agent any
  stages {
    
    stage('Installing packages') {
            steps {
                script {
                    sh ''' python3 -V
                    sudo apt-get -qq install -y python python-virtualenv python-pip
                    pip install requests '''
                    
                }
            }
        }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
