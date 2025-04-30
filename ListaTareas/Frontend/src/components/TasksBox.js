export default function TasksBox({name, done, id}) {
    return (
        <article> 
            <h3>{name}</h3>
            <p>{done ? 'Pendiente':'Hecho' }</p>
            <p>ID: {id}</p>
        </article>
    )
}