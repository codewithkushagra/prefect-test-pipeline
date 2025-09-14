from prefect import serve
from workflow import sequential_workflow
import os

if __name__ == "__main__":
    # Create the deployment
    deployment = sequential_workflow.to_deployment(
        name="sequential-workflow-deployment",
        description="A deployment of the sequential workflow with 3 tasks",
        tags=["demo", "sequential", "basic"],
        version="1.0.0"
    )
    
    # Check if running in CI/CD environment
    if os.getenv("GITHUB_ACTIONS"):
        # In CI/CD, just create the deployment without serving
        deployment.apply()
        print("Deployment created successfully!")
    else:
        # In local development, serve the deployment
        serve(deployment)
