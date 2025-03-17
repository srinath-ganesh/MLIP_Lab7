pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                echo 'In C or Java, we can compile our program in this step'
                echo 'In Python, we can build our package here or skip this step'
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''#!/bin/bash
                echo 'Test Step: Running pytest in the mlip environment'

                # Initialize Conda (only needed if it's not already initialized)
                source ~/miniconda3/etc/profile.d/conda.sh
                
                # Activate the mlip environment
                conda activate mlip
                
                # Run pytest
                pytest
                
                # Remove exit 1 to allow pipeline to continue
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'In this step, we deploy our porject'
                echo 'Depending on the context, we may publish the project artifact or upload pickle files'
            }
        }
    }
}
