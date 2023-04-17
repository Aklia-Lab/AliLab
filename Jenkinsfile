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
   
    
  stage('Deploy/build') {
        docker.withRegistry('http://192.168.1.10') {

        def customImage = docker.build("A-Lab:${env.BUILD_ID}", "./dockerfiles/test")

        /* Push the container to the custom Registry */
        customImage.push()
        customImage.push('latest')
                }
            }    

}
