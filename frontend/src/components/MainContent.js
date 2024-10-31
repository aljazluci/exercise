import UpdateUserForm from "./UpdateUserForm";
import UserDetails from "./UserDetails";

function MainContent ({user}) {
    /*return (
        user ? <UserDetails user={user}/> : <></>
    );*/
    return(
        <UpdateUserForm user={user}/>
    )
}

export default MainContent;