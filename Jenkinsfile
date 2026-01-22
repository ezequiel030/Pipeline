pipeline {
    agent any

    stages {
        stage('Construir') {
            steps {
                // Comando para construir la imagen de Docker [cite: 264]
                sh 'docker build -t fase2-jenkins .'
            }
        }
        stage('Comprobar') {
            steps {
                // Mensaje de confirmación en el log de Jenkins [cite: 275]
                echo 'La imagen se ha creado bien! Todo correcto.'
            }
        }
    }
}
