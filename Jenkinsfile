pipeline {
  agent { label 'slave' }

  environment {
    DOCKER_IMAGE = 'tameemdevops/myapp'               // 🔁 Your DockerHub image
    DOCKER_TAG = "v${BUILD_NUMBER}"                  // 💡 Auto-incremental tag
    FULL_IMAGE = "${DOCKER_IMAGE}:${DOCKER_TAG}"
    DOCKER_REGISTRY = 'docker.io'
  }

  stages {
    stage('Checkout Code') {
      steps {
        git url: 'https://github.com/TameemZahid/Multistagewithjenkins.git', branch: 'main'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh '''
          echo "🛠️ Building Docker image: $FULL_IMAGE"
          docker build -t $FULL_IMAGE .
        '''
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds',
          usernameVariable: 'DOCKER_USER',
          passwordVariable: 'DOCKER_PASS'
        )]) {
          sh '''
            echo "🔐 Logging in to Docker Hub"
            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin

            echo "☁️ Pushing image to Docker Hub"
            docker push $FULL_IMAGE
          '''
        }
      }
    }

    stage('Deploy to MicroK8s') {
      steps {
        sshagent(['microk8s-ssh-creds']) {
          sh '''
            echo "🚀 Deploying to MicroK8s..."

            ssh -o StrictHostKeyChecking=no root@137.184.65.39 "
              microk8s.kubectl set image deployment/myapp-deploy myapp=${FULL_IMAGE} -n default &&
              microk8s.kubectl rollout status deployment/myapp-deploy -n default
            "
          '''
        }
      }
    }
  }

  post {
    success {
      echo "✅ Deployment Successful: $FULL_IMAGE"
    }
    failure {
      echo "❌ Deployment Failed"
    }
  }
}
