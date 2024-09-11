"""
# Google Cloud Platform (GCP) - Python Task

This exercise is designed to test your understanding of key GCP services, how to interact with them programmatically, and how to design cloud-based solutions.

You will need to complete tasks involving:
1. Uploading and downloading files from Google Cloud Storage (GCS).
2. Deploying a simple Google Cloud Function.
3. Designing a multi-tier architecture using GCP services.

---

## Part 1: Google Cloud Storage (GCS) Interaction

Using Python, complete the function `upload_to_gcs` that uploads a file to a Google Cloud Storage bucket.

- You will need to use the `google-cloud-storage` Python client.
- Assume that the necessary GCP credentials are already set up in your environment (via a service account key or `gcloud` CLI).

The function should:
- Take in the bucket name, the file path to be uploaded, and the destination path in the bucket.
- Upload the file to the specified bucket.

### Task 1: Uploading a File to GCS
"""

from google.cloud import storage

# TODO: Task 1 - Upload to GCS
def upload_to_gcs(bucket_name: str, file_path: str, destination_blob_name: str) -> None:
    """
    Uploads a file to Google Cloud Storage.

    Parameters:
    - bucket_name: Name of the GCS bucket
    - file_path: Local path to the file to be uploaded
    - destination_blob_name: The name of the file in GCS (destination path)

    Example:
    upload_to_gcs('my-bucket', 'local-file.txt', 'remote/path/file.txt')
    """
    # Your code here:
    pass


"""
## Part 2: Deploy a Google Cloud Function

In this part, you'll design a simple Google Cloud Function that responds to HTTP requests. This function will take in a `GET` request with a query parameter `name` and return a greeting.

- Use Python to write a cloud function handler.
- Provide the basic structure for deploying it on GCP.

### Task 2: Cloud Function
"""

# TODO: Task 2 - Cloud Function
def cloud_function(request):
    """
    HTTP Cloud Function that takes a 'name' query parameter and returns a greeting.

    Example:
    - Input: GET /?name=John
    - Output: "Hello, John!"

    Returns:
    - A greeting string based on the 'name' query parameter.
    """
    # Your code here:
    pass


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
"""

# TODO: Task 3 - Architecture Design
# Provide your answers here:
