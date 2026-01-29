pipeline {
    agent any

    environment {
        // Aqui llamamos a la herramienta que configuramos en el Paso 4
        SCANNER_HOME = tool 'scanner-tool'
    }

    stages {
        stage('Descargar Código') {
            steps {
                checkout scm
            }
        }

        stage('Análisis SonarQube') {
            steps {
                // Aqui llamamos al servidor del Paso 3
                withSonarQubeEnv('sonar-server') {
                    sh "${SCANNER_HOME}/bin/sonar-scanner"
                }
            }
        }

        stage('Construir Docker') {
            steps {
                script {
                    // Tu comando de siempre para crear la imagen
                    sh 'docker build -t python-app-fase3:latest .'
                }
            }
        }
    }
}
