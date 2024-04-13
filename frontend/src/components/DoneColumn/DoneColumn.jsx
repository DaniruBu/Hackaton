import './DoneColumn.css'
import TaskComponent from "../TaskComponent/TaskComponent.jsx";

export default function DoneColumn() {
    return(
        <div>
            <div className={'headerTaskColumnDone'}>
                Готово
            </div>
            <div className={'columnDoneTask'}>
                <TaskComponent/>
                <TaskComponent/>
                <TaskComponent/>
                <TaskComponent/>
                <TaskComponent/>
                <TaskComponent/>
            </div>
        </div>

    )
}