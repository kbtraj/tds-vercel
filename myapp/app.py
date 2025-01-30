import json

def handler(request):
    # Enable CORS for all origins
    headers = {
        'Access-Control-Allow-Origin': '*',  # Allows requests from any origin
        'Content-Type': 'application/json',  # Ensures the response is in JSON format
        'Access-Control-Allow-Methods': 'GET',  # Specifies the allowed method
        'Access-Control-Allow-Headers': 'Content-Type'  # Specifies allowed headers
    }

    # Get names from query parameters
    names = request.args.getlist('name')

    # Load student data from marks.json
    with open('marks.json', 'r') as file:
        students_data = json.load(file)

    result = {"marks": []}
    for student in students_data:
        if student["name"] in names:
            result["marks"].append(student["marks"])

    # Return the result as a JSON response with the CORS headers
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(result)
    }
