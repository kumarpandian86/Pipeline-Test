pipeline {
  agent any
  stages {
    
    stage('Installing packages') {
            steps {
                script {
                    sh ''' python3 -V
                     '''
                    
                }
            }
        }
    stage('hello') {
      steps {
        sh 'python3 complaince.py'
      }
    }
  }
}
