import { useEffect, useState } from 'react'

import TasksBox from './components/TasksBox.js'
import CreateTask from './components/CreateTasks.js'
import ModifyTask from './components/ModifyTasks.js' 
import DeleteTasks from './components/DeleteTasks.js' 


function App() {
  const [tasks, setTasks] = useState([])
  useEffect(() => {
    fetch('http://localhost:8000/api/tasks')
    .then(res => res.json())
    .then(res=> setTasks(res))
  }, [])
  return(
    <main>
      <h1>App de Listado de Tareas</h1>

      <CreateTask />

      {tasks.map(task => (
        <div key={task.id} style={{ border: '1px solid gray', padding: '10px', marginBottom: '0px' }}>
          <TasksBox name={task.name} done={task.done} id={task.id} />
          <ModifyTask task={task} />
          <DeleteTasks task={task} />
        </div>
      ))}
    </main>

  );
}

export default App;