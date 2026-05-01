from  database import get_connection
import logging

def add_student(name,age,course):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = 'INSERT INTO students (name,age,course) VALUES (%s,%s,%s)'
        cursor.execute(query,(name,age,course))
        conn.commit()
        logging.info(f'Added student : {name}')
    except Exception as e:
        logging.error(f'Add Error : {e}')
    finally:
        cursor.close()
        conn.close()

def fetch_student():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def update_student(student_id,name,age,course):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"
        cursor.execute(query,(name,age,course,student_id))
        conn.commit()

        logging.info(f"Updated Student ID: {student_id}")

    except Exception as e:
        logging.error(f"Update Error: {e}")
    finally:
        cursor.close()
        conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = "DELETE FROM students WHERE id=%s"
        cursor.execute(query,(student_id,))
        conn.commit()

        logging.info(f"Deleted Student ID: {student_id}")
    except Exception as e:
        logging.error(f"Delete Error : {e}")
    finally:
        cursor.close()
        conn.close()