import json
import urllib.parse

def handler(event, context):
    # Enable CORS
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    try:
        # Parse query parameters
        query_params = event.get("queryStringParameters", {})
        names = query_params.get("name")

        if names:
            if isinstance(names, str):  # If only one name is passed
                names = [names]
        else:
            names = []

        # Load student data from marks.json
        with open('marks.json', 'r') as file:
            students_data = json.load(file)

        # Collect marks
        result = {"marks": []}
        for student in students_data:
            if student["name"] in names:
                result["marks"].append(student["marks"])

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(result)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({"error": "Internal Server Error", "details": str(e)})
        }
