
import psycopg2

conn = psycopg2.connect(host="localhost",
                        database="CourseWork5",
                        user="postgres",
                        password="645595")

cur = conn.cursor()