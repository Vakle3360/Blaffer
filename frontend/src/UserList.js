import React from "react";

const UserList = ({users}) => {
    const getUser = (id_) => {
        if (id_){
            for (let i = 0; i < users.length; i++){
                let user = users[i][0]
                try{
                    if (user.id == id_){
                        console.log(user)
                        return (user);
                    }
                }
                catch (e){}
            }
        }
    }

    const displayUser = (user) => {
        if (user){
            try {
                document.getElementById("fornavn").textContent = user.fornavn;
                document.getElementById("efternavn").textContent = user.efternavn;
                document.getElementById("email").textContent = user.email;
                document.getElementById("adgangskode").textContent = user.password;
            } catch (e) {
                console.log(e)
            }
        }
    }
    
    return <div>
        <h2>Brugere</h2>
        <input type="number" placeholder="id" id="searchByID"></input>
        <button onClick={() => {displayUser(getUser(document.getElementById("searchByID").value))}}>Search</button>
        <p>Fornavn: <p id="fornavn"></p></p>
        <p>Efternavn: <p id="efternavn"></p></p>
        <p>Email: <p id="email"></p></p>
        <p>Adgangskode: <p id="adgangskode"></p></p>
    </div>
}

export default UserList