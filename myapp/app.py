# api/index.py
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load student data from marks.json
def load_student_data():
    with open('marks.json', 'r') as file:
        return json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get the names from query parameters
    names = request.args.getlist('name')
    
    # Load the student data
    students_data = load_student_data()
    
    result = {"marks": []}
    for student in students_data:
        if student["name"] in names:
            result["marks"].append(student["marks"])

    # Return the result as a JSON response
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
