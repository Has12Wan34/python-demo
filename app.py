from flask import Flask, request, jsonify, send_file
from pydantic import BaseModel
import uuid
import os
from export_logic import generate_scope51_report

app = Flask(__name__)

# Pydantic model สำหรับข้อมูลที่รับ
class LoginModel(BaseModel):
    id: str
    email: str
    fname: str

@app.route('/export/ghg-scope51', methods=['POST'])
def export_ghg_scope51():
    data = request.get_json()
    replacement_data = data.get("replacement_data", {})
    # ตรวจสอบว่า request มี "summary_rows" และข้อมูลในนั้นมีจำนวนคอลัมน์ที่ถูกต้อง
    expected_columns = 2
    for row_data in data["summary_rows"]:
        if len(row_data) != expected_columns:
            return jsonify({
                "status": "error",
                "message": f"Expected {expected_columns} columns, but got {len(row_data)} columns in data."
            }), 415

    # สร้างไฟล์ .docx
    file_id = str(uuid.uuid4())
    output_path = f"reports/ghg_scope51_{file_id}.docx"
    os.makedirs("reports", exist_ok=True)

    # สร้างไฟล์ .docx ด้วยข้อมูล
    generate_scope51_report(replacement_data, output_path)

    # ส่งไฟล์กลับให้ผู้ใช้ดาวน์โหลด
    return jsonify({
        "status": "success",
        "message": "Report generated successfully",
        "file_url": f"http://localhost:5001/download/{file_id}.docx"
    }), 200

@app.route('/download/<file_id>', methods=['GET'])
def download_file(file_id):
    file_path = f"reports/ghg_scope51_{file_id}.docx"
    if os.path.exists(file_path):
        return send_file(file_path, 
                         as_attachment=True, 
                         download_name=f"GHG_Scope1_Summary_{file_id}.docx", 
                         mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    else:
        return jsonify({
            "status": "error",
            "message": "File not found"
        }), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
