import { useState, useEffect } from "react";

function UpdateUserForm({user, updateUser}) {
    console.log(user?.email)
    const [firstName, setFirstName] = useState(user?.firstName || "");
    const [lastName, setLastName] = useState(user?.lastName || "");
    const [age, setAge] = useState(user?.age || "");
    const [gender, setGender] = useState(user?.gender || "");
    const [email, setEmail] = useState(user?.email || "");
    const [phone, setPhone] = useState(user?.phone || "");

    useEffect(() => {
        setFirstName(user?.firstName || "");
        setLastName(user?.lastName || "");
        setAge(user?.age || "");
        setGender(user?.gender || "");
        setEmail(user?.email || "");
        setPhone(user?.phone || "");
    }, [user]);

    return (
        <form className="flex flex-col">
            <p>id {user?.id || ""}</p>
            <label> firstName
                <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)}/>
            </label>
            <label> lastName
                <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)}/>
            </label>
            <label> age
                <input type="text" value={age} onChange={(e) => setAge(e.target.value)}/>
            </label>
            <label> gender
                <input type="text" value={gender} onChange={(e) => setGender(e.target.value)}/>
            </label>
            <label> email
                <input type="text" value={email} onChange={(e) => setEmail(e.target.value)}/>
            </label>
            <label> phone
                <input type="text" value={phone} onChange={(e) => setPhone(e.target.value)}/>
            </label>
        </form>
    );
}

export default UpdateUserForm;