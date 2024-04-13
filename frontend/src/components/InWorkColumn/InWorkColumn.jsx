import './InWorkColumn.css'
import TaskComponent from "../TaskComponent/TaskComponent.jsx";

export default function InWorkColumn() {
    return(
        <div>
            <div className={'headerTaskColumnInWork'}>
                В работе
            </div>
            <div className={'columnInWorkTask'}>
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