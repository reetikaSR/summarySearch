# summarySearch

Install packages:
Use requirements.txt

Testing Instructions:
python3 manage.py test --settings SumarySearch.settings

API testing:
Url:
http://127.0.0.1:8000/search/

Headers:
Content-Type: multipart/form-data; boundary=\<calculated when request is sent\>
  
Body:
queries:is your problems
queries:achieve take book
k:3

