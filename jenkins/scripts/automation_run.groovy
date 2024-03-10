pipeline {
    agent any
    environment {
        DEVELOPER_BRANCH = 'develop'
        BRANCH = 'Branch#1'
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

        stage("Set Pending Status") {
            steps {
                script {
                    sh 'echo "Pending"'
                }
            }
        }

        stage("Automation Process") {
            steps {
                script {
                    sh 'echo "Automation Process"'
                    sh 'echo "Branch: $(BRANCH)"'
                    sh 'echo "Developer Branch: $(DEVELOPER_BRANCH)"'
                    sh 'echo "Automation Process Completed!"'
                }
            }
        }
    }
}
