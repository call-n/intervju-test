# Answers to Devops questions

## Terraform

### How do you manage state in Terraform when working in a team environment? What challenges have you faced, and how did you address them?

**Answer:** I used remote state storage with GCS (Google Cloud Storage) and a state locking mechanism via Google’s Bucket Object Versioning.
This approach prevents conflicts when multiple engineers work on the same project simultaneously.
One challenge we encountered was state file corruption due to improper handling during parallel runs.
To address this, I ensured proper state locking by configuring the backend to use a consistent locking strategy and implemented policies to prevent team members from running terraform apply without reviewing potential changes.

### Have you worked with remote backends for storing Terraform state? Can you explain how you would set one up in GCP or AWS?

**Answer:** Yes, I’ve set up remote backends in both GCP and AWS. In GCP, I created a GCS bucket to store the state file, set up IAM roles to control access, and configured versioning for backup. The backend configuration looked like this:

```hcl
backend "gcs" {
bucket = "my-terraform-state-bucket"
prefix = "terraform/state"
}
```

**In AWS**, I used an S3 bucket with DynamoDB for state locking. The configuration was similar, but using AWS resources:

```hcl
backend "s3" {
bucket = "my-s3-bucket"
key = "state/terraform.tfstate"
region = "us-west-2"
dynamodb_table = "terraform-lock"
}
```

### Describe a situation where you had to troubleshoot a Terraform deployment. What was the issue, and how did you solve it?

**Answer:** In one case, a Terraform deployment failed because of cyclic dependencies between IAM roles and service accounts.
The roles and accounts depended on each other, causing the deployment to fail.
I solved this by breaking the Terraform configurations into separate modules and using depends_on to explicitly manage the dependency order.
Additionally, I used the terraform graph command to visualize the resource dependencies and pinpoint where the cycle occurred.

## GitHub & GitHub Actions:

### How do you implement CI/CD pipelines using GitHub Actions? Can you provide an example where you optimized the workflow for a project?

**Answer:** I implemented CI/CD pipelines in GitHub Actions by setting up a YAML workflow file that would trigger on each commit to the repository.
I used actions like actions/checkout@v2 to pull the code, docker/build-push-action for building Docker images, and custom scripts for testing and deploying to GKE.
In a specific project, I optimized the pipeline by parallelizing test jobs and caching dependencies, which reduced the overall build time by 30%.

Here’s an example of a simple workflow:

```yaml
jobs:
build:
runs-on: ubuntu-latest
steps: - uses: actions/checkout@v2 - name: Build Docker Image
run: docker build -t my-app . - name: Deploy to GKE
run: kubectl apply -f deployment.yaml
```

### How do you handle secrets in GitHub Actions? What strategies would you recommend to secure sensitive data?

**Answer:** In GitHub Actions, I use the built-in secrets management system to securely store sensitive information like API keys, tokens, and credentials.
Secrets are encrypted at rest and can be accessed using secrets.<SECRET_NAME> within the workflows.
To further enhance security, I recommend rotating secrets periodically, restricting their usage to specific environments, and using GitHub’s environment protection rules to ensure sensitive actions are only run in a trusted context.

### What are some best practices when using Git and GitHub in a multi-environment setup (e.g., dev, test, prod)?

**Answer:** Best practices include:
Using branches for each environment (dev, test, prod) to ensure isolation of changes.
Implementing protected branches and requiring pull requests with approvals before merging.
Automating environment-specific deployments using CI/CD tools, such as GitHub Actions.
Managing configuration with environment variables and secrets, so that each environment has its own settings.
Tagging releases to track production deployments and revert easily if needed.

### Explain how you would set up a workflow that deploys a containerized application to GKE using GitHub Actions.

**Answer:** I would set up a GitHub Actions workflow that builds the Docker image, pushes it to Google Container Registry (GCR), and then deploys the application to GKE. Here’s an example of how this can be done:

```yaml
jobs:
deploy:
runs-on: ubuntu-latest
steps: - uses: actions/checkout@v2 - name: Set up Google Cloud SDK
uses: google-github-actions/setup-gcloud@v0
with:
project_id: ${{ secrets.GCP_PROJECT_ID }}
          credentials: ${{ secrets.GCP_CREDENTIALS }}
      - name: Build Docker Image
        run: docker build -t gcr.io/${{ secrets.GCP_PROJECT_ID }}/my-app:$GITHUB_SHA .
      - name: Push to Google Container Registry
        run: docker push gcr.io/${{ secrets.GCP_PROJECT_ID }}/my-app:$GITHUB_SHA
      - name: Deploy to GKE
        run: |
          gcloud container clusters get-credentials my-cluster --zone us-central1
          kubectl set image deployment/my-app my-app=gcr.io/${{ secrets.GCP_PROJECT_ID }}/my-app:$GITHUB_SHA
```

## Google Cloud:

### Can you explain how Workload Identity works in GKE and why it’s essential for securing Kubernetes workloads?

**Answer:** Workload Identity allows Kubernetes pods to automatically authenticate to Google Cloud services without needing service account keys.
It works by mapping Kubernetes service accounts to Google service accounts, allowing workloads to use IAM roles securely.
This eliminates the need for long-lived credentials and reduces security risks from key mismanagement.
Workload Identity ensures that each workload has the minimum necessary permissions to interact with Google Cloud services.

### Describe a situation where you had to troubleshoot a production issue in GCP. What tools did you use, and how did you resolve the issue?

**Answer:** During the Application Migration project, I encountered an issue where a GKE deployment was failing due to misconfigured firewall rules that blocked traffic between the app and its database.
I used Google Cloud Monitoring to view logs and metrics, and Stackdriver (now part of Google Cloud Operations Suite) to trace the network flows.
After identifying the blocked traffic, I adjusted the firewall rules and reconfigured network policies to allow the required communication.

### How do you monitor and optimize performance for a Kubernetes cluster in GKE?

**Answer:** I use Google Cloud Monitoring and Prometheus to gather metrics on cluster performance, such as CPU/memory utilization, pod health, and network traffic.
Alerts are configured for key thresholds like high resource usage.
To optimize performance, I scale the cluster automatically based on resource demand using GKE’s autoscaling features.
I also review pod resource requests and limits regularly to ensure optimal utilization and cost efficiency.

## Independence & Problem-Solving:

### Can you give an example of a project where you worked independently to solve a complex issue?

**Answer**: no clear answer here.

### How do you prioritize tasks when managing multiple cloud infrastructure projects simultaneously?

**Answer:** I prioritize tasks by balancing urgency and impact.
I start by breaking projects into smaller deliverables, then use tools like Jira to track progress and assign deadlines.
For critical issues (like production outages), I address them immediately.
I also ensure clear communication with stakeholders to set expectations and adjust timelines when necessary, focusing on high-impact deliverables that align with business goals.
