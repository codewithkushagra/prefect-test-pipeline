from prefect import serve
from workflow import sequential_workflow
import os

if __name__ == "__main__":
    # Create the deployment without work pool for free tier
    deployment = sequential_workflow.to_deployment(
        name="sequential-workflow-deployment",
        description="A deployment of the sequential workflow with 3 tasks",
        tags=["demo", "sequential", "basic"],
        version="1.0.0"
    )
    
    # Check if running in CI/CD environment
    if os.getenv("GITHUB_ACTIONS"):
        # For CI/CD, just create the deployment
        deployment.apply()
        print("Deployment created successfully!")
        print("Note: This deployment will run in serverless mode on Prefect Cloud")
    else:
        # For local development, serve the deployment
        serve(deployment)
