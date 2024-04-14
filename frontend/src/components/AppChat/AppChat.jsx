import Header from "../Header/Header.jsx";
import './AppChat.css'
import ChatComponent from "../ChatComponent/ChatComponent.jsx";
import axios from 'axios'
import {useEffect, useState} from "react";

export default function AppChat() {
    const [data, setData] = useState([]);
  const [inputValue, setInputValue] = useState('');

  useEffect(() => {
    const url = 'http://127.0.0.1:8000/chat/'  // URL вашего API

    axios.get(url)
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleClick = () => {
    const url = 'http://127.0.0.1:8000/chat/' // URL вашего API
    const data = {
        role: 'user',
      text: inputValue,
    };

    axios.post(url, data)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

    return (
        <>
            <Header/>
            <div className={'mainDivCaht'}>
                <div className={'leftContainer'}>
                    <div className={'leftColumn'}>
                        <a href="#" className={'chatContainer'}>
                            <div className={'circle'}></div>
                            <div className={'textContainerChat'}>
                                <p className={'titleChat'}>Сатурн</p>
                                <p className={'descriptionChat'}>AI помощник построения маршрута</p>
                            </div>
                        </a>
                    </div>
                </div>
                <div className={'rightContainer'}>
                    {data.map(item => (
                        <textarea className={'textArea'} readOnly>{item.answer}</textarea>
                    ))}
                    <div className={'imputContainer'}>
                        <input className={'input'} type="text" onChange={e => setInputValue(e.target.value)} value={inputValue} placeholder={'Напишите что-нибудь...'}/>
                        <input onClick={handleClick} type="submit" className={'inputButton'} value={'Send'}/>
                    </div>
                </div>
            </div>
        </>
    )
}