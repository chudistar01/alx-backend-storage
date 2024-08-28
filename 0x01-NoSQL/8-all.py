#!/usr/bin/env python3
""" Task number eight """


def list_all(mongo_collection):
    """ Lists all documents in python """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
