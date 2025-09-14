from prefect import flow, task
import time
from datetime import datetime


@task
def task_one():
    """First task that processes some data"""
    print("Starting Task 1: Data Collection")
    time.sleep(2)  # Simulate some work
    result = {"data_points": 100, "status": "collected"}
    print(f"Task 1 completed: {result}")
    return result


@task
def task_two(data_from_task_one):
    """Second task that processes the data from task one"""
    print("Starting Task 2: Data Processing")
    time.sleep(3)  # Simulate processing work
    processed_data = {
        "original_points": data_from_task_one["data_points"],
        "processed_points": data_from_task_one["data_points"] * 0.8,
        "processing_time": datetime.now().isoformat()
    }
    print(f"Task 2 completed: {processed_data}")
    return processed_data


@task
def task_three(processed_data):
    """Third task that generates final report"""
    print("Starting Task 3: Report Generation")
    time.sleep(2)  # Simulate report generation
    final_report = {
        "summary": f"Processed {processed_data['processed_points']} data points",
        "efficiency": f"{(processed_data['processed_points'] / processed_data['original_points']) * 100:.1f}%",
        "generated_at": datetime.now().isoformat()
    }
    print(f"Task 3 completed: {final_report}")
    return final_report


@flow(name="sequential-workflow", log_prints=True)
def sequential_workflow():
    """Main workflow that runs three tasks sequentially"""
    print("Starting Sequential Workflow")
    
    # Task 1: Data Collection
    data = task_one()
    
    # Task 2: Data Processing (depends on task 1)
    processed = task_two(data)
    
    # Task 3: Report Generation (depends on task 2)
    report = task_three(processed)
    
    print("Sequential Workflow completed successfully!")
    return report


if __name__ == "__main__":
    result = sequential_workflow()
    print(f"Final result: {result}")
