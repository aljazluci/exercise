import {useEffect, useState} from 'react';

function Sidebar () {

    const noUsers = 20;
    const [users, setUsers] = useState([]);

    async function getUsers (limit) {
        let baseUrl = 'https://dummyjson.com/users';
        let options = limit ? `limit=${limit}` : '';
        try {
            const res = await fetch(`${baseUrl}?${options}`);
            const data = await res.json();
            setUsers(data.users);
        } catch (error) {
            console.log("Get users sidebar error");
        }
    }

    useEffect(() => {
        getUsers(noUsers);
    }, []);

    return (
        <div>
            <ul>
                {users.map(user => (
                    <li key={user.id}>{user.firstName} {user.lastName}</li>
                ))}
            </ul>
        </div>   
    );
}

export default Sidebar;