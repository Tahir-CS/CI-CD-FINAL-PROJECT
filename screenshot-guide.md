# CI/CD Final Project Screenshot Guide

## Task 6: OpenShift PersistentVolumeClaim Screenshot (oc-pipelines-console-pvc-details.png)

### Steps:
1. Access your OpenShift console from the lab environment
2. Navigate to Administrator perspective
3. Go to Storage > PersistentVolumeClaims
4. Find your PVC named "oc-lab-pvc" 
5. Click on it to see details
6. Take a screenshot showing:
   - PVC name: oc-lab-pvc
   - Storage class: skills-network-learner
   - Size: 1GB
   - Status: Bound
7. Save as: oc-pipelines-console-pvc-details.png

## Task 7: GitHub Actions Success Screenshot (cicd-github-validate.png)

### Steps:
1. Go to your GitHub repository: https://github.com/Tahir-CS/CI-CD-FINAL-PROJECT
2. Click on "Actions" tab
3. Look for the most recent workflow run (should be green/successful)
4. Click on the workflow run to see details
5. Take a screenshot showing:
   - All steps completed successfully (green checkmarks)
   - Checkout, Install dependencies, Lint with flake8, Run unit tests with nose
6. Save as: cicd-github-validate.png

## Task 8: OpenShift Pipeline Details Screenshot (oc-pipelines-oc-final.png)

### Steps:
1. Access OpenShift console
2. Switch to Developer perspective
3. Navigate to Pipelines
4. Find your created pipeline
5. Click on it to view details
6. Take a screenshot showing:
   - Pipeline name
   - All pipeline steps: cleanup, git-clone, flake8, nose, buildah, openshift-client
   - Pipeline visualization
7. Save as: oc-pipelines-oc-final.png

## Task 9: OpenShift Pipeline Running Successfully (oc-pipelines-oc-green.png)

### Steps:
1. In OpenShift console, go to your pipeline
2. Run the pipeline (if not already running)
3. Wait for it to complete successfully
4. Take a screenshot showing:
   - All pipeline steps with green checkmarks
   - "Succeeded" status
   - Execution time and details
5. Save as: oc-pipelines-oc-green.png

## Task 10: Application Logs Screenshot (oc-pipelines-app-logs.png)

### Steps:
1. After successful pipeline deployment, go to OpenShift console
2. Navigate to Developer perspective > Topology
3. Find your deployed application pod
4. Click on the pod to view details
5. Go to "Logs" tab
6. Take a screenshot showing:
   - Application startup logs
   - Flask application running on port 5000
   - Any health check or initialization messages
7. Save as: oc-pipelines-app-logs.png

## Commands for OpenShift Setup:

### Install Tekton Tasks:
```bash
kubectl apply -f .tekton/tasks.yml
```

### Create PVC via CLI (alternative):
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: oc-lab-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: skills-network-learner
```

### Pipeline Steps to Create:
1. cleanup (uses your cleanup task)
2. git-clone (Tekton catalog task)
3. flake8 (custom task or inline script)
4. nose (uses your nose task)
5. buildah (Tekton catalog task for building container)
6. openshift-client (for deployment)

## Pipeline Parameters:
- app-name: counter-service
- build-image: image-registry.openshift-image-registry.svc:5000/your-namespace/counter-service
- git-url: https://github.com/Tahir-CS/CI-CD-FINAL-PROJECT
- git-revision: master

## Deployment Command for OpenShift Client Task:
```bash
oc create deployment $(params.app-name) --image=$(params.build-image) --dry-run=client -o yaml | oc apply -f -
```