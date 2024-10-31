import {useEffect, useState} from 'react';
import UsernameItem from './UsernameItem';
import axios from 'axios';

function Sidebar ({onUserSelect}) {

    const noUsers = 20;
    const [users, setUsers] = useState([]);

    async function getUsers (limit) {
        // Should be in .env file anyways
        let baseUrl = 'http://localhost:8000/users';
        try {
            const res = await axios.get(baseUrl, {params: {limit}});
            setUsers(res.data);
        } catch (error) {
            console.log(error, "Get users sidebar error");
        }
    }

    useEffect(() => {
        getUsers(noUsers);
    }, []);

    return (
        <div>
            <ul>
                {users.map(user => (
                    <UsernameItem key={user.id} user={user} onClick={onUserSelect}/>
                ))}
            </ul>
        </div>   
    );
}

export default Sidebar;