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

## Helpful Hints for Troubleshooting

1. You might a encounter a few errors most of these will most likely be due to the fact that you misspelled something. So make sure everything is exactly the same just change where it says "rangel9697" for the dockerhub id to your own personal dockerhub id and make sure to have your dockerhub credentials set in place. You can do that by going "Manage Jenkins/Manage Credentials" there you can create your own dockerhub credentials with your username and password. That way you can pass those credentials as a environment variable for the project.

2. The second one might be that you didn't set something correctly. For this I would recommend going to your Jenkins "console output" after you build your job and it should give you a good understanding of what went wrong.

## How I set up my build image pipeline

![Screenshot 2023-05-12 163620](https://github.com/saha-rajdeep/kubernetesmanifest/assets/108555140/f0c1fa82-f4a7-4033-b205-7d7ab2e08760)


![Screenshot 2023-05-12 163648](https://github.com/saha-rajdeep/kubernetesmanifest/assets/108555140/a12bf0a2-0287-4aef-844e-306804fe5214)


## How I set up my manifest pipeline

![Screenshot 2023-05-12 164158](https://github.com/saha-rajdeep/kubernetesmanifest/assets/108555140/b6d45c53-32d2-4ff0-a0ec-c24630d48634)


![Screenshot 2023-05-12 164216](https://github.com/saha-rajdeep/kubernetesmanifest/assets/108555140/d0ef97f6-e570-4740-bc88-9c6afd7de0f5)


## How did new build images look like in Dockerhub?

![Screenshot 2023-05-12 164408](https://github.com/saha-rajdeep/kubernetesmanifest/assets/108555140/b02b0590-3085-4228-99d7-fa7179f2f055)


## How did the ArgoCD server environment look like?

![Screenshot 2023-05-11 165502](https://github.com/saha-rajdeep/kubernetesmanifest/assets/108555140/0abaed2c-b3a2-485e-8efd-c9e7561b0bc6)


1. In this next picture you can see that the "tag:10" parameter was passed in the build which was the latest build number at the time.

![Screenshot 2023-05-12 155148](https://github.com/saha-rajdeep/kubernetesmanifest/assets/108555140/662ee412-d4c5-483d-bf6f-120e18bc24a8)


