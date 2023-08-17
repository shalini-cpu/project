import React, { useState, useEffect } from 'react';
import useWebSocket from 'react-use-websocket';

const WS_URL = 'ws://localhost:8000/ws/';

function App() {
  const [students, setStudents] = useState([]);
  const { lastMessage, sendJsonMessage } = useWebSocket(WS_URL);

  useEffect(() => {
    if (lastMessage !== null) {
      const newData = JSON.parse(lastMessage.data);
      console.log(newData);
      setStudents(newData);
    }
  }, [lastMessage]);

  const sendMessage = () => {
    const message = {
      action: 'fetch'
    };
    sendJsonMessage(message);
  };

  console.log('students:', students,students.length);

  return (
    <div>
      <h1>Student List</h1>
      <div>
        {/* {Array.isArray(students) && */}
          {students.length>0?(Object.keys(students).map((student,index) => 
            students[student].forEach((element,intt) => (
            <div key={intt}>
              <p>{element.name}</p>
            </div>
))
            )
            ):(<p>No data changed</p>
            )
          
          }
      </div>
      {/* <button onClick={sendMessage}>Send Message</button> */}
    </div>
  );
}

export default App;
