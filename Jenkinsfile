
pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('拉取 GitHub 代码') {
            steps {
                checkout scm
            }
        }

        stage('检查 Python 环境') {
            steps {
                bat 'python --version'
            }
        }

        stage('安装依赖') {
            steps {
                bat 'if not exist .venv\\Scripts\\python.exe python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('执行 pytest 测试') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v tests --alluredir=allure-results --clean-alluredir'
            }
        }
    }

    post {
        always {
            echo '开始生成 Allure 测试报告'

            allure(
                commandline: 'allure2',
                results: [[path: 'allure-results']]
            )
        }

        success {
            echo '自动化测试执行成功！'
        }

        failure {
            echo '自动化测试执行失败！'
        }
    }
}
