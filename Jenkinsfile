pipeline {
  agent any
  stages {
    
    stage('Installing packages') {
            steps {
                script {
                    sh ''' python3 -V
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
