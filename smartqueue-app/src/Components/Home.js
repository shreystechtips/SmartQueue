import React from 'react'
import Title from './Title'

export default function Home({setPage, setLat, setLng}) {
    return (
        <div id="home">
            <Title setPage={setPage} setLat={setLat} setLng={setLng} />
            <div className="circle" id="circle-1" />
            <div className="circle" id="circle-2" />
            <div className="circle" id="circle-3" />
        </div>
    )
}
