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
#----------------------------------------<br/>
#GET COURSE<br/>
#----------------------------------------<br/>
type: get<br/>
url : http://0.0.0.0:5000/getcourse?course_id=DS512<br/>
<br/>
Response: <br/>
{<br/>
    "course_id":"DS512",<br/>
    "name":"Information Systems",<br/>
    "ects": 10<br/>
}<br/>
<br/>
<br/>
#----------------------------------------<br/>
#ΑDD COURSE<br/>
#----------------------------------------<br/>
type: put<br/>
url : http://0.0.0.0:5000/add-course/alexpap2@gmail.com<br/>
body:<br/>
{    <br/>
    "course_id":"DS515"<br/>
}<br/>
<br/>
Response:"Student data updated:"<br/>
<br/><br/>
<br/>
#----------------------------------------<br/>
#DELETE STUDENT<br/>
#----------------------------------------<br/>
type: delete<br/>
url : http://0.0.0.0:5000/delete-student?email=alexpap1@gmail.com<br/>
<br/>
Response: "The student has been removed."<br/>
<br/>
<br/>
#----------------------------------------<br/>
#INSERT COURSE DESCRIPTION<br/>
#----------------------------------------<br/>
type: post<br/>
url : http://0.0.0.0:5000/insert-course-description?course_id=DS512<br/>
body:<br/>
{<br/>
    "description": "This is the description"<br/>
}<br/>
<br/>
Response: "The course has now description"<br/>
<br/>
<br/>
#----------------------------------------<br/>
#UPDATE COURSE<br/>
#----------------------------------------<br/>
type: put<br/>
url : http://0.0.0.0:5000/update-course?course_id=DS512<br/>
body:<br/>
{<br/>
    "name":"InfoSys",<br/>
    "ects": 70,<br/>
    "description": "bblalalal"<br/>
}<br/>
<br/>
Response: "Course info updated"<br/>
