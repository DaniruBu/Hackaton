import './TaskComponent.css'

export default function TaskComponent() {
    return (
        <div>
            <div className={'headerTask'}>
                Task
            </div>
            <div className={'mainTaskComponent'}>
                <p className={'mainText'}>head</p>
                <p className={'secondText'}>headLow</p>
            </div>
        </div>
    )
}