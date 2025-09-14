# Prefect Sequential Workflow

A simple Prefect workflow with 3 sequential tasks that can be deployed to Prefect Cloud using GitHub.

## Overview

This project contains:
- **Task 1**: Data Collection - Simulates collecting 100 data points
- **Task 2**: Data Processing - Processes the collected data (80% efficiency)
- **Task 3**: Report Generation - Creates a final summary report

All tasks run sequentially, with each task depending on the output of the previous one.

## Project Structure

```
prefect-test-pipeline/
├── workflow.py          # Main workflow with 3 sequential tasks
├── deploy.py            # Deployment script
├── requirements.txt     # Python dependencies
├── prefect.yaml        # Prefect configuration
├── .github/
│   └── workflows/
│       └── deploy.yml  # GitHub Actions for deployment
└── README.md           # This file
```

## Local Development

### Prerequisites

- Python 3.11+
- Prefect Cloud account

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd prefect-test-pipeline
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Prefect Cloud**
   ```bash
   prefect cloud login
   ```

4. **Run the workflow locally**
   ```bash
   python workflow.py
   ```

## Deployment to Prefect Cloud

### Method 1: Using GitHub Actions (Recommended)

1. **Set up GitHub Secrets**
   Go to your GitHub repository → Settings → Secrets and variables → Actions
   Add these secrets:
   - `PREFECT_API_URL`: Your Prefect Cloud API URL
   - `PREFECT_API_KEY`: Your Prefect Cloud API key

2. **Push to main branch**
   ```bash
   git add .
   git commit -m "Initial Prefect workflow"
   git push origin main
   ```

   The GitHub Action will automatically deploy your workflow to Prefect Cloud.

### Method 2: Manual Deployment

1. **Deploy using the deployment script**
   ```bash
   python deploy.py
   ```

2. **Or use Prefect CLI**
   ```bash
   prefect deployment build workflow.py:sequential_workflow -n sequential-workflow
   prefect deployment apply sequential-workflow-deployment.yaml
   ```

## Running the Workflow

Once deployed, you can run the workflow in several ways:

### From Prefect Cloud UI
1. Go to your Prefect Cloud dashboard
2. Navigate to Deployments
3. Find "sequential-workflow-deployment"
4. Click "Run" to execute the workflow

### From CLI
```bash
prefect deployment run "sequential-workflow/sequential-workflow-deployment"
```

### From Python
```python
from prefect import run_deployment

# Run the deployment
result = run_deployment("sequential-workflow/sequential-workflow-deployment")
```

## Workflow Details

### Task 1: Data Collection
- Simulates collecting 100 data points
- Takes 2 seconds to complete
- Returns a dictionary with data points and status

### Task 2: Data Processing
- Processes the data from Task 1
- Simulates 80% processing efficiency
- Takes 3 seconds to complete
- Returns processed data with timestamps

### Task 3: Report Generation
- Creates a final summary report
- Calculates processing efficiency
- Takes 2 seconds to complete
- Returns a comprehensive report

## Monitoring

- View workflow runs in the Prefect Cloud UI
- Monitor task execution and logs
- Set up notifications for failures
- Track performance metrics

## Customization

To modify the workflow:

1. Edit `workflow.py` to change task logic
2. Update `requirements.txt` if you add new dependencies
3. Modify `prefect.yaml` for deployment configuration
4. Push changes to trigger automatic deployment

## Troubleshooting

### Common Issues

1. **Authentication Error**
   - Ensure your Prefect Cloud API key is correct
   - Check that `PREFECT_API_URL` is set correctly

2. **Deployment Fails**
   - Verify all dependencies are in `requirements.txt`
   - Check GitHub Actions logs for specific errors

3. **Workflow Not Running**
   - Ensure you have an active work pool in Prefect Cloud
   - Check that the deployment is properly configured

### Getting Help

- [Prefect Documentation](https://docs.prefect.io/)
- [Prefect Cloud Guide](https://docs.prefect.io/cloud/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
