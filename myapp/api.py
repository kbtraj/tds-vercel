from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Enable CORS manually
@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.route('/api', methods=['GET'])
def get_marks():
    try:
        # Read names from query parameters
        names = request.args.getlist('name')

        # Load student data from marks.json
        with open('marks.json', 'r') as file:
            students_data = json.load(file)

        # Collect marks
        result = {"marks": [student["marks"] for student in students_data if student["name"] in names]}

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run()
