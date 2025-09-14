from prefect import serve
from workflow import sequential_workflow

if __name__ == "__main__":
    # Create and serve the deployment
    deployment = sequential_workflow.to_deployment(
        name="sequential-workflow-deployment",
        description="A deployment of the sequential workflow with 3 tasks",
        tags=["demo", "sequential", "basic"],
        version="1.0.0"
    )
    
    # Serve the deployment
    serve(deployment)
