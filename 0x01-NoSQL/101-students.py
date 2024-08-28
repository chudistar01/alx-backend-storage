#!/usr/bin/env python3
"""Returns sorted average scores"""


def top_students(mongo_collection):
    """ Returns sorted average scores """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"sort": {"averageScore": -1}}
    ])

    return top_student
