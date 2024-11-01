import { useState } from "react";
import UpdateUserForm from "./UpdateUserForm";

function MainContent ({user}) {
    const [response, setResponse] = useState("");

    return(<>
            user ? <UpdateUserForm user={user} onUserChange={setResponse}/> : <></>
            Response: {JSON.stringify(response)}
        </>
    )
}

export default MainContent;