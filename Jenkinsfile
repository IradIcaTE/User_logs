pipeline {
    agent { label "First" }

    stages {
        stage("Run Python Script") {
            steps {
                echo "Running Pythong script to log user info"
                sh 'echo -e "Parth\\nparth@example.com" | python3 user_logger.py'
            }
        }

        stage ('Archive Outout') {
            steps {
                archiveArtifacts artifacts: "user_info.txt", onlyIfSuccessful: true
            }
        }
    }
}