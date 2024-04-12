import './PlanColumn.css'
import TaskComponent from "../TaskComponent/TaskComponent.jsx";

export default function PlanColumn() {
    return(
        <div>
            <div className={'headerTaskColumnPlan'}>
                План
            </div>
            <div className={'columnPlanTask'}>
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