function UsernameItem({user, onClick}) {
    return(
        <li onClick={()=>onClick(user)}>
            {user.name}
        </li>
    )
}

export default UsernameItem;