package main

import (
    "database/sql"
    "fmt"
    "strconv"

    _ "github.com/mattn/go-sqlite3"
)

func main() {
    database, _ := sql.Open("sqlite3", "./Snehadb.db")
    statement, _ := database.Prepare("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)")
    statement.Exec()
    statement, _ = database.Prepare("INSERT INTO users (name, phone, email, password) VALUES (?, ?, ?, ?)")
	
	var id int
    var name string
    var phone string
	var email string
	var password string
	fmt.Println("Enter name:")
	fmt.Scan(&name)
	fmt.Println("Enter phone number:")
	fmt.Scan(&phone)
	fmt.Println("Enter email id:")
	fmt.Scan(&email)
	fmt.Println("Enter password:")
	fmt.Scan(&password)
    statement.Exec(name, phone, email, password)
    rows, _ := database.Query("SELECT id, name, phone, email, password FROM users")	
    
    for rows.Next() {
        rows.Scan(&id, &name, &phone, &email, &password)
        fmt.Println(strconv.Itoa(id) + ": " + name + " " + phone + " " + email + " " + password)
    }
}
