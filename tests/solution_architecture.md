# System Design Task: URL Shortening Service on GCP

Objective: Design a scalable URL shortening service (similar to bit.ly) on Google Cloud Platform (GCP).
You will walk through high-level architecture, API design, and key components involved in building the system.

## Task 1: High-Level Architecture Design

### Design the core components of a URL shortening service on GCP.

- Consider GCP services for API, database, caching, and load balancing.
- Discuss how you would handle both creating short URLs and redirecting users from shortened URLs to the original long URLs.

### Components:

Which GCP services would you use for:

- API handling?
- Database?
- Load balancing and caching?
- Other components to consider?

## Task 2: API Design

### Design the API endpoints for the service:

1. POST /shorten: Accepts a long URL and returns a shortened URL.
2. GET /<short_url>: Redirects to the original long URL.

#### Provide details on:

- Request and response formats.
- Input validation and error handling.
- Status codes for different scenarios (e.g., success, invalid input, not found).

## Task 3: Data Storage and GCP Services

### Database Design:

- How would you store both the long and short URLs?
- Which GCP database service would you choose and why (e.g., Cloud SQL, Firestore, Cloud Spanner)?
- How would you ensure quick retrieval of the long URL when the shortened one is accessed?

### Scalability Considerations:

- How would you scale the service as the number of URLs and traffic grow?
- Would you use any caching mechanisms (e.g., Cloud Memorystore)? If so, where and why?

## Task 4: Scalability and Availability on GCP

### Load Balancing and Fault Tolerance:

- How would you use GCP services (e.g., Cloud Load Balancing, Global Load Balancer) to distribute traffic and ensure fault tolerance?

### Caching:

- How would you integrate Cloud Memorystore (Redis) for caching frequently accessed URLs?
