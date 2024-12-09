void call(Map args = [:]) {
    checkout([$class: 'GitSCM',
              branches: scm.branches,
              userRemoteConfigs: scm.userRemoteConfigs])
}

