import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';

function App() {
    const [items, setItems] = useState([]);
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/api/items')
            .then(response => response.json())
            .then(data => setItems(data));

        fetch('http://localhost:8000/api/users')
            .then(response => response.json())
            .then(data => setUsers(data));
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <h1>Items</h1>
                <ul>
                    {items.map(item => (
                        <li key={item.id}>{item.name}</li>
                    ))}
                </ul>

                <h1>Users</h1>
                <ul>
                    {users.map(user => (
                        <li key={user.id}>{user.username}</li>
                    ))}
                </ul>
            </header>
        </div>
    );
}

export default App;