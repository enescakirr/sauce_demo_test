pipeline {
    agent any
    environment {
        DEVELOPER_BRANCH = 'develop'
        BRANCH = '${BRANCH_NAME}'
        ANSIBLE_FORCE_COLOR = 'true'
    }

    stages {

        stage("Get Branch Name") {
            steps {
                script {
                    branch = env.BRANCH
                }
            }

        }

        stage("Set Panding Status") {
            steps {
                script {
                    sh 'echo "Pending"'
                }
            }
        }

        stage("Automation Process") {
            steps {
                scripts {
                    sh 'echo "Automation Process"'
                    sh 'echo "Branch: $(BRANCH)"'
                    sh 'echo "Developer Branch: $(DEVELOPER_BRANCH)"'
                    sh 'echo "Automation Process Completed!"'
                }
            }
        }

        post {
            always {
                echo 'Automation Process finished..'
            }
        }
    }
}
