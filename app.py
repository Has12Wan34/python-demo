from flask import Flask, request, jsonify
from pydantic import BaseModel
import database

app = Flask(__name__)

class LoginModel(BaseModel):
    id: str
    email: str
    fname: str

@app.route('/api/auth/login', methods=['POST'])
def Login():
    # รับข้อมูลจาก JSON
    data = request.get_json()
    # สร้าง Object ของ Model
    new_book = LoginModel(**data) 
    print(new_book)

    # ส่งผลลัพธ์
    return jsonify({'message': 'หนังสือถูกเพิ่มเรียบร้อยแล้ว'})

@app.route('/api/auth/register' , methods=['POST'])
def insert():
    data = request.get_json()
    database.insert_data(data)
    return jsonify({'message' : "success"})

@app.route('/api/user/users' , methods=['GET'])
def fetch():
    jsonData = database.get_data()
    # new_book = LoginModel(**data) 
    return jsonify(jsonData)

@app.route('/api/user/users/<id>' , methods=['DELETE'])
def remove(id):
    database.delete_data(id)
    return "Hello"

if __name__ == "__main__":
    # debug=True
    app.run(debug=True) 