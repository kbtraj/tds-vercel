import json

def handler(event, context):
    # Enable CORS
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    try:
        # Extract query parameters
        query_params = event.get("queryStringParameters", {})
        names = query_params.get("name", [])

        # Ensure names is a list (if only one name is provided, it's a string)
        if isinstance(names, str):
            names = [names]

        # Load student marks from marks.json
        with open('marks.json', 'r') as file:
            students_data = json.load(file)

        # Find marks for the requested names
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
