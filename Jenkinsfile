pipeline {
    environment {
        REGISTRY = 'pablosr11/newscicd'
        TAG = '0.0.1'
    }
    agent any
    stages {
        stage('Build docker image') {
            steps {
                script {
                    docker.build("${REGISTRY}:${TAG}")
                }
            }
        }
        stage('Language specific security checks') {
            steps {
                script {
                    docker.image("${REGISTRY}:${TAG}").inside {
                        sh 'echo PYTHON SECURITY CHECKS'
                    }
                }
            }
        }
        stage('Container security checks') {
            steps {
                script {
                    docker.image("${REGISTRY}:${TAG}").inside {
                        sh 'echo CONTAINER WIDE CHECKS'
                    }
                }
            }
        }
        stage('Run Linter') {
            steps {
                script {
                    docker.image("${REGISTRY}:${TAG}").inside {
                        sh 'python -m pylint app/'
                    }
                }
            }
        }
        stage('Run test') {
            steps {
                script {
                    docker.image("${REGISTRY}:${TAG}").inside {
                        sh 'python -m pytest app/tests/'
                    }
                }
            }
            post {
                failure {
                    echo 'Failing tests, senf notification'
                }
            }
        }
        stage('Push Image') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'Dockerhub-user', variable: 'USER'), string(credentialsId: 'Dockerhub-pass', variable: 'PASS')]) {
                        sh "echo $PASS | docker login --username $USER --password-stdin"
                    }
                    docker.image("${REGISTRY}:${TAG}").push()
                }
            }
        }
        stage('Build helm charts with new version etc') {
            agent {
                docker { image 'alpine/helm:2.16.9' }
            }
            steps {
                sh 'helm lint k8s/'
            }
        }
        stage('Run Functional-tests') {
            steps {
                echo 'Integration tests go here'
            }
        }
        stage('Stage Deployment') {
            steps {
                echo 'K8s deployment yiiiiija'
            }
        }
        stage('Run E2E-tests') {
            steps {
                echo 'E2E tests go here'
            }
        }
        stage('Production Deployment') {
            steps {
                echo 'K8s deployment yiiiiija'
            }
        }
    }
    post {
        always {
            echo 'Always runs'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
