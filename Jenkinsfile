pipeline {
  agent any
  stages {
    stage('Check') {
      steps {
        sh '''virtualenv --python=python3.5 ~/venv/sassy
. ~/venv/sassy/bin/activate
pip install -r requirements.txt
tox'''
      }
    }
  }
}