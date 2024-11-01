import { useEffect, useState } from "react";
import UpdateUserForm from "./UpdateUserForm";

function MainContent ({user}) {
    const [response, setResponse] = useState("");

    useEffect(() => {
        setResponse("");    
    }, [user]);

    return(user ? <div className="flex flex-row pt-8 px-16">
            <UpdateUserForm user={user} onUserChange={setResponse}/>
            <div className="px-8 text-xs"><pre>{JSON.stringify(response, null, 4)}</pre></div>
        </div> 
        : <div>Select user to modify</div>
    )
}

export default MainContent;