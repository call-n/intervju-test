"""
## Part 1: Google Cloud Storage (GCS) Interaction

Using Python, complete the function `upload_to_gcs` that uploads a file to a Google Cloud Storage bucket.

- You will need to use the `google-cloud-storage` Python client.
- Assume that the necessary GCP credentials are already set up in your environment (via a service account key or `gcloud` CLI).

The function should:
- Take in the bucket name, the file path to be uploaded, and the destination path in the bucket.
- Upload the file to the specified bucket.

Explanation: This function uses google-cloud-storage to interact with GCS.
It uploads a file from a local path to a specified bucket and destination path on GCS.

### Task 1: Uploading a File to GCS
"""

from google.cloud import storage

def upload_to_gcs(bucket_name: str, file_path: str, destination_blob_name: str) -> None:
    """
    Uploads a file to Google Cloud Storage.
    """
    # Initialize the client
    client = storage.Client()

    # Get the bucket
    bucket = client.bucket(bucket_name)

    # Create a blob object from the file
    blob = bucket.blob(destination_blob_name)

    # Upload the file to GCS
    blob.upload_from_filename(file_path)

    print(f"File {file_path} uploaded to {destination_blob_name}.")

"""
## Part 2: Deploy a Google Cloud Function

In this part, you'll design a simple Google Cloud Function that responds to HTTP requests. This function will take in a `GET` request with a query parameter `name` and return a greeting.

- Use Python to write a cloud function handler.
- Provide the basic structure for deploying it on GCP.

Explanation: This Cloud Function extracts the name parameter from the HTTP request and returns a greeting. If no name is provided, it defaults to "World."

Deployment: The function could be deployed using the following GCP command:

### Task 2: Cloud Function
"""

def cloud_function(request):
    """
    HTTP Cloud Function that takes a 'name' query parameter and returns a greeting.
    """
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided
    return f"Hello, {name}!"


"""
# Deploy command

gcloud functions deploy cloud_function --runtime python310 --trigger-http --allow-unauthenticated
"""

"""
## Part 3: Cloud Architecture Design

### Task 3: Multi-tier Architecture

You're tasked with designing a basic multi-tier architecture using GCP services for a web application. Explain how you would structure the architecture for the following use case:

**Use Case**:
- You need to deploy a scalable web application.
- The frontend is a web client.
- The backend should handle API requests and store data in a database.
- The solution should be highly available and scalable, using Google Cloud Platform services.

### Questions:
1. **Frontend**: What GCP services would you use for hosting the frontend?
2. **Backend**: What GCP services would you use for the API server? How would you ensure scalability?
3. **Database**: Which GCP database service would you recommend and why?
4. **High Availability**: How would you ensure the system remains available during high traffic?

Answer the above questions in the comments.

Part 3: Multi-tier Cloud Architecture Design

Here are the answers for the architecture design:

Frontend:
I would use Google Cloud Storage (GCS) or Firebase Hosting for static web content (HTML, CSS, JavaScript).
Both services provide global CDN (Content Delivery Network) support for fast content delivery.

Backend:
For the API server, I’d use Google Cloud Run or Google Kubernetes Engine (GKE) for containerized applications.
Both services allow for scalable, serverless API deployments, with Cloud Run automatically scaling based on the number of incoming requests.

Database:
For the database, I’d recommend Cloud Firestore for a NoSQL solution (if the app requires real-time sync) or Cloud SQL (MySQL or PostgreSQL) for a relational database.
Firestore scales automatically, while Cloud SQL is a good choice if you need SQL-based operations.

High Availability:
To ensure high availability, I would configure Google Cloud Load Balancer to distribute traffic across multiple backend instances.
Using auto-scaling features on Cloud Run or GKE ensures the backend scales during traffic spikes.
I would also deploy resources across multiple zones for redundancy, ensuring the system remains available during outages.

"""
