from flask import Flask, render_template, request
import boto3 

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb')  # Replace with your desired region
table_name = 'raj-table'  # Replace with your DynamoDB table name
table = dynamodb.Table(table_name)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    print(name+" " +str(age));
   
    table.put_item(Item={'name': name, 'age': age})
    

    return 'Data stored successfully in DynamoDB'

@app.route('/usercount', methods=['GET', 'POST'])
def usercount():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'Anil@0153':  # Replace 'your_password' with your actual password
            response = table.scan()
            count = response['Count']
            return f'Total users: {count}'
        else:
            return 'Invalid password'
    return render_template('usercount.html')
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0",port=8080,debug=False)
    print(table_name)


