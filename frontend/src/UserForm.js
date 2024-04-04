import { useState } from "react";

const UserForm = ({}) => {
  const [fornavn, setFornavn] = useState("");
  const [efternavn, setEfternavn] = useState("");
  const [alder, setAlder] = useState("");
  const [email, setEmail] = useState("");
  const [adgangskode, setAdgangskode] = useState("");

    const onSubmit = async (e) => {
        //don't refresh page
        e.preventDefault();

        const data = {
            fornavn,
            efternavn,
            alder,
            email,
            adgangskode
        };
        const url = "http://127.0.0.1:5000/api/user";
        const options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        };
        const repsonse = await fetch(url, options);

        if (repsonse.status !== 201 && repsonse.status !== 200) {
            const data = await repsonse.json();
            alert(data.message)
        } else {
            //success
            alert("user has been created!")
        };
    };

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="fornavn">Fornavn:</label>
        <input
          type="text"
          id="fornavn"
          value={fornavn}
          onChange={(e) => setFornavn(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="efternavn">Efternavn:</label>
        <input
          type="text"
          id="efternavn"
          value={efternavn}
          onChange={(e) => setEfternavn(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="alder">Alder:</label>
        <input
          type="number"
          id="alder"
          value={alder}
          onChange={(e) => setAlder(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="text"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="adgangskode">Adgangskode:</label>
        <input
          type="password"
          id="adgangskode"
          value={adgangskode}
          onChange={(e) => setAdgangskode(e.target.value)}
        />
      </div>
      <button type="submit">Opret Bruger</button>
    </form>
  );
};

export default UserForm;