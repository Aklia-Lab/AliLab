node{
   def app
   
   stage('SCM Checkout'){
     git 'https://github.com/Aklia-Lab/AliLab'
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
   
   stage('Test') {
      agent { dockerfile true }
            steps {
                sh 'node --version'
                sh 'svn --version'
            }
        }
   
 stage('Build image') {
        app = docker.build("a-lab/pyapp")
    }  
   
 stage('Push image') {
        docker.withRegistry('https://registry.aaklia.com') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}
