from flask import Flask, jsonify,request


app=Flask(__name__)
tasks=[
    {
        'id':1,
        'contact':'6386934587',
        'name':'Ellena',
        'done':False
    },
    {
       'id':2,
        'contact':'9628772122',
        'name':'Rose',
        'done':False 
    }
]
@app.route('/')#create a route,it will open app

def Hello_world():
    return 'Hello World'

@app.route('/add-data',methods=['POST'])#allowing the user to add data
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide the data'
        },400)#400port usually for error

    task={
        'id':tasks[-1]['id']+1,#new task id previous id+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',' '),
        'done':False
    }

    tasks.append(task)
    return jsonify({
            'status':'successful',
            'message':'Task added successfully'
        })

@app.route('/get-data')

def get_task():
    return jsonify({
        'data':tasks
    })




if (__name__ =='__main__'):#it will assign name to your constructor __name__
    app.run(debug=True)#if code not wokring fine,error gets displayed

