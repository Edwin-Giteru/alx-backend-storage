#!/usr/bin/env python3
from pymongo import MongoClient

def nginx_stats():
    """Provides statistics about Nginx logs stored in MongoDB"""
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    # Count total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count requests by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count GET requests to /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    nginx_stats()

