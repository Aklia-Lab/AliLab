node{
   stage('SCM Checkout'){
     git 'https://github.com/Aklia-Lab/AliLab'
  }
   stage('Test Stage'){
    sh 'echo "test"'
  }
   
 stage('SonarQube Analysis') {
    def scannerHome = tool 'a-sonar';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }

  stage("Quality Gate"){
          timeout(time: 5, unit: 'MINUTES') {
              def qg = waitForQualityGate()
              if (qg.status != 'OK') {
                  error "Pipeline aborted due to quality gate failure: ${qg.status}"
              }
          }
      }


 stage('Build docker image'){
            steps{
                script{
                    sh 'docker build -t aklialab/a-lab .'
                 }
            }
        } 
   
  stage('Push image to Hub'){
            steps{
                script{    
                   sh 'docker push aklialab/a-lab:${env.BUILD_ID}'
                }
            }
        } 
}
