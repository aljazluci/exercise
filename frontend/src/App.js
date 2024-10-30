import { useState } from "react";
import MainContent from "./components/MainContent";
import Sidebar from "./components/Sidebar";

function App() {

  const [selectedUser, setSelectedUser] = useState(null);

  const onUserSelect = (user) => {
    setSelectedUser(user);
  }

  return (
    <div className="flex flex-row">
      <Sidebar onUserSelect={onUserSelect}/>
      <MainContent user={selectedUser}/>
    </div>
  );
}

export default App;
