pipeline {
    agent {
        docker {
	    alwaysPull true
            image "lordmyshepherd/jenkins-build"
            args "-e SECRET_KEY=ssssss -u root:root"
        }
    }

    stages {
        stage("1. Environment Setup") {
            steps {
                echo "The build number is ${env.BUILD_NUMBER}"
		
		sh """
		    pip install -r requirements/requirements.txt
		    sudo service mysql start
		    sudo mysql -uroot -e "UPDATE mysql.user SET authentication_string=PASSWORD('password') WHERE User='root'; FLUSH PRIVILEGES;"
		    sudo mysql -uroot -ppassword -e "CREATE DATABASE db";
                """
                }
        }
        stage("2. Build & Test") {
            steps {
                sh "python3.8 manage.py test ."
            }
        }
    }
}
// 	stage("3. Staging Deploy") {
// 	    when {
// 	        branch develop
//             }
            
//             echo "Build staging docker image with Dockerfile"
//             echo "Push docker image to registry"

// 	    echo "get ec2 ip list with aws cli"
//             echo "access to aws ec2 with aws cli"
            
//             echo "docker stop"
//             echo "docker run {line 35 pushed docker images} -d
//         }
//     }
// }