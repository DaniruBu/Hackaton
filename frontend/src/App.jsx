import { useState } from 'react'
import './App.css'
import Header from "./components/Header/Header.jsx";
import Filter from "./components/Filter/Filter.jsx";
import PlanColumn from "./components/PlanColumn/PlanColumn.jsx";
import InWorkColumn from "./components/InWorkColumn/InWorkColumn.jsx";
import DoneColumn from "./components/DoneColumn/DoneColumn.jsx";

function App() {

  return (
    <>
        <Header />
        <div className={'mainDiv'}>
            <p className={'textZadachi'}>Задачи</p>
            <Filter />
            <div className={'divWithColumns'}>
                <PlanColumn/>
                <InWorkColumn/>
                <DoneColumn/>
            </div>
        </div>
    </>
  )
}

export default App
