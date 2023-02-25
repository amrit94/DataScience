## Deployment
* Deployed on AWS using
    * Elastic Beanstalk
    * CodePipeline

### Steps
1. Push code to github
2. Create: Beanstalk Web App
```
1. App Name
2. Platform
    * Python
    * Python 3.7
    * Next
3. Application code
    * Sample application
```
3. Create: CodePipeline
```
1. Pipeline Name
2. Source: Github version-1
    * Select: Repo
    * Select: Branch
    * Next
3. Skip build stage
4. Deploy: AWS BeanStalk
    * Select: App Name
    * Select: Eve Name
    * Next
5. Create pipeline
```

### Error
* Elastic Beanstalk 502 Bad Gateway Error
    * https://thebeebs.net/2021/02/02/elastic-beanstalk-502-bad-gateway-error/