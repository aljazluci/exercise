import { useState } from "react";
import MainContent from "./components/MainContent";
import Sidebar from "./components/Sidebar";

function App() {

  const [selectedUser, setSelectedUser] = useState(null);

  const onUserSelect = (user) => {
    setSelectedUser(user);
  }

  return (
    <div className="flex flex-col max-h-screen">
      <div className="header bg-color-dark h-16 p-12 content-center items-center border-b-white border-b fixed min-w-full">
        <img src={`${process.env.PUBLIC_URL}/header_logo.svg`} alt="Logo"/>
      </div>
      <div className="flex flex-row flex-1 pt-24">
        <Sidebar onUserSelect={onUserSelect}/>
        <MainContent user={selectedUser}/>
      </div>
    </div>
  );
}

export default App;
