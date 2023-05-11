## Jenkins pipeline with GitOps to deploy to our Kubernetes Cluster

1. To get a better understanding of this project let's make a scenerio. So as a developer you will create a app.py file that you will push to a repo nmamed my_kubernetescode. That file will trigger a Jenkins job that will build an image with a builder tag and push it to our dockerhub repo. Now you also have another repository named my_kubernetesmanifest that has a deployment.yaml file that will reference the our newly build image with the latest tag. So this is done by our second Jenkins job that will automatically update the image in our deployment.yaml file. So we take care of the CD part by using ArgoCD. In this case ArgoCD will be monitoring my_kubernetesmanifest repo, so whenever there's an update or change it will match our Kubernetes cluster to it matches the deployment.yaml file.

2. Now the first time this run it ArgoCD will notice that there are no containers in our Kubernetes cluster so it will create them for us. But what happens when it gets triggered again by a changed made in our app.py file? Well when we push an updated app.py file the first Jenkins job will be triggered and build a new dockerimage with a new tag this job will simultaneously trigger our second Jenkins job and update the deployment.yaml file with the docker image with our new tag. Then ArgoCD will detect a change in our my_kubernetesmanifest repo and destroy our contaienr with the previous tag and create a new one with the new tag.

3. So in this project we are doing the continous intergration CI with the Jenkins jobs and the continous deployment CD with ArgoCD. Now the benefits of GitOps is substantial because if we were to do this traditionally with regular CI/CD we would have our second Jenkins job directly push our deployment.yaml changes to our Kubernetes cluster in a extra step. Well the disadvantage here is that we would need some type of notification system or step to keep monitoring our Kubernetes cluster to detect any changes. Similarly if anyone deletes our Kubernetes containers or cluster we would have to manually restore it back to the previous version. So this is where the power of GitOps really shines through. With GitOps our repository is our single source of truth so anytime our Kubernetes cluster and our repository don't match GitOps will restore it so they're both matching!

## Setting up our environment

1. You will need the following tools installed in your computer or VM:

* Jenkins
* Docker
* Kubernetes
* EKS
* ArgoCD
* Git

2. I will not go in extensive detail on how install most of these tools. You can always search how to install them and follow the website's steps. However, because I had a lot of diffficulty trying to install ArgoCD using the website I will post the following.

3. If you go to https://argo-cd.readthedocs.io/en/stable/getting_started/ on the first step. The link they have you download doesn't contain the argocd-server package. Instead follow this link for the first step: https://github.com/argoproj/argo-cd/releases/latest and the go back to the main website and follow the rest of the steps I recommend you use port forwarding to access ArgoCD. Besides that you should be ready to go!