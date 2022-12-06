import psycopg2

def dbconnect():
    return psycopg2.connect(
    host="localhost",
    port="5432",
    database="assessmentdb",
    user="postgres",
    password="tmad1652")

def main():
    print("Hello assesment!")

if __name__ == "__main__":
    main()