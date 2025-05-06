from docx import Document


def generate_scope51_report(replacement_data, output_path):
    doc = Document("templates/ts_template.docx")
    tables = doc.tables

    # for debug  
    # print(f"พบทั้งหมด {len(tables)} ตาราง\n")

    # for idx, table in enumerate(tables):
    #     print(f"\n===== ตารางที่ {idx} =====")
    #     for row_idx, row in enumerate(table.rows):
    #         row_data = [cell.text.strip() for cell in row.cells]
    #         print(f"แถวที่ {row_idx}: {' | '.join(row_data)}")

    if len(tables) == 0:
        raise ValueError("ไม่พบตารางในเอกสาร Word")

    scope51_table = tables[0]  # เปลี่ยน index ถ้าตาราง 5.1 ไม่ใช่ตารางแรก
    tttt = tables[17]

    for row in scope51_table.rows:
        for cell in row.cells:
            for code, replacement in replacement_data.items():
                if code in cell.text:
                    cell.text = cell.text.replace(code, replacement)

    data_rows = [
        ["1", "", "180", "0.1", "0.2", "0.05", "", "", "", "", "180.35"],
        ["2", "", "200", "0.2", "0.1", "0.06", "", "", "", "", "200.36"],
        ["3", "", "150", "0.05", "0.1", "0.02", "", "", "", "", "150.17"]
    ]
    
    for i, row_data in enumerate(data_rows[1]):
        row_index = 2 + i
        if row_index >= len(tttt.rows):
            break  # ป้องกัน index error ถ้าตารางมีแถวน้อยเกิน

        row = tttt.rows[row_index]
        for col_index, value in enumerate(row_data):
            if col_index < len(row.cells):
                row.cells[col_index].text = str(value)

    doc.save(output_path)
