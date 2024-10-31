function UserDetails({user}) {
    /*
    <div>
            <p>{user.id}</p>
            <p>{user.firstName} {user.lastName}</p>
            <p>{user.age} {user.gender}</p>
            <p>{user.email} {user.phone}</p>
        </div>
    */ 

    return (
        <div>
            <p>{user.id}</p>
            <p>{user.name}</p>
            <p>{user.email}</p>
        </div>
    )
}

export default UserDetails;