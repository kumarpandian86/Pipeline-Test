pipeline {
  agent any
  stages {
    
    stage('Installing packages') {
            steps {
                script {
                    sh ''' python3 -V
                    pip3 install requests '''
                    
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
