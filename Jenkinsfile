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
        def docker = "docker"
        docker.withRegistry('http://192.168.1.10:5000') {

        def customImage = docker.build("A-Lab:${env.BUILD_ID}")

        /* Push the container to the custom Registry */
        customImage.push()
        customImage.push('latest')
                }
            }    

}
