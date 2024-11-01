function UsernameItem({user, onClick}) {
    return(
        <li onClick={()=>onClick(user)} className="text-white">
            {user.firstName} {user.lastName}
        </li>
    )
}

export default UsernameItem;