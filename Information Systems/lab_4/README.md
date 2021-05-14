4th lab for "Information Systems"
--------------------------------
Χρησιμοποιήστε ένα MongoDB container το οποίο θα χρησιμοποιεί την port 27017 του host και να εισάγετε τα δεδομένα του αρχείου
students.json που θα βρείτε στο link.
Να προσθέσετε στο web service που θα βρείτε εδώ τα παρακάτω endpoint:
1. Να βρίσκει τα άτομα που έχουν κάποια καταγεγραμμένη κατοικία.
endpoint: /getStudentsWithAddress
2. Να βρίσκει τη διεύθυνση της κατοικίας τους βάσει email
endpoint: /getStudentsAddress/<student_email>
3. Να βρίσκει όλα τα άτομα που έχουν κατοικία και έχουν γεννηθεί τη δεκαετία του 1980.
endpoint: /getEightiesAddress
4. Να επιστρέφεται ο αριθμός των ατόμων που έχουν δηλωμένη κάποια κατοικία.
endpoint: /countAddress
5. Να υλοποιηθεί ξανά η συνάρτηση insert_student()ώστε να μπορεί να γίνει εισαγωγή στη βάση δεδομένων κάποιος νέος
φοιτητής μαζί με δεδομένα για τη κατοικία του.
6. Να επιστρέφεται ο αριθμός των ατόμων που έχουν γεννηθεί μία συγκεκριμένη χρονιά:
endpoint: /countYearOfBirth/<yearOfBirth>
--------------------------------


We create our container:
--------------------------------
$ docker run -d -p 27017:27017 --name mongo_con mongo
$ docker cp students.json mongo_con:/students.json
$ docker exec -it mongo_con mongoimport --db=InfoSys --collection=Students --file=students.json


Then we run our flask app:
--------------------------------
$ python proeretiki_4_e16099.py


With postman we can do our POST/GET requests:
--------------------------------
ex.<br/>
type: post <br/>
url : http://0.0.0.0:5000//insertstudentv2<br/>
body: <br/>
{<br/>
"name":"Alexandros",<br/>
"yearOfBirth":1998,<br/>
"email":"alexpap2@gmail.com",<br/>
"city": "Lowgap",<br/>
"postcode": 18330,<br/>
"street": "Jardine Place"  <br/>
}
