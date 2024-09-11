# Solutions:

## Solution 1: High-Level Architecture Design

### Core Components:

- API Layer: Use Cloud Run or Google Kubernetes Engine (GKE) for hosting the API services. Both options are serverless or container-based, providing easy scaling for incoming requests.
- Database: Store mappings of short URLs to long URLs in Cloud Firestore (NoSQL) or Cloud SQL (relational). Firestore is ideal for fast reads and automatic scaling, while Cloud SQL works well for relational data.
- Load Balancer: Use Google Cloud Load Balancing to distribute traffic between instances of the API (Cloud Run or GKE).
- Cache: Use Cloud Memorystore (Redis) for caching frequently accessed URL mappings to reduce database lookups.

### Flow:

#### Shortening URL:

- A user sends a long URL to the /shorten API.
- The service generates a short URL, stores the mapping in the database, and returns the short URL.

#### Redirecting:

- The user accesses the short URL.
- The service looks up the long URL (from the cache or database) and redirects the user.

## Solution 2: API Design

### POST /shorten

**Request**

```json
{
  "long_url": "https://www.example.com"
}
```

**Response**

```json
{
  "short_url": "https://short.ly/abc123"
}
```

### GET /<short_url>

#### Response:

- 301 or 302 redirect to the long URL.

### Validation & Error Handling:

- Validate the input URL using Python's validators library or regex.
- Return 400 for invalid URLs, and 404 if the short URL does not exist.

### Status Codes:

- 201 for successful URL shortening.
- 301/302 for redirection.
- 400 for invalid input.
- 404 for short URL not found.

## Solution 3: Data Storage and GCP Services

### Database Design:

- Cloud Firestore (NoSQL): Ideal for high-traffic scenarios with automatic scaling and fast retrieval. Use the short URL as the primary key and store the long URL as the value.
- Cloud SQL (relational): Use an auto-incrementing ID as the primary key and store both the short and long URLs.
- Partitioning: If using Cloud SQL, partition based on URL ranges for faster access to records.
- Indexes: Create indexes on frequently queried fields (e.g., short URL) for faster lookups.

### Scalability:

- Use Firestore for seamless scalability with global distribution of data.
- Caching with Cloud Memorystore: Cache frequently accessed short-long URL pairs to reduce read load on the database.

## Solution 4: Scalability and Availability on GCP

### Load Balancing:

- Use Google Cloud Load Balancing to handle traffic distribution across multiple API instances (Cloud Run or GKE). This ensures even load distribution and handles spikes in traffic.
- Global Load Balancer: For a global-scale service, use GCP’s Global Load Balancer to route traffic to the nearest API instance, improving latency.

### Fault Tolerance:

- Deploy API instances in multiple regions for redundancy and failover. If one region becomes unavailable, the traffic will be routed to another region.

### Caching:

- Use Cloud Memorystore (Redis) for caching frequently accessed URL mappings. This helps reduce database load and improves response times for frequently used short URLs.
- Set an appropriate cache expiration policy based on the usage pattern of the URLs.
