#----------------------------------------<br/>
#INSERT COURSE<br/>
#----------------------------------------<br/>
type: post<br/>
url : http://0.0.0.0:5000/insertcourse<br/>
body: <br/>
{<br/>
    "course_id":"DS512",<br/>
    "name":"Information Systems",<br/>
    "ects": 10<br/>
}<br/>
<br/>
Response: "The course was added to the MongoDB"<br/>
or "The course with the given ID already exists"<br/>
<br/>
<br/>
#----------------------------------------
#GET COURSE
#----------------------------------------
type: get
url : http://0.0.0.0:5000/getcourse?course_id=DS512

Response: 
{
    "course_id":"DS512",
    "name":"Information Systems",
    "ects": 10
}


#----------------------------------------
#ΑDD COURSE
#----------------------------------------
type: put
url : http://0.0.0.0:5000/add-course/alexpap2@gmail.com
body:
{    
    "course_id":"DS515"
}

Response:
[
    "Student data updated:",
    {
        "_id": "609e57ecfdb984253fd851e1",
        "courses": [
            "DS515"
        ],
        "email": "alexpap2@gmail.com",
        "name": "Alexandros",
        "yearOfBirth": 1998
    }
]


#----------------------------------------
#DELETE STUDENT
#----------------------------------------
type: delete
url : http://0.0.0.0:5000/delete-student?email=alexpap1@gmail.com

Response: "The student has been removed."


#----------------------------------------
#INSERT COURSE DESCRIPTION
#----------------------------------------
type: post
url : http://0.0.0.0:5000/insert-course-description?course_id=DS512
body:
{
    "description": "This is the description"
}

Response: "The course has now description"


#----------------------------------------
#UPDATE COURSE
#----------------------------------------
type: put
url : http://0.0.0.0:5000/update-course?course_id=DS512
body:
{
    "name":"InfoSys",
    "ects": 70,
    "description": "bblalalal"
}

Response: "Course info updated"





