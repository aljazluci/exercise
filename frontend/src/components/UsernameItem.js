function UsernameItem({user, onClick}) {
    return(
        <li onClick={()=>onClick(user)}>
            {user.firstName} {user.lastName}
        </li>
    )
}

export default UsernameItem;