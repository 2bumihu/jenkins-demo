
pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('第一阶段：拉取代码') {
            steps {
                echo '开始拉取 GitHub 代码'
                checkout scm
            }
        }

        stage('第二阶段：检查 Python 环境') {
            steps {
                bat 'python --version'
            }
        }

        stage('第三阶段：安装依赖') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('第四阶段：执行 pytest 测试') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v tests'
            }
        }
    }

    post {
        success {
            echo 'pytest 自动化测试执行成功！'
        }

        failure {
            echo 'pytest 自动化测试执行失败！'
        }
    }
}
