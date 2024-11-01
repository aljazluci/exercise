import { useState } from "react";
import MainContent from "./components/MainContent";
import Sidebar from "./components/Sidebar";

function App() {

  const [selectedUser, setSelectedUser] = useState(null);

  const onUserSelect = (user) => {
    setSelectedUser(user);
  }

  const contactButtonClassName="px-4 py-2 border w-32 justify-center align-center border-color-orange-border rounded-xl m-4 text-sm";
  // Header and the bottom part
  return (
    <div className="flex flex-col max-h-screen ">
      <div className="text-white header bg-color-dark h-16 p-12 content-center items-center border-b-white border-b fixed min-w-full flex justify-between">
        <img src={`${process.env.PUBLIC_URL}/header_logo.svg`} alt="Logo"/>
        <div className="flex flex-row">
          <div className={contactButtonClassName}>Contact us</div>
          <div className={contactButtonClassName}>Login</div>
        </div>
      </div>
      <div className="flex flex-row flex-1 pt-24">
        <Sidebar onUserSelect={onUserSelect}/>
        <MainContent user={selectedUser}/>
      </div>
    </div>
  );
}

export default App;
