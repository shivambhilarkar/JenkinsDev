pipeline {
    agent { 
        node {
            label 'wsl-agent'
            }
      }
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd app 
                python3 -m venv .venv
                # Use bash to activate virtual environment
                bash -c "source .venv/bin/activate && pip3 install -r requirements.txt"
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                pwd
                // sh '''
                // cd app
                // # activate virtual environment before running test
                // bash -c "source .venv/bin/activate && pip3 install -r requirements.txt"
                // pytest
                // '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}