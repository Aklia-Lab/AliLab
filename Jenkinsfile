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
          timeout(time: 1, unit: 'HOURS') {
              def qg = waitForQualityGate()
              if (qg.status != 'OK') {
                  error "Pipeline aborted due to quality gate failure: ${qg.status}"
              }
          }
      }
  stage('Test Stage'){
    docker.withServer('tcp://10.10.1.21:2376')
    def customImage = docker.build("my-image:${env.BUILD_ID}")
  }        
}
