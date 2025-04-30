import { useState } from "react"
export default function CreateTask() {
    const [ TextName, setTextName ]= useState ('')
    const [ TextDone, setDone ]= useState ('False')
    function handleTextName (e) {
        setTextName(e.target.value)
    }
    function handleDone (e) {
        setDone(e.target.checked)
    }
    function handleClickForm (e) {
        e.preventDefault() 

        fetch ('http://localhost:8000/api/tasks', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify({
                name: TextName,
                done: TextDone
            })
        }).then(() => {
            setTextName('')
            setDone('False')
        })
    }
    return (
        <form>
            <label htmlFor ="name">Nombre:</label>
            <input id="name" type="text" onChange={handleTextName} value={TextName}/>
            <label htmlFor ="done">Finalizada: SI:</label>
            <input id="done" type="checkbox" onChange={handleDone} value={TextDone}/>
            <input type="submit" value="Crear Tarea" onClick={handleClickForm}/>
        </form>
    )
}