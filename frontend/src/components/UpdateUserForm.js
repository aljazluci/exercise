import { useState, useEffect } from "react";
import axios from "axios";

function UpdateUserForm({user, onUserChange}) {
    // states
    const [firstName, setFirstName] = useState(user?.firstName || "");
    const [lastName, setLastName] = useState(user?.lastName || "");
    const [age, setAge] = useState(user?.age || "");
    const [gender, setGender] = useState(user?.gender || "");
    const [email, setEmail] = useState(user?.email || "");
    const [phone, setPhone] = useState(user?.phone || "");

    // on user change 
    useEffect(() => {
        setFirstName(user?.firstName || "");
        setLastName(user?.lastName || "");
        setAge(user?.age || "");
        setGender(user?.gender || "");
        setEmail(user?.email || "");
        setPhone(user?.phone || "");
    }, [user]);

    async function handleSubmit(event) {
        event.preventDefault();
        const formUser = {
            id: user?.id,
            firstName,
            lastName,
            age,
            gender,
            email,
            phone
        };
        onUserSubmit(formUser);
    }

    async function onUserSubmit(formUser) {
        // should be in env file
        let baseUrl = 'http://127.0.0.1:8000/users/' + formUser.id;
        try {
            const res = await axios.put(baseUrl, {
                firstName, lastName, age, gender, email, phone
            });  
            onUserChange(res);
        } catch (error) {
            console.log(error, "Update users form error");
        }
    }

    const inputTextClassName="block border-2 mt-2 p-2 py-1 rounded-xl";
    const labelClassName="mb-2";
    // Form for updating user
    return (
        <form className="flex flex-col border-2 h-4/5 border-color-orange-border px-12 py-8 min-w-96 rounded-xl text-sm" onSubmit={handleSubmit}>
            <p className="mb-4">User ID: {user?.id || ""}</p>
            <label className={labelClassName}> First name:
                <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)}
                className={inputTextClassName} />
            </label>
            <label className={labelClassName}> Last name:
                <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} 
                className={inputTextClassName}/>
            </label>
            <label className={labelClassName}> Age:
                <input type="number" value={age} onChange={(e) => setAge(e.target.value)}
                className={inputTextClassName}/>
            </label>
            <label className={labelClassName}> Gender:
            <select 
                value={gender} 
                onChange={(e) => setGender(e.target.value)} 
                className="block my-2 px-2 py-2  rounded-xl"
            >
                    <option value="" disabled>Select gender</option> {}
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                </select>
            </label>
            <label className={labelClassName}> Email:
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)}
                className={inputTextClassName}/>
            </label>
            <label className={labelClassName}> Phone:
                <input type="tel" value={phone} onChange={(e) => setPhone(e.target.value)}
                className={inputTextClassName}/>
            </label>
            <input type="submit" value="Update user data"
                className="bg-color-orange-submit w-52 p-4 mt-4 text-white rounded-xl shadow-md transform transition-transform duration-200 hover:cursor-pointer hover:scale-105"
            />
        </form>
    );
}

export default UpdateUserForm;