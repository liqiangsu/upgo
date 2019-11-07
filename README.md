
# UPGO

## What it is
  
cloud-aimed service management command-tool.
similar to npm, docker compose, sls....

## Pain Point Resolved
### Reusability:
No needs to repeat youself when start a new project on aws cloud.
For example, user authentication and authrization that is widely used in most of project can be reused 
just by typing upgo install myproj user-authz
 
### Business Logic Centric:
Users do not need to worry about iam,auditing, security, monitoring, deploying, account isolation.
For example, upgo install myproj user-authz --with-git-repo will clone user-authz to your local drive.
you can modify the cloudformation.yaml and business-logix codes to cater for your specific needs.
 
### Multi-Accounts
Each app installed by upgo has it own aws account, git-repo and deploy piplines - dev,qa and prod.
the account will be automatically mananged by upgo by the use of AWS  organazations.
 
## How it should be use
upgo init
upgo search project/app
upgo create project/app
upgo install project/app
upgo show project/app
upgo update project/app 

## Features
1. Each project is represented as one OU.
2. Each project contains multi apps
3. Each app is represented as one account attached to project OU.
4. Each app is a complete solution that incudes different aws services. eg aws pipline, iam roles, codes.
5. App/Project are reuasable and can be downloaded.


# Development note
## build
### Prepare
```console
> python -m pip install --upgrade pip setuptools wheel tqdm
> python -m pip install --user --upgrade twine
```

### Build command
```console
> python setup.py bdist_wheel
```
Artifacts will be generated under "dist" directory

### Test local
```console
# To install 
> python install dist/[package].whl

# To run
> upgo
```
