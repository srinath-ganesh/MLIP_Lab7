pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''#!/bin/bash
                echo In C or Java, we can compile our program in this step
                echo In Python, we can build our package here or skip this step
                '''
            }
        }
        stage('Test') {
            steps {
                bat '''
                echo Test Step: Activating virtual environment and running pytest

                call mlip\\Scripts\\activate.bat
                pytest
                '''
            }
        }        
        stage('Deploy') {
            steps {
                bat '''
                echo In this step, we deploy our project
                echo Depending on the context, we may publish the project artifact or upload pickle files
                '''
            }
        }
    }
}
