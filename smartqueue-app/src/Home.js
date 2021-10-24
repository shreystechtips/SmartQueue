import React from 'react'
import Sidebar from './Components/Sidebar'
import Title from './Components/Title'

export default function Home() {
    return (
        <div id="home">
            <div className="circle" id="circle-1">
                <Title />
            </div>
            <div className="circle" id="circle-2" />
            <div className="circle" id="circle-3" />
        
            <Sidebar />
        </div>
    )
}
