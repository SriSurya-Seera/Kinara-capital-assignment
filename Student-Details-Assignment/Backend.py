from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/students', methods=['GET'])
def get_students():
    # Get pagination parameters
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))

    # Read student details from CSV file
    students = read_student_details_from_csv('C:/Users/Seera/OneDrive/Desktop/Student-Details-Assignment/student_data.csv')

    # Paginate the student data
    paginated_students = paginate_students(students, page, page_size)

    return jsonify(paginated_students)

def read_student_details_from_csv(file_path):
    students = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

def paginate_students(students, page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return students[start_index:end_index]

if __name__ == '__main__':
    app.run(debug=True)
