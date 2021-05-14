from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect, Response
import json

# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choose InfoSys database and Courses collection
db = client['InfoSys']
courses = db['Courses']
students = db['Students']

# Initiate Flask App
app = Flask(__name__)

# Insert Course
# Create Operation
@app.route('/insertcourse', methods=['POST'])
def insert_student():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "course_id" in data or not "name" in data or not "ects" in data:
        return Response("You have to give course_id AND name AND ects",status=500,mimetype="application/json")
    
    if courses.find({"course_id":data["course_id"]}).count() == 0 :
        course = {"course_id": data['course_id'], "name": data['name'], "ects":data['ects']}
        # Add student to the 'students' collection
        courses.insert_one(course)
        return Response("The course was added to the MongoDB",status=200,mimetype='application/json') 
    else:
        return Response("The course with the given ID already exists",status=200,mimetype='application/json')


# Get Course (with argument)
@app.route('/getcourse', methods=['GET'])
def get_course():
    course_id = request.args.get('course_id')
    if course_id == None:
        return Response("Bad request (no arguments)", status=500, mimetype='application/json')
    else:
        course = courses.find_one( {'course_id':course_id })
        if course !=None:
            #course  = {'_id':str(course["_id"]),'course_id':course["course_id"],'name':course["name"], 'ects':course["ects"], 'description':course["description"]}
            course  = {'_id':str(course["_id"]),'course_id':course["course_id"],'name':course["name"], 'ects':course["ects"]}
            return jsonify(course)
    return Response('No course found',status=500,mimetype='application/json')


# ADD COURSE
@app.route('/add-course/<string:email>', methods=['PUT'])
def add_course(email):
    if request.data:
        data = json.loads(request.data)
        student = students.find_one({"email":email})
        if student != None:
            students.update( {'email': email},
                    {'$set': { 'courses': data['course_id'] } })
            return Response('Student data updated', status=200)
            #return jsonify(student)
        return Response('No student found',status=500,mimetype='application/json')
    else: 
         return Response("Bad request", status=500, mimetype='application/json')


# DELETE STUDENT (with argument)
@app.route('/delete-student', methods=['DELETE'])
def delete_student():
    email = request.args.get('email')
    if email == None:
        return Response("Bad request (no arguments)", status=500, mimetype='application/json')
    else:
        student = students.find({'email':email}).count()
        if student==1:
            students.delete_one({'email':email})
            return Response('The student has been removed.', status=200)
    return Response('No student found',status=500,mimetype='application/json')


#INSERT COURSE DESCRIPTION
@app.route('/insert-course-description', methods=['POST'])
def insert_course_description():
    #request argument
    course_id = request.args.get('course_id')
    if course_id == None:
        return Response("Bad request (no arguments)", status=500, mimetype='application/json')
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "description" in data:
        return Response("Information incompleted",status=500,mimetype="application/json")
    
    if courses.find({"course_id":course_id}).count() == 1 :
        courses.update( {'course_id': course_id},
                    {'$set': {'description': data['description']} })
        return Response("The course has now description",status=200,mimetype='application/json') 
    else:
        return Response("Course id dosent exists in DB",status=200,mimetype='application/json')


# Find student by email
@app.route('/getstudent/<string:email>', methods=['GET'])
def get_student_by_email(email):
    if email == None:
        return Response("Bad request", status=500, mimetype='application/json')
    student = students.find_one({"email":email})
    if student !=None:
        student = {'_id':str(student["_id"]),'name':student["name"],'email':student["email"], 
        'yearOfBirth':student["yearOfBirth"], 'courses':student["courses"]}
        return jsonify(student)
    return Response('no student found',status=500,mimetype='application/json')


# UPDATE COURSE
@app.route('/update-course', methods=['PUT'])
def update_course():
    #request argument
    course_id = request.args.get('course_id')
    if course_id == None:
        return Response("Bad request (no arguments)", status=500, mimetype='application/json')
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "name" in data or not "ects" in data or not "description" in data:
        return Response("Information incompleted",status=500,mimetype="application/json")

    if courses.find({"course_id":course_id}).count() == 1 :
        courses.update_one({'course_id': course_id},
                {'$set': {'name': data['name'], 'ects':data['ects'], 'description':data['description']}})
        return Response("Course info updated",status=200,mimetype='application/json') 
    else:
        return Response("Course id dosent exists in DB",status=200,mimetype='application/json')


# Run Flask App
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
