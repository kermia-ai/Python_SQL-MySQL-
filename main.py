import mysql.connector

# Connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)

# Création d'un curseur pour exécuter les requêtes SQL
cursor = db.cursor()

# INSERT : Créer un nouvel utilisateur dans la table "users"
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
val = ("John Doe", "johndoe@email.com")
cursor.execute(sql, val)
db.commit()
print(cursor.rowcount, "record inserted.")

# SELECT : Récupérer tous les utilisateurs de la table "users"
sql = "SELECT * FROM users"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)

# UPDATE : Mettre à jour l'email de l'utilisateur dont le nom est "John Doe"
sql = "UPDATE users SET email = %s WHERE name = %s"
val = ("newemail@email.com", "John Doe")
cursor.execute(sql, val)
db.commit()
print(cursor.rowcount, "record(s) affected")

# DELETE : Supprimer l'utilisateur dont l'email est "johndoe@email.com"
sql = "DELETE FROM users WHERE email = %s"
val = ("johndoe@email.com",)
cursor.execute(sql, val)
db.commit()
print(cursor.rowcount, "record(s) deleted")

# Fermeture du curseur et de la connexion à la base de données MySQL
cursor.close()
db.close()
