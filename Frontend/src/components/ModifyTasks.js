// EditTask.js
import { useState } from "react"

export default function EditTask({ task }) {
  const [done, setDone] = useState(task.done)

  function handleToggleDone() {
    const updatedDone = !done
    setDone(updatedDone)

    fetch(`http://localhost:8000/api/tasks/${task.id}/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ done: updatedDone })
    })
    .then(res => {
      if (!res.ok) {
        throw new Error('Error al actualizar la tarea')
      }
      return res.json()
    })
    .then(data => {
      console.log('Tarea actualizada:', data)
    })
    .catch(err => console.error(err))
  }

  return (
    <div>
      <label>
        <input type="checkbox" checked={done} onChange={handleToggleDone} />
        Finalizada
      </label>
    </div>
  )
}
