import Header from "../Header/Header.jsx";
import './AppChat.css'
import ChatComponent from "../ChatComponent/ChatComponent.jsx";

export default function AppChat() {
    return (
        <>
            <Header/>
            <div className={'mainDivCaht'}>
                <div className={'leftContainer'}>
                    <div className={'leftColumn'}>
                        <ChatComponent/>
                        <ChatComponent/>
                        <ChatComponent/>
                    </div>
                </div>
                <div className={'rightContainer'}>
                    <div className={'imputContainer'}>
                        <input className={'input'} type="text" placeholder={'Напишите что-нибудь...'}/>
                    </div>
                </div>
            </div>
        </>
    )
}