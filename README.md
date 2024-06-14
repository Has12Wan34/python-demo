## สรุปเนื้อหา
### `setup`
- ติดตั้งโปรแกรมภาษา python `https://www.python.org/downloads/`
- กำหนด `Path` เพื่อเชื่อมโยงให้ระบบปฏิบัติการสามารถที่จะเข้าใจคำสั่งของภาษา Python ได้ และรันโปรแกรมของ Python จาก Command line ได้ทุกที่

### `fundementals`
- `Module` : ไฟล์ของภาษา Python ซึ่ง Module จะประกอบไปด้วยคลาส ฟังก์ชัน และตัวแปรต่างๆ และนอกจากนี้เรายังสามารถ import โมดูลอื่นเข้ามาในโปรแกรมได้
- `Expressions` : 
    - `Boolean expression` : เป็นการกระทำกันระหว่างตัวแปรและตัวดำเนินการเปรียบเทียบค่าหรือตัวดำเนินการตรรกศาสตร์ และจะได้ผลลัพธ์เป็น Boolean 

    ```bash
        print(a == 5) //true, false
        print(a == 4 and b == 5) //true, false
    ```
    - `Non-boolean expressions` : การกระทำกันระหว่างตัวแปรและตัวดำเนินการคณิตศาสตร์ และจะได้รับค่าใหม่เป็นตัวเลขหรือค่าที่ไม่ใช่ Boolean

    ```bash
        print(a + b)
        print(((a * a) + (b * b)) / 2)
        print("Python " + "Language")
    ```
- `specifier`
    ```bash
        a = 1
        b = 2 
        print ('a = ', a) // a = 1
        print ('c = %d' % (a/b)) // c = 0
        print ('c = %f' % (a/b)) // c = 0.5
        print ('c = %s' % hi) // c = hi
        print("%s %f %d" % (hi, 0.5, 5)) // hi 0.5 5
    ```
- `ฟังก์ชันที่ใช้กับตัวแปร`
    - `sys.getsizeof(a))` : สำหรับหาขนาดของตัวแปรที่มีหน่วยเป็น Byte 
    - `type(a)` : สำหรับดูประเภทของตัวแปรว่าอยู่ในคลาสไหน
    - `del()` : สำหรับยกเลิกหรือลบการประกาศตัวแปรออก
    - `locals()` : สำหรับตรวจสอบตัวแปรในโมดูลปัจจุบัน
    - `globals()` : สำหรับตรวจสอบตัวแปรในโปรแกรมทั้งหมด
    - `print()` : เพื่อแสดงผลข้อความ ตัวเลข หรือข้อมูลประเภทอื่นๆ
        ```bash
            print(value, ..., sep = ' ', end = '\n');
        ```
    - `input()` : สำหรับการรับค่า String จากทางคีย์บอร์ด
        ```bash
            name = input("Enter your name: ")
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Hello " + name)
            print("a + b = %d" % (a + b))
        ```
    - `คำสั่งเลือกเงื่อนไข` :
        - `if` : 
            ```bash
                if expression:
                    # statements
            ```
        - `if else` : 
            ```bash
                if expression:
                    # statements
                else:
                    # statements
            ```
        - `if else if` : 
            ```bash
                if expression:
                    # statements
                elif expression:
                    # statements
                else:
                    # statements
            ```
    - `ฟังก์ชัน` :
        ```bash
            def function_name(args...):
                # statements

            def function_name(args...):
                # statements
                return value
        ```
    - `การนำเข้าโมดูล` : 
        - `import` : นำเข้าโมดูลเพื่อนำมาใช้งานในโปรแกรม
        ```bash
            import file_name
            print(file_name.function(args...))
        ```
        - `from ... import` : สำหรับนำเข้าข้อมูลบางส่วนภายในโมดูล และสามารถใช้งานออบเจ็คได้โดยตรงโดยไม่ต้องมี Prefix ชื่อของโมดูล
        ```bash
            from file_name import file_name_1, file_name_2
            print(file_name_1.function(args...), file_name_2.function(args...))
        ```