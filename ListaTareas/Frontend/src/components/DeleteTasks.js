export default function DeleteTask({ task }) {
  function handleDelete() {
    fetch(`http://localhost:8000/api/tasks/${task.id}/`, {
      method: 'DELETE'
    })
      .then(res => {
        if (res.ok) {
          console.log(`Tarea con ID ${task.id} eliminada`)
          // Aquí podrías avisar al padre para refrescar
        } else {
          throw new Error('Error al eliminar la tarea')
        }
      })
      .catch(err => console.error(err))
  }

  return (
    <button onClick={handleDelete} style={{ marginLeft: '10px', color: 'red' }}>
      Eliminar
    </button>
  )
}
