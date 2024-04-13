import { useState } from 'react'
import './AppTodo.css'
import Filter from "../Filter/Filter.jsx";
import PlanColumn from "../PlanColumn/PlanColumn.jsx";
import InWorkColumn from "../InWorkColumn/InWorkColumn.jsx";
import DoneColumn from "../DoneColumn/DoneColumn.jsx";
import Header from "../Header/Header.jsx";

export default function AppTodo() {
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