function UsernameItem({user, onClick}) {
    return(
        <li className="text-white  ">
            <p 
                onClick={()=>onClick(user)} 
                className="inline-block m-0 p-1 hover:text-color-orange-on-dark cursor-pointer">
                    {user.firstName} {user.lastName}
            </p>
        </li>
    )
}

export default UsernameItem;