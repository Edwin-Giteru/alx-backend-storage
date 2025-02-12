#!/usr/bin/env python3

'a script that returns all students sorted by average score'

def top_students(mongo_collection):
     return list(mongo_collection.aggregate([
        {"$addFields": {"averageScore": {"$avg": "$scores"}}},
        {"$sort": {"averageScore": -1}}
    ]))

