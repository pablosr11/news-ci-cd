pipeline {
    environment {
        REGISTRY = 'pablosr11/newscicd'
        creds = 'dockerhub'
        TAG = 'latest'
    }
    agent any
    stages {
        stage('Build docker image') {
            steps {
                script {
                    Object customImage = docker.build('pablosr11/newscicd:latest')

                    customImage.inside {
                        sh 'python -m pytest app/tests/'
                    }

                    withCredentials([string(credentialsId: 'Dockerhub-user', variable: 'USER'), string(credentialsId: 'Dockerhub-pass', variable: 'PASS')]) {
                        sh "echo $PASS | docker login --username $USER --password-stdin"
                    }

                    customImage.push()
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
        }
        stage('Run Linter') {
            steps {
                echo 'Pylint for the win'
            }
        }
        stage('Security checks and other static analysis') {
            steps {
                echo 'Security checks'
            }
        }
        stage('Run Unittests') {
            agent {
                docker { image 'python:3.8-buster' }
            }
            steps {
                sh '. venv/bin/activate && python -m pytest app/tests/'
            }
            post {
                failure {
                    echo 'Failing tests, senf notification'
                }
            }
        }
        stage('Run Functional-tests') {
            steps {
                echo 'Integration tests go here'
            }
        }
        stage('Run E2E-tests') {
            steps {
                echo 'E2E tests go here'
            }
        }

        stage('Push to docker hub') {
            steps {
                echo 'Pushing to dockerhub'
            }
        }
        stage('Stage Deployment') {
            steps {
                echo 'K8s deployment yiiiiija'
            }
        }
    }
    post {
        always {
            echo 'Remove env'
            sh 'rm -rf venv'
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
