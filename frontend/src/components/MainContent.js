import UserDetails from "./UserDetails";

function MainContent ({user}) {
    return (
        user ? <UserDetails user={user}/> : <></>
    );
}

export default MainContent;