import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "876783Zahir#",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True

}

try: 
    db =mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    cursor = db.cursor()
    # inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id ")
    director = cursor.fetchall()
    print(f"-- DISPLAYING FILMS --")
    for directors in director:
        print("Film Name: {}\n Director: {}\n Genre Name ID: {}\n Studio Name: {}\n".format(directors[0],directors[1],directors[2],directors[3]))
             
def show_films (cursor,films):
   
    cursor.execute("INSERT INTO film (film_name,film_releaseDate,film_director,film_runtime,film_id,studio_id,genre_id) VALUES ('Friday','1995',' F. Gary Gray','91',4,8,5")
    films1 = cursor.fetchall()
    print("-- DISPLAYING FILMS AFTER INSERT --")
    for film1 in films:
        print("Film Name: {}\n Director: {}\n Genre Name ID: {}\n Studio Name: \n".format(film[1], film[2], film[3], film[8]))

       
    #update   
    cursor.execute("UPDATE genre SET genre_id = 3 genre_name = 'Drama' WHERE film_id = 'Alien'")
    films2 = cursor.fetchall()
    print("-- DISPLAYING FILMS AFTER UPDATE --")


    #Delete
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
    films3 = cursor.fetchall()
    print("-- DISPLAYING FILMS AFTER DELETE --")
    
    print("\n -- {} --".format(films))
   
    
    
       
db.close()


