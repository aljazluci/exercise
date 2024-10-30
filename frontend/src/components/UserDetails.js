function UserDetails({user}) {
    return (
        <div>
            <p>{user.id}</p>
            <p>{user.firstName} {user.lastName}</p>
            <p>{user.age} {user.gender}</p>
            <p>{user.email} {user.phone}</p>
        </div>
    )
}

export default UserDetails;