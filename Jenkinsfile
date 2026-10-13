
pipeline {
    agent any

    stages {
        stage('第一阶段：检查环境') {
            steps {
                echo 'Jenkinsfile 加载成功！'
                bat 'ver'
            }
        }

        stage('第二阶段：执行测试') {
            steps {
                bat 'echo Hello Jenkinsfile!'
            }
        }

        stage('第三阶段：完成任务') {
            steps {
                echo '测试任务执行完成'
            }
        }
    }

    post {
        success {
            echo 'Jenkinsfile 流水线执行成功！'
        }

        failure {
            echo 'Jenkinsfile 流水线执行失败！'
        }
    }
}
