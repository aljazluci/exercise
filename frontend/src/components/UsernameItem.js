

function UsernameItem({user, onClick}) {
    return(
        <li onClick={()=>onClick(user)}>
            {user.username}
        </li>
    )
}

export default UsernameItem;