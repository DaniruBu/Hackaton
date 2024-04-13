import './ChatComponent.css'

export default function ChatComponent() {
    return (
        <a href="#" className={'chatContainer'}>
            <div className={'circle'}></div>
            <div className={'textContainerChat'}>
                <p className={'titleChat'}>Сатурн</p>
                <p className={'descriptionChat'}>AI помощник построения маршрута</p>
            </div>
        </a>
    )
}